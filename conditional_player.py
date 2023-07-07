# Import libraries
from player import Player
from board import Board


# Represents a tic-tac-toe agent that evaluates moves using conditional logic
class ConditionalPlayer(Player):

    # Returns the next move given the current board state
    def get_next_move(self, board: Board) -> int:
        """_summary_
            Returns the next move to play
        Args:
            board (Board): board state.
        Returns:
            int: the space to put the mark on.
        """
        move = self.get_decisive_move(board)
        if move:
            return move
        else:
            return self.get_non_decisive_move(board)

    def get_decisive_move(self, board: Board) -> int:
        """_summary_
        This function checks if there is a winning move.  If not,
        it checks for a defensive move.
        Args:
            board (Board): board state.        
        Returns:
            int: position to mark in the board.
        """
        move = None

        # Check for winning move:
        for line in board.lines:
            if (
                board.spaces[line[0]] ==
                board.spaces[line[1]] == self.mark
                and board.is_open_space(line[2])
            ):
                move = line[2]
            elif (
                board.spaces[line[0]] ==
                board.spaces[line[2]] == self.mark
                and board.is_open_space(line[1])
            ):
                move = line[1]
            elif (
                board.is_open_space(line[0])
                and board.spaces[line[1]] ==
                board.spaces[line[2]] == self.mark
            ):
                move = line[0]

        if move is None:
            # Check for defensive move:
            for line in board.lines:
                if (
                    board.spaces[line[0]] ==
                    board.spaces[line[1]] == self.opponent_mark
                    and board.is_open_space(line[2])
                ):
                    move = line[2]
                elif (
                    board.spaces[line[0]] ==
                    board.spaces[line[2]] == self.opponent_mark
                    and board.is_open_space(line[1])
                ):
                    move = line[1]
                elif (
                    board.is_open_space(line[0])
                    and board.spaces[line[1]] ==
                    board.spaces[line[2]] == self.opponent_mark
                ):
                    move = line[0]

        return move

    def get_non_decisive_move(self, board: Board) -> int:
        """_summary_
            This function will look for a space to mark.
            It first check if the board is empty, then returns 0.
            If the center space is empty, return 4.
            If any corner is empty, return a corner.
            And finally, if a space between is empty, return that space.
        Args:
            board (Board): board state.
        Returns:
            int: position to mark on the board.            
        """
        move = None
        if board.is_empty():
            move = 0
        elif board.is_open_space(4):
            move = 4
        elif board.is_open_space(0):
            move = 0
        elif board.is_open_space(2):
            move = 2
        elif board.is_open_space(6):
            move = 6
        elif board.is_open_space(8):
            move = 8
        else:
            for index, _ in enumerate(board.spaces):
                if board.is_open_space(index):
                    move = index
                    break

        return move