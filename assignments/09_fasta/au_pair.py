#!/usr/bin/env python3
"""
Author : michaelblum <michaelblum@localhost>
Date   : 2021-10-26
Purpose: Split interleaved/paired reads
"""

import argparse
import os
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Split interleaved/paired reads',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'),
                        help='Input file(s)')

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        default='split')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)

    for file in args.files:
        basename = os.path.basename(file.name)
        root, ext = os.path.splitext(basename)

        fwd_out = os.path.join(args.outdir, root + '_1' + ext)
        rev_out = os.path.join(args.outdir, root + '_2' + ext)

        fwd_seq_list, rev_seq_list = interleaved_fasta(file)

        write_fasta(fwd_seq_list, fwd_out)
        write_fasta(rev_seq_list, rev_out)

    print(f'Done, see output in "{args.outdir}"')


# --------------------------------------------------
def write_fasta(sequences, outfile):
    """ Write fasta lines to file """

    with open(outfile, 'wt', encoding='utf-8') as fh:
        for seq in sequences:
            fh.write(seq[0] + '\n')
            fh.write(seq[1] + '\n')


# --------------------------------------------------
def interleaved_fasta(fh):
    """ Create sequences for interleaved fasta data """

    reader = list(SeqIO.parse(fh.name, 'fasta'))
    fwd_seq_list = []
    rev_seq_list = []

    for num, rec in enumerate(reader):
        if num % 2 == 0:
            fwd_seq_list.append(('>' + rec.description, str(rec.seq)))
        else:
            rev_seq_list.append(('>' + rec.description, str(rec.seq)))

    return fwd_seq_list, rev_seq_list


# --------------------------------------------------
def test_interleaved_fasta():
    """ Test iterleaved_fasta function """

    with open('./inputs/reads1.fa', 'rt', encoding='utf-8') as fh:

        fwd, rev = interleaved_fasta(fh)

        assert fwd == [
            ('>M10991:61:000000000-A7EML:1:1101:14011:1001 1:N:0:28',
             'NGCTCCTAGGTCGGCATGATGGGGGAAGGAGAGCATGGGAAGAAATGAGAGAGTAGCAA'),
            ('>M10991:61:000000000-A7EML:1:1201:15411:3101 1:N:0:28',
             'NGCTCCTAGGTCGGCATGATGGGGGAAGGAGAGCATGGGAAGAAATGAGAGAGTAGCAA')
        ]
        assert rev == [
            ('>M10991:61:000000000-A7EML:1:1101:14011:1001 2:N:0:28',
             'NGCTCCTAGGTCGGCATGACGCTAGCTACGATCGACTACGCTAGCATCGAGAGTAGCAA'),
            ('>M10991:61:000000000-A7EML:1:1201:15411:3101 2:N:0:28',
             'CGCTAGCTACGACTCGACGACAGCGAACACGCGATCGATCGGAAATGAGAGAGTAGCAA')
        ]


# --------------------------------------------------
if __name__ == '__main__':
    main()
