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
                        metavar='DIR',
                        default='split')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    # print(args)
    # print(os.path.isdir(args.outdir))
    # print(f'>>> "{args.outdir}"')

    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)

    input_files = []
    file_names = []

    for file in args.files:
        input_files.append(file)
        file_names.append(os.path.splitext(file.name))

    # print(input_files)
    # print(file_names)

    for file in input_files:
        basename = os.path.basename(file.name)
        root, ext = os.path.splitext(basename)

        fwd_out = os.path.join(args.outdir, root + '_1' + ext)
        rev_out = os.path.join(args.outdir, root + '_2' + ext)
        
        reader = list(SeqIO.parse(file.name, 'fasta'))

        fwd_seq_list = []
        rev_seq_list = []

        for num, rec in enumerate(reader):
            if num % 2 == 0:
                fwd_seq_list.append(('>' + rec.description, str(rec.seq)))
            else:
                rev_seq_list.append(('>' + rec.description, str(rec.seq)))

        # print(len(fwd_seq_list), len(rev_seq_list), len(reader))

        with open(fwd_out, 'wt') as fh_fwd:
            for seq in fwd_seq_list:
                fh_fwd.write(seq[0] + '\n')
                fh_fwd.write(seq[1] + '\n')

        with open(rev_out, 'wt') as fh_rev:
            for seq in rev_seq_list:
                fh_rev.write(seq[0] + '\n')
                fh_rev.write(seq[1] + '\n')

    print(f'Done, see output in "{args.outdir}"')
        

# --------------------------------------------------
if __name__ == '__main__':
    main()
