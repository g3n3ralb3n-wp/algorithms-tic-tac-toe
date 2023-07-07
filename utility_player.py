# Import libraries
from board import Board
from conditional_player import ConditionalPlayer
from argmax import argmax

# Represents a tic-tac-toe agent evaluating moves with a utility function
# Note: this agent inherits from a conditional player
# Note: it uses it's conditional logic for making decisive moves
class UtilityPlayer(ConditionalPlayer):

    # Gets the next move using an utility function
    # and conditional logic for decisive moves
    def get_next_move(self, board: Board) -> int:
        
        move = self.get_decisive_move(board)
        if move:
            return move
        else:
            lines = self.get_utility_of_lines(board)
            spaces = self.get_utility_of_spaces(board, lines)
            # best_space = spaces.index(max(spaces))
            best_space = self.best_space(board, spaces)
            return best_space
                
    def is_line_empty(self, board: Board, line):
        
        if board.spaces[line[0]] == "-" \
                and board.spaces[line[1]] == "-" \
                and board.spaces[line[2]] == "-":
            return True
        return False
        
    def is_line_full(self, board: Board, line):
        
        space_0 = board.spaces[line[0]]
        space_1 = board.spaces[line[1]]
        space_2 = board.spaces[line[2]]
        if space_0 != "-" and space_1 != "-" and space_2 != "-":
            return True
        return False
    
    #returns list of utility for each space
    def get_utility_of_spaces(self, board: Board, utility_of_lines: list):
        space_dict = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}
        max_value = max(utility_of_lines)
        max_indices = [i for i, j in enumerate(utility_of_lines) if j == max_value]
        
        for i in range(len(board.spaces)):
            if board.spaces[i] != "-":
                space_dict[f"{i}"] = -99
        
        for index in max_indices:
            for space in board.lines[index]:
                if board.spaces[space] == "-" and utility_of_lines[index] != 0:
                    space_dict[f"{space}"] += 1
        utility_of_spaces = list(space_dict.values())
        
        return utility_of_spaces

    # returns list of utlity for each line
    def get_utility_of_lines(self, board: Board) -> list:

        line_utilities = []
        for line in board.lines:
            if self.is_line_empty(board, line):
                utility = 0
            elif self.is_line_full(board, line):
                utility = -10
            else:
                utility = self.get_line_utility(board, line)
            line_utilities.append(utility)
        
        return line_utilities
    
    # returs utility for specific lines using utility function
    def get_line_utility(self, board: Board, line) -> int:

        agent_marks = 0
        opponent_marks = 0
        for space in line:
            if board.spaces[space] == self.mark:
                agent_marks += 1
            elif board.spaces[space] == self.opponent_mark:
                opponent_marks += 1
        line_utility = 3*agent_marks - opponent_marks
        
        return line_utility

    # returns index of best space 
    # based on all row, col, and diagonal of the space
    def best_space(self, board: Board, utility_of_spaces: list) -> int:
        best_space_indices = [i for i, j in enumerate(utility_of_spaces) \
                              if j == max(utility_of_spaces)]
        best_space_utilities = []
        
        for space in best_space_indices:
            best_space_utility = []
            for line in board.lines:
                if space in line:
                    best_space_utility.append(self.get_line_utility(board, line))
            x = sum(best_space_utility)
            best_space_utilities.append(x)
        best_space_index = best_space_utilities.index(max(best_space_utilities))
        best_space = best_space_indices[best_space_index]

        return best_space