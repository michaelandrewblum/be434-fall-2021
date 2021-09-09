#!/usr/bin/env python3
# Purpose: Say hello allowing a name parameter

import argparse

def get_args():
    parser = argparse.ArgumentParser(description='say hello to the world or to anything else with --name parameter')
    parser.add_argument('-n', '--name', metavar='name',
                        default='Stranger', help='Name to greet')
    parser.add_argument('-g', '--greeting', metavar='greeting', 
                        default='Howdy', help='greeting to use')
    parser.add_argument('-e', '--excited', metavar='excited',
                        default='.', nargs='?', const="!", help='how excited you should be')
    return parser.parse_args()

def main():
    args = get_args()
    print(args.greeting + ', ' + args.name + args.excited)



if __name__ == '__main__':
    main()
