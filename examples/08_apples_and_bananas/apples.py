#!/usr/bin/env python3
"""
Author : michaelblum <michaelblum@localhost>
Date   : 2021-10-04
Purpose: Apples and Bananas
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='vowel',
                        type=str,
                        default='a',
                        choices=list('aeiouAEIOU'))

    args = parser.parse_args()

    if os.path.isfile(args.text):
        with open(args.text, 'rt', encoding='utf-8') as fh:
            args.text = fh.read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    vowel = args.vowel
    text = [
            vowel if c in 'aeiou' else vowel.upper()
            if c in 'AEIOU' else c for c in args.text
    ]

    print(''.join(text))


# --------------------------------------------------
if __name__ == '__main__':
    main()
