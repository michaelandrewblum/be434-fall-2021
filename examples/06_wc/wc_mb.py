#!/usr/bin/env python3
"""
Author : michaelblum <michaelblum@localhost>
Date   : 2021-09-23
Purpose: Word Count Program
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Word Counter',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        metavar='FILES',
                        nargs='+',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin],
                        help='Input file(s)')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Word Count"""

    args = get_args()
    total_lines, total_words, total_chars = 0, 0, 0

    for arg in args.files:

        line_num, word_num, char_num = 0, 0, 0
        for line in arg:
            line_num += 1
            word_num += len(line.split())
            for char in line:
                char_num += 1

        total_lines += line_num
        total_words += word_num
        total_chars += char_num

        print('{:8}{:8}{:8} {}'.format(line_num, word_num, char_num, arg.name))


# --------------------------------------------------
if __name__ == '__main__':
    main()
