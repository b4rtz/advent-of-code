# pass the time by playing bingo with a giant squid
# first line in bingo_boards.txt is the numbers to call
# each board is a 5x5 grid of numbers
# first board to have all numbers in any column or row called wins
# calculate score of the first winner by
#   first adding together all unmarked numbers
#   then by multiplying the sum with the last number called
from typing import List
import numpy as np
import sys

def play_bingo(filename, part):
    with open(filename) as file:
        numbers_to_draw = [int(num) for num in file.readline().rstrip().split(',')]
        lines = file.readlines()
        boards = get_bingo_boards(lines)

        i = 1
        winning_boards = []
        while (i < len(numbers_to_draw)):
            for board in boards:
                if (check_board(board, numbers_to_draw[:i])):
                    if (new_winner(winning_boards, board)):
                        winning_boards.append((np.array(board), numbers_to_draw[i]))

            if (len(winning_boards) == len(boards)):
                break
            else:
                i+=1

        # print(winning_board)
        # print(len(winning_boards))
        winning_board = winning_boards[0] if part == '1' else winning_boards[-1]
        (winner, final_num) = winning_board
        score = calculate_score(winner, numbers_to_draw[:final_num])
        return score

def new_winner(winning_boards : List[np.ndarray], board: np.ndarray):
    if (len(winning_boards) == 0):
        return True
    for (winner, number_drawn) in winning_boards:
        if ((winner == board).all()):
            #print("not a new winner")
            return False

    #print("new winner!")
    return True

def calculate_score(winning_board, numbers: List[int]):
    print(len(numbers))
    board_numbers = winning_board.flatten()
    final_num = numbers[-1]
    # print(board_numbers)
    unmarked_numbers = [num for num in board_numbers if num not in numbers]
    sum_of_unmarked = sum(unmarked_numbers)
    score = sum_of_unmarked * final_num
    return score

def check_board(board, numbers: List[int]):
    for row in board:
        if (check_row_or_col(row, numbers)):
            return True

    for col in board.T:
        if (check_row_or_col(col, numbers)):
            return True

    return False

def check_row_or_col(arry, numbers: List[int]):
    return all(num in numbers for num in arry)

def get_bingo_boards(lines: List[str]):
    boards = []
    linescount = len(lines)
    i = 0
    while i < linescount:
        if (lines[i].rstrip() == ''):
            i+=1
            continue
        else:
            board = np.array([[int(num) for num in line.rstrip().split(' ') if num != ''] for line in lines[i:i+5]])
            # print(board)
            boards.append(board)
            i+=5

    # print(boards)
    return boards

if __name__ == '__main__':
    file = sys.argv[1]
    part = sys.argv[2]

    score_of_winner = play_bingo(file, part)
    print("SCORE OF WINNING BOARD")
    print(score_of_winner)
