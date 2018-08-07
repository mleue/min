import os


def read_filenames(path):
  """Read the filenames in a dir.

  Arguments:
    path  -- the path to read filenames from

  Returns:
    filenames -- list of filename strings
  """
  filenames = os.listdir(path)
  return filenames


def read_docs_file(filepath):
  """Read a docs file.

  Returns:
    filestring -- string read from the file
  """
  with open(filepath, encoding='utf-8') as docs_file:
    return docs_file.read()
