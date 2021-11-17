#!/usr/bin/env python3
"""
Author : michaelblum <michaelblum@localhost>
Date   : 2021-11-09
Purpose: Run-length encoding/data compression
"""

import argparse
import os
from itertools import groupby


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run-length encoding/data compression',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='DNA text or file')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    if not os.path.isfile(args.str):
        print(group_repeated(args.str))
    else:
        with open(args.str, 'rt', encoding='utf-8') as fh:
            for line in fh:
                seq = line.rstrip()

                print(group_repeated(seq))


# --------------------------------------------------
def group_repeated(input_str: str) -> str:
    """ group repeated characters in string as character followed
        by number of repititions, e.g. AAA is replaced by A3 """

    repeated = [''.join(group) for _, group in groupby(input_str)]

    newstr = ''
    for chars in repeated:
        if len(chars) == 1:
            newstr += chars
        else:
            newstr += chars[0]
            newstr += str(len(chars))

    return newstr


# --------------------------------------------------
if __name__ == '__main__':
    main()
