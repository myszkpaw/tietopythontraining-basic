# Chess king moves horizontally, vertically or diagonally to any adjacent cell.
# Given two different cells of the chessboard, determine whether a king can go from the first cell to the second in one move.
# The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the
# first cell, and then the last two - for the second cell.
# The program should output YES if a king can go from the first cell to the second in one move, or NO otherwise.

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

possible_move_list = [(x1, y1+1), (x1+1, y1+1), (x1+1, y1), (x1+1, y1-1), (x1, y1-1), (x1-1, y1-1), (x1-1, y1), (x1-1, y1+1)]
if (x2, y2) in possible_move_list:
    print("YES")
else:
    print("NO")
