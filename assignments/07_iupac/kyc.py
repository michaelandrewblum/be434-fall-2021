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

    parser.add_argument('seqs',
                        metavar='SEQ',
                        nargs='+',
                        type=argparse.FileType('rt'),
                        help='Input sequence file(s)')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    iupac_dict = {
        'A': 'A',
        'C': 'C',
        'G': 'G',
        'T': 'T',
        'U': 'U',
        'R': '[AG]',
        'Y': '[CT]',
        'S': '[GC]',
        'W': '[AT]',
        'K': '[GT]',
        'M': '[AC]',
        'B': '[CGT]',
        'D': '[AGT]',
        'H': '[ACT]',
        'V': '[ACG]',
        'N': '[ACGT]'
    }

    for fh in args.seqs:
        for seq_num, seq in enumerate(map(str.rstrip, fh), start=1):
            # regex = ''.join([iupac_dict.get(base, '-') for base in seq])
            # if '-' in regex:
            #     print(seq, 'Unknown base in sequence', file=sys.stderr)
            # else:
            #     print(seq, regex, file=args.outfile)

            regex = ''
            for base in seq:
                if base in iupac_dict:
                    regex += iupac_dict[base]
                else:
                    print(seq,
                          f'Line {seq_num}: Unknown base "{base}"',
                          file=sys.stderr)
                    break

            print(seq, regex, file=args.outfile)

    if os.path.isfile(args.outfile.name):
        print(f'Done, see output in "{args.outfile.name}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
