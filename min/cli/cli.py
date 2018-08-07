import os
import fire
import argparse
from .read_docs import read_filenames, read_docs_file

here_path = os.path.dirname(os.path.realpath(__file__))
identifiers = ['commands', 'topics']
TOPICS_PATH = os.path.join(here_path, '..', 'docs', 'topics')


def min(command):
  """Run min cli."""
  names_to_filename = {}
  for identifier in identifiers:
    path = os.path.join(here_path, '..', 'docs', identifier)
    filenames = read_filenames(path)
    names_to_filename[identifier] = {filename.split('.')[0]: os.path.join(path, filename) for filename in filenames}

  # if no command was given, list available commands
  if not command:
    for identifier in identifiers:
      print("Available {}:".format(identifier))
      print(list(names_to_filename[identifier].keys()))
  else:
    try:
      if command in names_to_filename['commands']:
        print(read_docs_file(names_to_filename['commands'][command]))
      elif command in names_to_filename['topics']:
        print(read_docs_file(names_to_filename['topics'][command]))
      else:
        raise ValueError
    except ValueError:
      print("No entry for command {}.".format(command))


def min_cli():
  """Fire entry point."""
  #import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument("command", help="the command you want the minpage for",
                      nargs='?', default='', type=str)
  args = parser.parse_args()
  min(command=args.command)
