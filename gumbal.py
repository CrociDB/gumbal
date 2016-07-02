import os
import sys

from gumbal.gumbal_parser import GumbalParser
import gumbal.gumbal_info as gumbal_info

if __name__ == '__main__':
    parser = GumbalParser(os.path.realpath(__file__))
    parser.parse(sys.argv)
    gumbal_info.print_message("\n")
