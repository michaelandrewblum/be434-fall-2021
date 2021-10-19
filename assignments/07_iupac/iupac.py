#!/usr/bin/env python3
"""
Author : michaelblum <michaelblum@localhost>
Date   : 2021-10-13
Purpose: Expanding DNA IUPAC Codes into Regular Expressions
"""

import argparse
import sys
import os
# from subprocess import getstatusoutput

# Homework assignment passes all tests in test suite but also has added ability
# to handle lowercase letters, invalid characters, printing errors to file or
# stdout, and allowing strings, files, or both as inputs

# Try:
# $ python3 iupac.py ARCG DcYw sequences.txt ACGQ (-o out.txt) (-e err.txt)


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Expand IUPAC codes',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq',
                        metavar='SEQ',
                        nargs='+',
                        help='Input sequence(s)')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    parser.add_argument('-e',
                        '--errfile',
                        help='Error filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stderr)

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

    # initialize list of sequences
    sequences = []

    # add to list all sequences input as string or files
    for sequence in args.seq:
        if os.path.isfile(sequence):
            with open(sequence, encoding='utf-8') as fh:
                sequences.extend(fh.read().split())
        else:
            sequences.append(sequence)

    # create regex strings from input sequences
    for seq in sequences:

        seq = seq.upper()   # handle sequences with lowercase characters

        regex = ''.join([iupac_dict.get(char, '-') for char in seq])

        # if invalid chars in sequence print error to stderr or to file
        if '-' in regex:
            errlist = [base for base in seq if base not in iupac_dict]
            errors = ', '.join(errlist)
            print(f'Unknown base(s) ({errors}) in sequence "{seq}"',
                  file=args.errfile)

        # print sequence and regex string to stdout or to file
        else:
            print(seq, regex, file=args.outfile)

    # message about printing output to file
    if os.path.isfile(args.outfile.name):
        print(f'Done, see output in "{args.outfile.name}"')

    # message about printing errors to file
    if os.path.isfile(args.errfile.name):
        print(f'Error file generated, see errors in "{args.errfile.name}"')


# --------------------------------------------------
# def test_lowercase():
#     """Test for lowercase input"""

#     prg = './iupac.py'
#     seq = 'ACtg'
#     rv, out = getstatusoutput(f'{prg} {seq}')
#     assert rv == 0
#     assert out == 'ACTG ACTG'


# --------------------------------------------------
if __name__ == '__main__':
    main()
