#!/usr/bin/env python3
"""
Author : michaelblum <michaelblum@localhost>
Date   : 2021-10-06
Purpose: Common Words
"""

import argparse
import sys


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
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Common words between files"""

    args = get_args()

    word_list_file1 = []
    word_list_file2 = []

    # Create list of unique words in first file
    for line in args.FILE1:

        word_list_file1.extend(line.rsplit())
    word_list_file1 = list(set(word_list_file1))
    word_list_file1.sort()

    # Create list of unique words in second file
    for line in args.FILE2:

        word_list_file2.extend(line.rsplit())
    word_list_file2 = list(set(word_list_file2))
    word_list_file2.sort()

    # Print list of words common between both files
    for word in word_list_file1:
        if word in word_list_file2:
            print(word, file=args.outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()
