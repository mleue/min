import os


def read_docs_filenames():
  """Read the filenames of all docs files.

  Returns:
    docs_path -- path string to docs directory
    filenames -- list of filename strings
  """
  here_path = os.path.dirname(os.path.realpath(__file__))
  docs_path = os.path.join(here_path, '..', 'docs')
  filenames = os.listdir(docs_path)

  return docs_path, filenames


def read_docs_file(filepath):
  """Read a docs file.

  Returns:
    filestring -- string read from the file
  """
  with open(filepath, encoding='utf-8') as docs_file:
    return docs_file.read()
