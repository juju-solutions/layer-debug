import os

dir = os.environ["SOS_SCRIPT_DIR"]


def open_file(path, *args, **kwargs):
    """ Open a file within the SOS script dir """
    return open(os.path.join(dir, path), *args, **kwargs)
