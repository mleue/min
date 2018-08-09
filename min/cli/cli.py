import argparse
from .io_ops import read_resources
from .io_ops import print_available_resources, print_minpage


def min(resource, show_topics):
  """Run min cli.

  Arguments
    resource -- string, identifier of the requested resource
    show_topics -- bool, whether to query for topics instead of bash commands
  """
  category = 'commands'
  if show_topics:
    category = 'topics'

  id2filepath = read_resources(category)

  # if no resource was specified, list available resources
  if not resource:
    print_available_resources(id2filepath, category)
  # otherwise try to find the requested resource and print the minpage
  else:
    print_minpage(resource, id2filepath, category)


def min_cli():
  """CLI entry point."""
  parser = argparse.ArgumentParser()
  parser.add_argument("resource", help="which resource you want a minpage for",
                      nargs='?', default='', type=str)
  parser.add_argument("-t", help="help for topics", action="store_true")
  args = parser.parse_args()
  min(resource=args.resource, show_topics=args.t)
