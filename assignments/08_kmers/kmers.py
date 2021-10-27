#!/usr/bin/env python3
"""
Author : michaelblum <michaelblum@localhost>
Date   : 2021-10-20
Purpose: Finding Common K-mers
"""

import argparse
from typing import TextIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common kmers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1',
                        metavar='FILE1',
                        type=argparse.FileType('rt'),
                        help='Input file 1')

    parser.add_argument('file2',
                        metavar='FILE2',
                        type=argparse.FileType('rt'),
                        help='Input file 2')

    parser.add_argument('-k',
                        '--kmer',
                        help='K-mer size',
                        metavar='int',
                        type=int,
                        default=3)

    args = parser.parse_args()

    if args.kmer < 1:
        parser.error(f'--kmer "{args.kmer}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    kmerdict1 = count_kmers(args.file1, args.kmer)
    kmerdict2 = count_kmers(args.file2, args.kmer)

    common_kmers = {}

    for kmer in kmerdict1.keys() & kmerdict2.keys():
        common_kmers[kmer] = (kmerdict1[kmer], kmerdict2[kmer])

    for kmer, count in common_kmers.items():
        print(f'{kmer:10} {count[0]:5} {count[1]:5}')


# --------------------------------------------------
def find_kmers(seq: str, k: int) -> list:
    """ Find k-mers in string """

    n = len(seq) - k + 1
    return [] if n < 1 else [seq[i:i + k] for i in range(n)]


# --------------------------------------------------
def count_kmers(fh: TextIO, k: int) -> dict:
    """ count k-mers in file """

    kmerdict = {}

    for line in fh:
        for word in line.rstrip().split():
            for kmer in find_kmers(word, k):
                kmerdict[kmer] = kmerdict.get(kmer, 0) + 1

    return kmerdict


# --------------------------------------------------
def test_find_kmers():
    """ Test find_kmers """

    assert find_kmers('', 1) == []
    assert find_kmers('ACTG', 1) == ['A', 'C', 'T', 'G']
    assert find_kmers('ACTG', 2) == ['AC', 'CT', 'TG']
    assert find_kmers('ACTG', 3) == ['ACT', 'CTG']
    assert find_kmers('ACTG', 4) == ['ACTG']
    assert find_kmers('ACTG', 5) == []


# --------------------------------------------------
if __name__ == '__main__':
    main()
