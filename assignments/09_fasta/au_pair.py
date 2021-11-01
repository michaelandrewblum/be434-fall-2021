#!/usr/bin/env python3
"""
Author : michaelblum <michaelblum@localhost>
Date   : 2021-10-26
Purpose: Split interleaved/paired reads
"""

import argparse
import os
import errno
from pathlib import Path
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
                        metavar='str',
                        default='split')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    print(args)
    print(os.path.isdir(args.outdir))
    print(f'"{os.path.dirname(args.outdir)}"')

    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)

    input_files = []
    file_names = []

    for file in args.files:
        input_files.append(file)
        file_names.append(os.path.splitext(file.name))

    fwd_out = os.path.join(args.outdir, os.path.basename(file_names[0][0]) + '_1' + file_names[0][1])
    rev_out = os.path.join(args.outdir, os.path.basename(file_names[0][0]) + '_2' + file_names[0][1])

    for file in input_files:
        input_seqs = list(SeqIO.parse(file, 'fasta'))

    fwd_seq_list = []
    rev_seq_list = []

    for num, seq in enumerate(input_seqs):
        if num % 2 == 0:
            fwd_seq_list.append([seq.id, str(seq.seq)])
        else:
            rev_seq_list.append([seq.id, str(seq.seq)])

    with open(fwd_out, 'wt') as fh_fwd:
        for seq in fwd_seq_list:
            fh_fwd.write(seq[0])
            fh_fwd.write(seq[1])

        

# --------------------------------------------------
if __name__ == '__main__':
    main()
