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

    if args.kmer <= 0:
        parser.error(f'--kmer "{args.kmer}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    kmer_counts = {}

    kmers_file1, unique_kmers1 = unique_kmers(args.file1, args.kmer)

    kmers_file2, unique_kmers2 = unique_kmers(args.file2, args.kmer)

    common_kmers = unique_kmers1.intersection(unique_kmers2)

    for kmer in common_kmers:
        kmer_counts[kmer] = (kmers_file1.count(kmer), kmers_file2.count(kmer))

    for kmer in sorted(common_kmers):
        print(f'{kmer:10} {kmer_counts[kmer][0]:5} {kmer_counts[kmer][1]:5}')


# --------------------------------------------------
def find_kmers(seq, k):
    """ Find k-mers in string """

    n = len(seq) - k + 1
    return [] if n < 1 else [seq[i:i + k] for i in range(n)]


# --------------------------------------------------
def unique_kmers(fh: TextIO, k: int):
    """ Find unique k-mers in file """

    kmers = []
    unique = set()

    for line in fh:
        for word in line.rstrip().split():
            kmers.extend(find_kmers(word, k))
            unique.update(find_kmers(word, k))

    return kmers, unique


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
