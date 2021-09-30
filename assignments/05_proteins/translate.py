#!/usr/bin/env python3
"""
Author : michaelblum <michaelblum@localhost>
Date   : 2021-09-29
Purpose: Translate DNA/RNA to AA
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='DNA/RNA sequence')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        action='store_true',
                        default='out.txt')

    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        required=True,
                        type=argparse.FileType('rt'),
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    lookup = {}

    # generate dictionary of codons
    for line in args.codons:
        lookup[line.split()[0]] = line.split()[1]

    # break input text into codons
    n = 3
    codon_list = [args.text.upper()[i:i+n] for i in range(0, len(args.text), n)]

    # translate codons
    translation = []
    for codon in codon_list:
        if codon in lookup:
            translation.append(lookup[codon])
        else:
            translation.append('-')

    translate_str = ''.join(translation)

    # write translation to output file
    out_fh = open('out.txt', 'wt') if args.outfile else sys.stdout
    out_fh.write(translate_str)
    out_fh.close()

    print(f'Output written to "{args.outfile}".')
        



# --------------------------------------------------
if __name__ == '__main__':
    main()
