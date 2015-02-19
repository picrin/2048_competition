from __future__ import print_function
import lib2048 as _2048
import os

read_move = "write_move"
write_board = "read_board"

def pretty_board(board):
    for row in board:
        print()
        for elem in row:
            print(elem, end=" ")
    print()

def inject_and_complete(board, moves, filename):
    _2048.inject_random(board)
    complete(board, moves)

def complete(board, moves):
    with open(write_board, 'w') as fifo:
        fifo.write(str(board))
        fifo.write("\n")
    pretty_board(board)
    print(moves)
if not os.path.exists("history"):
    os.makedirs("history")
try:
    os.unlink(write_board)
except OSError:
    pass
try:
    os.unlink(read_move)
except OSError:
    pass
os.mkfifo(write_board)
os.mkfifo(read_move)

while True:
    filename = str(_2048.randr.randint(0, 10**20))
    os.mknod(os.path.join("history", filename))
    board = _2048.create_board()
    _2048.inject_random(board)
    moves = 1
    inject_and_complete(board, moves, filename)
    while True:
        updown = False
        downright = False
        with open(read_move, 'r') as fifo:
            command = fifo.readline()[:-1]
            if command == "left":
                pass
            elif command == "right":
                downright = True
            elif command == "down":
                downright = True
                updown = True
            elif command == "up":
                updown = True
            else:
                continue
        board_json = _2048.next_board(board, updown, downright)
        newboard = board_json["newboard"]
        if _2048.gameover(newboard):
            with open(write_board, "w") as fifo:
                fifo.write("[]")
            break
        if newboard == board:
            complete(board, moves)
            continue
        else:
            board = newboard
            moves += 1
            inject_and_complete(board, moves, filename)
            with open(os.path.join("history", filename), "a") as history:
                history.write(str(board_json))

