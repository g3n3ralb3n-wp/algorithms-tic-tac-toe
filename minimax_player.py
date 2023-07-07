# Import libraries
from player import Player
from board import Board
from argmax import argmax


# Represents a brute-force minimax agent
class MinimaxPlayer(Player):

    # Gets the next move given the current board state
    def get_next_move(self, board: Board) -> int:
        # enter code