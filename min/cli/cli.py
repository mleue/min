import os
import fire
from .read_docs import read_docs_filenames, read_docs_file


def min(command):
  """Run min cli."""
  docs_path, filenames = read_docs_filenames()
  commands = {filename.split('.')[0]: os.path.join(docs_path, filename)
              for filename in filenames}

  try:
    print(read_docs_file(commands[command]))
  except KeyError:
    print("No entry for command {}.".format(command))


def min_cli():
  """Fire entry point."""
  fire.Fire(min)
