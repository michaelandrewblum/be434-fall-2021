#!/usr/bin/env python3
"""
Author : michaelblum <michaelblum@localhost>
Date   : 2021-09-22
Purpose: File Concatenation Program
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python cat',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+',
                        default=[sys.stdin],
                        help='Input file(s)')

    parser.add_argument('-n',
                        '--number',
                        help='Number the lines',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Concatenate files with enumerate"""

    args = get_args()

    for arg in args.files:
        for line_num, line in enumerate(arg, start=1):
            if args.number:
                print('{:6}{}{}'.format(line_num, '\t', line.rstrip()))
            else:
                print(line.rstrip())


# --------------------------------------------------
if __name__ == '__main__':
    main()
