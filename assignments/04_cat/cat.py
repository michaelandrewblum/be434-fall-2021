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
        description='Concatentate files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+',
                        default=[sys.stdin],
                        help='Files to concatenate')

    parser.add_argument('-n',
                        '--number',
                        help='If true, print line numbers, otherwise do not.',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Concatenate files"""

    args = get_args()

    for arg in args.files:
        line_num = 1
        for line in arg:
            if args.number:
                print('{:6}{}{}'.format(line_num, '\t', line.rstrip()))
            else:
                print(line.rstrip())
            line_num += 1


# --------------------------------------------------
if __name__ == '__main__':
    main()
