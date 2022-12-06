import yaml
from env import GITHUB_USER, GITHUB_TOKEN
import requests
from misc import copy_and_overwrite, inplace_change, git_push, get_snapshot_metadata, get_restake_params, get_live_peers
import glob
import shutil
import os

environments = {
    'mainnet': ['agoric', 'cosmoshub', 'gravitybridge', 'jackal', 'kujira', 'stride', 'teritori', 'rebus', 'osmosis'],
    'testnet': ['agoric', 'aura', 'defund', 'gitopia', 'haqq', 'jackal', 'nibiru', 'ollo', 'quicksilver', 'sei',
                'teritori', 'uptick']
}


def get_replacement_params(chain, chain_environment):
    print(chain, chain_environment)
    replacements = {'${PROJECT_NAME}': chain}

    if chain_environment == 'testnet':
        chain = f'{chain}_{chain_environment}'

    url = f'https://raw.githubusercontent.com/kj89/ansible-cosmos/main/group_vars/{chain}.yml'

    resp = requests.get(url, auth=(GITHUB_USER, GITHUB_TOKEN))
    print(resp.status_code)

    if resp.status_code == 200:
        data = yaml.safe_load(resp.content)
        print(f"*************{data['chain_git_repos']}*******************")

        # workaround for gravity-bridge
        if data['chain_git_repos']:
            git_dir = list(data['chain_git_repos'].keys())[-1]
            git_url = data['chain_git_repos'][git_dir]
        else:
            git_dir = 'gravity-bin'
            git_url = ''
            latest_binary_version = data['chain_upgrades'][-1]['binary_src'].split('/')[-2]
            replacements['${LATEST_BINARY_VERSION}'] = latest_binary_version

        chain_name = data['chain_user']
        chain_id = data['chain_id']
        chain_port_prefix = str(data['chain_port_prefix'])
        chain_app = data['chain_binary']
        chain_peer = data['chain_tenderseed_seeds'].split('@')[0]
        chain_tendeseed_peer = data['chain_tenderseed_peer'].split('@')[0]
        chain_denom = data['chain_denom']
        chain_min_gas_price = data['chain_min_gas_prices']
        chain_service = data['chain_service']
        chain_binary_src = data['chain_binary_src']
        chain_website = data['chain_website']
        chain_short_description = data['chain_short_description']

        if 'chain_dirs' in data:
            chain_dir = data['chain_dirs'][0]
        else:
            chain_dir = data['chain_dir']

        if 'chain_wasm' in data:
            recover_wasm = '### Download latest wasm\n\n' \
                           "{% hint style='info' %}\n" \
                           'Currently state sync does not support copy of the `wasm` folder. Therefore, you will have to download it manually.\n' \
                           '{% endhint %}\n\n' \
                           '```bash\n' \
                           f'curl -L https://snapshots.kjnodes.com/{chain_service}/wasm_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/{chain_dir}\n' \
                           '```'
            chain_wasm = 'ON'
        else:
            recover_wasm = ''
            chain_wasm = 'OFF'
        replacements['${CHAIN_WASM}'] = chain_wasm
        replacements['${RECOVER_WASM}'] = recover_wasm

        replacements['${GIT_DIR}'] = git_dir
        replacements['${GIT_URL}'] = git_url
        replacements['${CHAIN_NAME}'] = chain_name
        replacements['${CHAIN_ID}'] = chain_id
        replacements['${CHAIN_PORT}'] = chain_port_prefix
        replacements['${CHAIN_BINARY_SRC}'] = chain_binary_src
        replacements['${CHAIN_SERVICE}'] = chain_service
        replacements['${CHAIN_APP}'] = chain_app
        replacements['${CHAIN_DIR}'] = chain_dir
        replacements['${CHAIN_DENOM}'] = chain_denom
        replacements['${CHAIN_PEER}'] = chain_peer
        replacements['${CHAIN_TENDERSEED_PEER}'] = chain_tendeseed_peer
        replacements['${MIN_GAS_PRICE}'] = chain_min_gas_price
        replacements['${CHAIN_WEBSITE}'] = chain_website
        replacements['${CHAIN_SHORT_DESCRIPTION}'] = chain_short_description

        latest_version_name = data['chain_upgrades'][-1]['name']
        replacements['${LATEST_VERSION_NAME}'] = latest_version_name

        print(data['chain_upgrades'])
        if 'tag' in data['chain_upgrades'][-1].keys():
            genesis_version_name = 'genesis'
            genesis_version_tag = data['chain_upgrades'][0]['tag']
            latest_version_name = data['chain_upgrades'][-1]['name']
            latest_version_tag = data['chain_upgrades'][-1]['tag']
            replacements['${GENESIS_VERSION_NAME}'] = genesis_version_name
            replacements['${GENESIS_VERSION_TAG}'] = genesis_version_tag
            replacements['${LATEST_VERSION_NAME}'] = latest_version_name
            replacements['${LATEST_VERSION_TAG}'] = latest_version_tag

            if latest_version_name == genesis_version_name:
                replacements['${BINARY_CURRENT}'] = genesis_version_name
                replacements['${COMPILE_LATEST_VERSION}'] = ''
            else:
                replacements['${BINARY_CURRENT}'] = f'upgrades/{latest_version_name}'
                replacements['${COMPILE_LATEST_VERSION}'] = f"\n# Compile latest version {latest_version_tag}\n" \
                                                            f"git checkout {latest_version_tag}\n" \
                                                            f"make build\n" \
                                                            f"mkdir -p $HOME/{chain_dir}/cosmovisor/upgrades/{latest_version_name}/bin\n" \
                                                            f"mv {chain_binary_src} $HOME/{chain_dir}/cosmovisor/upgrades/{latest_version_name}/bin/\n" \
                                                            f"rm {chain_binary_src} -rf"

        # Get restake data
        restake_valoper, restake_run_time = get_restake_params(chain_name)
        if restake_valoper:
            replacements['${RESTAKE}'] = f'## Restake\n\n' \
                                         f'[Restake with kjnodes]' \
                                         f'(https://restake.app/{chain_name}/{restake_valoper}) ' \
                                         f'(every day at {restake_run_time})'
        else:
            replacements['${RESTAKE}'] = ''

        # Get live peers
        live_peers, live_peers_count = get_live_peers(chain_name)
        replacements['${CHAIN_LIVE_PEERS}'] = live_peers
        replacements['${CHAIN_LIVE_PEERS_COUNT}'] = live_peers_count

        # Get snapshot metadata
        snapshot_size_gb, snapshot_block, snapshot_version, snapshot_age = get_snapshot_metadata(chain_name)
        if snapshot_version == 'genesis':
            snapshot_version = genesis_version_tag
        replacements['${SNAPSHOT_SIZE}'] = snapshot_size_gb
        replacements['${SNAPSHOT_BLOCK}'] = snapshot_block
        replacements['${SNAPSHOT_AGE}'] = snapshot_age
        replacements['${SNAPSHOT_VERSION}'] = snapshot_version

        if chain_environment == 'testnet':
            replacements['${KEYRING_BACKEND}'] = 'test'
        else:
            replacements['${KEYRING_BACKEND}'] = 'file'

    else:
        print("Request failed!")

    return replacements


def generate_summary_page(environment):
    result = []
    for chain in environments[environment]:
        print(chain)
        chain_prettyname = chain.capitalize()
        if chain == 'cosmoshub':
            chain_prettyname = 'Cosmos Hub'
        if chain == 'gravitybridge':
            chain_prettyname = 'Gravity Bridge'

        result.append(f'* [{chain_prettyname}]({environment}/{chain}/README.md)\n'
                      f'  * [Installation]({environment}/{chain}/installation/README.md)\n'
                      f'  * [Snapshot]({environment}/{chain}/snapshot/README.md)\n'
                      f'  * [State sync]({environment}/{chain}/state-sync/README.md)\n'
                      f'  * [Useful commands]({environment}/{chain}/useful-commands/README.md)\n\n')
    return result


def generate_home_page(environment):
    result = []
    for chain in environments[environment]:
        print(chain)
        chain_prettyname = chain.capitalize()
        if chain == 'cosmoshub':
            chain_prettyname = 'Cosmos Hub'
        if chain == 'gravitybridge':
            chain_prettyname = 'Gravity Bridge'
        result.append(f'<img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/{chain}.png"'
                      f' alt="" data-size="line"> [{chain_prettyname}]({environment}/{chain}/)\n\n')

    return result


def main():
    shutil.copyfile('./templates/SUMMARY.md', './docs/SUMMARY.md')
    shutil.copyfile('./templates/README.md', './docs/README.md')
    for environment in environments:

        src = f'${environment.upper()}_SUMMARY'
        dst = ''.join(generate_summary_page(environment))
        inplace_change('./docs/SUMMARY.md', src, dst)

        src = f'${environment.upper()}_HOME'
        dst = ''.join(generate_home_page(environment))
        inplace_change('./docs/README.md', src, dst)

        for chain in environments[environment]:
            src_dir = './templates/project_page'
            dst_dir = f'./docs/{environment}/{chain}'
            copy_and_overwrite(src_dir, dst_dir)

            # Override chain specific pages if there are any
            if os.path.isdir(f'./templates/{chain}'):
                shutil.copytree(f'./templates/{chain}', dst_dir, dirs_exist_ok=True)

            replace_list = get_replacement_params(chain, environment)
            print(replace_list)
            files = [f for f in glob.glob(f'{dst_dir}/**/*[.md]', recursive=True)]
            for f in files:
                print(f)
                for src, dst in replace_list.items():
                    inplace_change(f, src, dst)

    git_push()


if __name__ == '__main__':
    main()
