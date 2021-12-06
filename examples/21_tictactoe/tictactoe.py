#!/usr/bin/env python3
"""
Author : michaelblum <michaelblum@localhost>
Date   : 2021-11-08
Purpose: Rock the Casbah
"""

import argparse
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-b',
                        '--board',
                        help='The state of the board',
                        metavar='str',
                        type=str,
                        default='.' * 9)

    parser.add_argument('-p',
                    '--player',
                    help='Player',
                    metavar='str',
                    type=str,
                    choices='XOxo',
                    default=None)

    parser.add_argument('-c',
                        '--cell',
                        help='Cell 1-9',
                        metavar='int',
                        type=int,
                        choices=range(1,10),
                        default=None)

    args = parser.parse_args()

    if not re.match('^[XO.]{9}$', args.board):
        parser.error(f'--board "{args.board}" must be 9 characters of ., X, O')

    if any([args.player, args.cell]) and not all([args.player, args.cell]):
        parser.error('Must provide both --player and --cell')

    if args.cell:
        if not args.board[args.cell - 1] == '.':
            parser.error(f'--cell "{args.cell}" already taken')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    board = list(args.board)

    if args.cell:
        board[args.cell - 1] = args.player


    print(format_board(board))
    print(find_winner(board))


# --------------------------------------------------
def format_board(board):
    """ Format tic-tac-toe board """

    dashes = '-------------'
    cells = '| {} | {} | {} |'

    board = [str(i) if c == '.' else c for i, c in enumerate(board, start=1)]

    return '\n'.join([dashes, cells.format(*board[:3]),
    dashes,
    cells.format(*board[3:6]),
    dashes,
    cells.format(*board[6:10]), dashes])
   

# --------------------------------------------------
def find_winner(board):
    """ Find winner """

    winning = 
    return 'No winner.'


# --------------------------------------------------
if __name__ == '__main__':
    main()
