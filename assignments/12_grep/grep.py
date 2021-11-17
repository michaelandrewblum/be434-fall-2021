#!/usr/bin/env python3
"""
Author : michaelblum <michaelblum@localhost>
Date   : 2021-11-16
Purpose: Python grep
"""

import argparse
import sys
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python grep',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern',
                        metavar='PATTERN',
                        help='Search pattern')

    parser.add_argument('files',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+',
                        help='Input file(s)')

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        action='store_true')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    out = args.outfile

    for file in args.files:
        for line in file:
            if args.insensitive:
                if re.search(args.pattern.lower(), line.lower()):
                    if len(args.files) > 1:
                        print(file.name + ':', end='', file=out)
                    print(line.rstrip(), file=out)
            else:
                if re.search(args.pattern, line):
                    if len(args.files) > 1:
                        print(file.name + ':', end='', file=out)
                    print(line.rstrip(), file=out)


# --------------------------------------------------
if __name__ == '__main__':
    main()
