import yaml
from env import GITHUB_USER, GITHUB_TOKEN
import requests
import datetime
from misc import get_file_list, get_time_ago, copy_and_overwrite, inplace_change

chains = ['kujira', 'stride', 'teritori', 'rebus']


def get_file_metadata(chain):
    r = requests.head(f"https://s3.eu-central-1.amazonaws.com/snapshots.kjnodes.com/{chain}/snapshot_latest.tar.lz4")
    size_bytes = r.headers.get('Content-Length')
    size_gb = f"{round(int(size_bytes) / (1 << 30), 2)} GB"
    block = r.headers.get('x-amz-meta-blockheight')
    last_modified = r.headers.get('Last-Modified')
    stripped = datetime.datetime.strptime(last_modified, "%a, %d %b %Y %H:%M:%S %Z")
    age = get_time_ago(stripped)
    # print(f'{chain} | {block} | {last_modified} | {age} | {size_gb}')

    return size_gb, block, age


def get_replacement_params(chain):
    snapshot_size_gb, snapshot_block, snapshot_age = get_file_metadata(chain)
    url = f'https://raw.githubusercontent.com/kj89/ansible-cosmos/main/group_vars/{chain}.yml'

    resp = requests.get(url, auth=(GITHUB_USER, GITHUB_TOKEN))
    replacements = {}
    if resp.status_code == 200:
        data = yaml.safe_load(resp.content)

        git_dir = list(data['chain_git_repos'].keys())[0]
        git_url = data['chain_git_repos'][git_dir]
        genesis_version = data['chain_upgrades'][0]['tag']
        latest_version = data['chain_upgrades'][-1]['tag']
        chain_name = data['chain_user']
        chain_id = data['chain_id']
        chain_port_prefix = str(data['chain_port_prefix'])
        chain_app = data['chain_binary']
        chain_dir = data['chain_dir']
        chain_denom = data['chain_denom']
        chain_min_gas_price = data['chain_min_gas_prices']

        replacements['${GIT_DIR}'] = git_dir
        replacements['${GIT_URL}'] = git_url
        replacements['${GENESIS_VERSION}'] = genesis_version
        replacements['${LATEST_VERSION}'] = latest_version
        replacements['${CHAIN_NAME}'] = chain_name
        replacements['${CHAIN_ID}'] = chain_id
        replacements['${CHAIN_PORT}'] = chain_port_prefix
        replacements['${CHAIN_APP}'] = chain_app
        replacements['${CHAIN_DIR}'] = chain_dir
        replacements['${CHAIN_DENOM}'] = chain_denom
        replacements['${MIN_GAS_PRICE}'] = chain_min_gas_price
        replacements['${SNAPSHOT_SIZE}'] = snapshot_size_gb
        replacements['${SNAPSHOT_BLOCK}'] = snapshot_block
        replacements['${SNAPSHOT_AGE}'] = snapshot_age

    else:
        print("Request failed!")

    return replacements


def main():

    for chain in chains:
        dst_dir = f'./docs/{chain}'
        copy_and_overwrite('./templates', dst_dir)
        replace_list = get_replacement_params(chain)
        files = get_file_list(dst_dir)
        for f in files:
            for src, dst in replace_list.items():
                inplace_change(f, src, dst)


if __name__ == '__main__':
    main()
