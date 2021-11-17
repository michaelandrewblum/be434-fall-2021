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
        bases = [''.join(grp) for num, grp in groupby(args.str)]
        newseq = ''
        for base in bases:
            if len(base) == 1:
                newseq += base
            else:
                newseq += base[0]
                newseq += str(len(base))
        print(newseq)
    else:
        with open(args.str, 'rt', encoding='utf-8') as fh:
            for line in fh:
                seq = line.rstrip()

                bases = [''.join(grp) for num, grp in groupby(seq)]

                newseq = ''
                for base in bases:
                    if len(base) == 1:
                        newseq += base
                    else:
                        newseq += base[0]
                        newseq += str(len(base))

                print(newseq)


# --------------------------------------------------
if __name__ == '__main__':
    main()
