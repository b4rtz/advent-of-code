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
        total_numbers = len(numbers_to_draw)
        lines = file.readlines()
        boards = get_bingo_boards(lines)

        first_five = numbers_to_draw[:5]
        winning_board = [board for board in boards if check_board(board, first_five) == 'BINGO']
        #print(winning_board)
        if (winning_board):
            print("BINGO")
        else:
            print("No bingos yet")

        i = 6
        while (i < len(numbers_to_draw)):
            winning_board = np.array([board for board in boards if check_board(board, numbers_to_draw[:i]) == 'BINGO'])
            if (np.any(winning_board)):
                print(f"BINGO after {i} numbers drawn")
                break
            else:
                print("No bingos yet")
                i+=1

        # print(winning_board)
        score = calculate_score(winning_board, numbers_to_draw[:i])
        return score

def calculate_score(winning_board, numbers: List[int]):
    print(winning_board)
    final_num_drawn = numbers[-1]
    # print(final_num_drawn)
    board_numbers = winning_board.flatten()
    unmarked_numbers = [num for num in board_numbers if num not in numbers]
    sum_of_unmarked = sum(unmarked_numbers)
    score = sum_of_unmarked * final_num_drawn
    return score

def check_board(board, numbers: List[int]):
    # print(board)
    for row in board:
        if (check_row_or_col(row, numbers)):
            return "BINGO"

    for col in board.T:
        if (check_row_or_col(col, numbers)):
            return "BINGO"

    return ""

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
