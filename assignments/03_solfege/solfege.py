#!/usr/bin/env python3
"""
Author : michaelblum <michaelblum@localhost>
Date   : 2021-09-20
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Solfege',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('solfege_arg',
                        metavar='str',
                        nargs='+',
                        help='Enter solfege')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Print Solfege"""


    args = get_args()
    solfege = {'Do': 'A deer, a female deer',
               'Re': 'A drop of golden sun',
               'Mi': 'A name I call myself',
               'Fa': 'A long long way to run',
               'Sol': 'A needle pulling thread',
               'La': 'A note to follow sol',
               'Ti': 'A drink with jam and bread'}

    for arg in args.solfege_arg:
        # if arg[0].islower():
        #     arg = arg[0].upper() + arg[1:]
        if arg in solfege:
            print(arg, ", ", solfege[arg], sep='')
        else:
            print('I don\'t know "', arg, '"', sep='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
