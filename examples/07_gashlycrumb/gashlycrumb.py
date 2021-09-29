#!/usr/bin/env python3
"""
Author : michaelblum <michaelblum@localhost>
Date   : 2021-09-29
Purpose: Gashlycrumb
"""

import argparse
from collections import defaultdict


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='letter',
                        nargs='+',
                        help='Letter(s)')

    parser.add_argument('-f',
                        '--file',
                        metavar='FILE',
                        help='A readable file',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Print lines in file beginning with given letters."""

    args = get_args()

    # Create collection dictionary with lists to collect multiple lines
    lookup = defaultdict(list)

    # Populate dictionary from file
    for line in args.file:

        if line[0].upper() in lookup:
            lookup[line[0].upper()].append(line.rstrip())
        else:
            lookup[line[0].upper()] = [line.rstrip()]

    # Print lines that start with given letter in the file.
    # Return inline message if not found.
    for char in args.letter:
        if char.upper() in lookup:
            print(*lookup.get(char.upper()), sep='\n')
        else:
            print(f'I do not know "{char}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
