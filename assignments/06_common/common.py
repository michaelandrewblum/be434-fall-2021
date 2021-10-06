#!/usr/bin/env python3
"""
Author : michaelblum <michaelblum@localhost>
Date   : 2021-10-06
Purpose: Common Words
"""

import argparse
import sys
# import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE1',
                        help='Input file 1',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('FILE2',
                        help='Input file 2',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=[sys.stdout])

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    list_file1 = []
    list_file2 = []

    for line in args.FILE1:
        # line = line.translate(str.maketrans('', '', string.punctuation))
        list_file1.extend(line.rsplit())
    list_file1 = list(set(list_file1))
    list_file1.sort()
    # print(list_file1)

    for line in args.FILE2:
        # line = line.translate(str.maketrans('', '', string.punctuation))
        list_file2.extend(line.rsplit())
    list_file2 = list(set(list_file2))
    list_file2.sort()
    # print(set(list_file2))

    for word in list_file1:
        if word in list_file2:
            print(word)


# --------------------------------------------------
if __name__ == '__main__':
    main()
