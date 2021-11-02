#!/usr/bin/env python3
"""
Author : michaelblum <michaelblum@localhost>
Date   : 2021-11-01
Purpose: Rock the Casbah
"""

import argparse
import random
import csv


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='CSV input file of exercises',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='inputs/exercises.csv')

    parser.add_argument('-n',
                        '--num',
                        help='Number of exercises',
                        metavar='exercises',
                        type=int,
                        default=4)
                        
    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)
    
    parser.add_argument('-e',
                        '--easy',
                        help='Halve the reps',
                        action='store_true')

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    wod = []
    exercizes = read_csv(args.file)
    for name, low, high in random.sample(exercizes, k=args.num):
        reps = random.randint(low, high)
        if args.easy:
            reps = round(reps/2)
        wod.append((name, reps))

    print(tabulate(wod, headers=('Exercize', 'Reps')))


# --------------------------------------------------
def read_csv(fh):
    """ Read csv file """

    reader = csv.DictReader(fh, delimiter=',')
    exercizes = []

    for rec in reader:
        low, high = map(int, rec['reps'].split('-'))
        exercizes.append((rec['exercise'], low, high))

    return exercizes


# --------------------------------------------------
if __name__ == '__main__':
    main()
