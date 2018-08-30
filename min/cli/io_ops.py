import os
from pydoc import pager
from .config import DOCS_PATH


def get_filenames(path):
  """Read the filenames in a dir and yield them.

  Arguments
    path  -- the path to read filenames from

  Returns
    filenames -- list of filename strings (without hidden files)
  """
  for f in os.listdir(path):
    if not f.startswith('.'):
      yield f


def read_docs_file(filepath):
  """Read a docs file.

  Arguments
    filepath -- path to the docs file to read

  Returns
    filestring -- string read from the file
  """
  with open(filepath, encoding='utf-8') as docs_file:
    return docs_file.read()


def get_filename_from_filepath(filepath):
  """Parse the filename (without extension) from a filepath.

  Arguments:
    filepath -- filepath string

  Returns:
    filename -- name of the file in the path (without extension)
  """
  basename = os.path.basename(filepath)
  return os.path.splitext(basename)[0]


def print_available_resources(id2filepath, category):
  """Print the available resources for that category.

  Arguments
    id2filepath -- mapping resource identifiers to their filepaths
    category -- the resource category
  """
  print("Available {}:".format(category))
  print(sorted(list(id2filepath.keys())))


def print_minpage(resource, id2filepath, category):
  """Print the minpage for the requested resource if available.

  Arguments
    id2filepath -- mapping resource identifiers to their filepaths
    resource -- the requested resource (e.g.a bash command)
    category -- the resource category
  """
  try:
    pager(read_docs_file(id2filepath[resource]))
  except KeyError:
    print(("No entry for resource '{}' among the available {}.\n"
           "\n"
           "Do you think min should have it?\n"
           "Then please open an issue at {} \n"
           "Thanks in advance.")
           .format(resource, category, 'https://github.com/mleue/min/issues'))


def read_resources(category):
  """Read in the available resources for that category.

  Arguments
    category -- the resource category

  Returns
    id2filepath -- mapping resource identifiers to their filepaths
  """
  resources_path = os.path.join(DOCS_PATH, category)
  # list of resource filepaths
  filepaths = [os.path.join(resources_path, filename)
               for filename in get_filenames(resources_path)]
  # map resource identifiers to filepaths
  id2filepath = {get_filename_from_filepath(filepath): filepath
                 for filepath in filepaths}

  return id2filepath
