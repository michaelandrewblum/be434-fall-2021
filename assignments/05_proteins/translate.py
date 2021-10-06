#!/usr/bin/env python3
"""
Author : michaelblum <michaelblum@localhost>
Date   : 2021-09-29
Purpose: Translate DNA/RNA to AA
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='DNA/RNA sequence')

    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        required=True,
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.txt')

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
    codon_lst = [args.text.upper()[i:i+n] for i in range(0, len(args.text), n)]

    # translate codons
    translation = []
    for codon in codon_lst:
        # if codon in lookup:
        #     translation.append(lookup[codon])
        # else:
        #     translation.append('-')

        translation.append(lookup.get(codon, '-'))

    translate_str = ''.join(translation)

    # write translation to output file
    # with open(args.outfile.name, 'wt', encoding='utf-8') as out_fh:
    #     out_fh.write(translate_str)
    #     out_fh.close()

    print(translate_str, file=args.outfile)

    print(f'Output written to "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
