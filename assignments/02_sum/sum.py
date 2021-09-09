#!/usr/bin/env python3
# Purpose: Sum any number of inputted integers together.

import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Add numbers')
    parser.add_argument('integers', metavar='INT', type=int, nargs='+',
                        help='Numbers to add')
    return parser.parse_args()

def main():
    args = get_args()
    answer = args.integers
    print(' + '.join(map(str, answer)) + ' = ' + str(sum(args.integers)))

if __name__ == '__main__':
    main()