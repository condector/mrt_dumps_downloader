import os
import logging

# Application log
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
log = logging.getLogger()

def create_and_set_folder(main, subdir):
    path = subdir + '/'
    sub = '/' + path
    os.makedirs(main + sub, exist_ok=True)
    dir_path = os.path.join(main, path)
    return dir_path


def file_path(folder, filename):
    return os.path.join(folder, filename)


main_dir = os.path.abspath(os.path.dirname(__file__))
dumps_dir = create_and_set_folder(main_dir, 'dumps')

