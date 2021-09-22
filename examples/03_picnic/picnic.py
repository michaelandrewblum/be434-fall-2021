#!/usr/bin/env python3
# Purpose: list items you're bringing to a picnic.

import argparse

def get_args():
    parser = argparse.ArgumentParser(description='List picnic items')
    parser.add_argument('picnic_items', metavar='picnic', type=str, nargs='+',
                        help='List of items brought to picnic')
    parser.add_argument('-s','--sorted', action='store_true',
                        help='Should list be sorted or no')
    return parser.parse_args()

def main():
    args = get_args()
    items = args.picnic_items

    if args.sorted:
        items.sort()
    if len(args.picnic_items) == 1:
        print('You are bringing ' + str(items[0]) + '.')
    elif len(args.picnic_items) == 2:
        print('You are bringing ' + items[0] + ' and ' + items[1] + '.')
    else:
        answer_3 = ', '.join(map(str,args.picnic_items[:-1]))
        print('You are bringing ' + answer_3 + ', and ' + str(args.picnic_items[-1]) + '.')

if __name__ == '__main__':
    main() 
