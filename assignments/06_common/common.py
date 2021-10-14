#!/usr/bin/env python3
"""
Author : michaelblum <michaelblum@localhost>
Date   : 2021-10-06
Purpose: Find Common Words
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

    words_file1 = set()
    words_file2 = set()

    # Create list of unique words in first file
    for line in args.FILE1:
        words_file1.update(line.split())

    # Create list of unique words in second file
    for line in args.FILE2:
        words_file2.update(line.split())

    print('\n'.join(words_file1.intersection(words_file2)), file=args.outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()
