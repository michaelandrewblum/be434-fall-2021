#!/usr/bin/env python3
"""
Author : michaelblum <michaelblum@localhost>
Date   : 2021-10-21
Purpose: Bottles of beer song
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='How many bottles',
                        metavar='int',
                        type=int,
                        default=10)

    args = parser.parse_args()

    if not args.num > 0:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    one = ('1 bottle of beer on the wall,\n'
           '1 bottle of beer,\n'
           'Take one down, pass it around,\n'
           'No more bottles of beer on the wall!')

    two = ('2 bottles of beer on the wall,\n'
           '2 bottles of beer,\n'
           'Take one down, pass it around,\n'
           '1 bottle of beer on the wall!')

    if args.num == 1:
        print(one)
    elif args.num == 2:
        print(two, one, sep='\n\n')
    else:
        for num in reversed(range(3, args.num + 1)):
            print(f'{num} bottles of beer on the wall,\n',
                  f'{num} bottles of beer,\n',
                  'Take one down, pass it around,\n',
                  f'{num - 1} bottles of beer on the wall!\n',
                  sep='')
        print(two, one, sep='\n\n')


# --------------------------------------------------
def verse(bottle):
    """ Sing verse of bottle song """

    return bottle


# --------------------------------------------------
def test_verse(bottle):
    """ Test verse function """

     

# --------------------------------------------------
if __name__ == '__main__':
    main()
