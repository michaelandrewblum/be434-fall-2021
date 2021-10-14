#!/usr/bin/env python3
"""
Author : michaelblum <michaelblum@localhost>
Date   : 2021-10-13
Purpose: Expanding DNA IUPAC Codes into Regular Expressions
"""

import argparse
import sys
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Expand IUPAC codes',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('SEQ',
                        metavar='SEQ',
                        nargs='+',
                        help='Input sequence(s)')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    args = parser.parse_args()

    for seq in args.SEQ:
        seq = seq.upper()
        for char in seq:
            if char not in 'ACGTURYSWKMBDHVN':
                parser.error(f'Unknown character ("{char}") in input sequence')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    iupac_dict = {'A': 'A', 'C': 'C', 'G': 'G', 'T': 'T', 'U': 'U',
                  'R': '[AG]', 'Y': '[CT]', 'S': '[GC]', 'W': '[AT]',
                  'K': '[GT]', 'M': '[AC]', 'B': '[CGT]', 'D': '[AGT]',
                  'H': '[ACT]', 'V': '[ACG]', 'N': '[ACGT]'}

    for seq in args.SEQ:
        seq = seq.upper()
        regex = ''
        for char in seq:
            regex += iupac_dict.get(char)
        print(seq, regex, file=args.outfile)

    if os.path.isfile(args.outfile.name):
        print(f'Done, see output in "{args.outfile.name}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
