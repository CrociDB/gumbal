import sys

from gumbal.gumbal_parser import GumbalParser

if __name__ == '__main__':
    parser = GumbalParser()
    parser.parse(sys.argv)
