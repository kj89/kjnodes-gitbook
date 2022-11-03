import os
import shutil
import datetime
from git import Repo


def git_push():
    try:
        repo = Repo('.')
        repo.git.add(update=True)
        repo.index.commit('Update gitbook contents')
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occurred while pushing the code')


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


def get_file_list(path):
    return [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
