"""Sample DocOpt program

Usage:
  sampledocopt.py arg1 <name>...
  sampledocopt.py arg1 <name> [--opt=<n>]
  sampledocopt.py (-h | --help)
  sampledocopt.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --opt=<n>     Uses an optional argument
"""

from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version="Sample DocOpt program, v0.1")
    print "Arguments:\n{}".format(arguments)
