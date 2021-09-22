#1/usr/bin/env python3
# Purpose: To alert the captain of anything off the larboard bow

import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Items off the larboard bow')
    parser.add_argument('item', 
                        metavar='str', 
                        type=str,
                        help='What was noticed off the larboard bow'
                        )
    return parser.parse_args()

def main():
    args = get_args()
    vowels = ['a', 'e', 'i', 'o', 'u']
    if args.item[0][0] in vowels:
        article = 'an'
    else:
        article = 'a'

    print('Ahoy, Captain, ' + article + ' ' + str(args.item) + ' off the larboard bow!')

if __name__ == '__main__':
    main() 
