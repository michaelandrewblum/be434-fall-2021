#!/usr/bin/env python3
"""
Author : michaelblum <michaelblum@localhost>
Date   : 2021-12-06
Purpose: Python clone of tac
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python clone of tac',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+',
                        default=[sys.stdin],
                        help='Input file(s)')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Concatenate files with enumerate"""

    args = get_args()

    for arg in args.files:
        lines = []
        for line in arg:
            lines.append(line.rstrip())

        if len(lines) == 0:
            print('', end='', file=args.outfile)

        for line in reversed(lines):
            print(line, file=args.outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()
