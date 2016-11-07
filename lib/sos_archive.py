import os

dir = os.environ["SOS_ARCHIVE_DIR"]

def open_file(path, *args, **kwargs):
  """ Open a file within the SOS archive """
  return open(os.path.join(dir, path), *args, **kwargs)
