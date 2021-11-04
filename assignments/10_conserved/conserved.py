#!/usr/bin/env python3
"""
Author : michaelblum <michaelblum@localhost>
Date   : 2021-11-03
Purpose: Find conserved bases
"""

import argparse
from collections import defaultdict


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find conserved bases',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    seqs = defaultdict(list)

    for line in args.file:
        print(line.rstrip())
        for i, num in enumerate(line.rstrip()):
            seqs[i].append(num)

    result = ''

    for value in seqs.values():
        if len(set(value)) == 1:
            result += '|'
        else:
            result += 'X'

    print(result)


# --------------------------------------------------
if __name__ == '__main__':
    main()
