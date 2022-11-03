import yaml
import os
import shutil
from env import GITHUB_USER, GITHUB_TOKEN
import requests
import datetime

chains = ['kujira', 'stride', 'teritori', 'rebus']


def display_time(seconds, granularity=1):
    intervals = (
        ('weeks', 604800),  # 60 * 60 * 24 * 7
        ('days', 86400),  # 60 * 60 * 24
        ('hours', 3600),  # 60 * 60
        ('minutes', 60),
        ('seconds', 1),
    )

    result = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(round(value), name))

    return ' '.join(result[:granularity]) + ' ago'


def get_time_ago(start_time):
    now = datetime.datetime.utcnow()
    delta_in_seconds = ((now - start_time).total_seconds())
    delta = display_time(abs(delta_in_seconds))

    return delta


def inplace_change(filename, old_string, new_string):
    # Safely read the input filename using 'with'
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            print('"{old_string}" not found in {filename}.'.format(**locals()))
            return

    # Safely write the changed content, if found in the file
    with open(filename, 'w') as f:
        print('Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals()))
        s = s.replace(old_string, new_string)
        f.write(s)


def copy_and_overwrite(from_path, to_path):
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)


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
        chain_app = data['chain_binary']
        chain_dir = data['chain_dir']
        chain_denom = 'unknown'
        chain_min_gas_price = data['chain_min_gas_prices']

        replacements['${GIT_DIR}'] = git_dir
        replacements['${GIT_URL}'] = git_url
        replacements['${GENESIS_VERSION}'] = genesis_version
        replacements['${LATEST_VERSION}'] = latest_version
        replacements['${CHAIN_NAME}'] = chain_name
        replacements['${CHAIN_ID}'] = chain_id
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


def get_file_list(path):
    return [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]


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
