# That's an example solution. Note language agnostics. Before you run the code
# make sure that the 2048 deamon is running (run python 2048_deamon.py in the
# current directory)

# Let's say that our dummy solution checks if there are at least 2 tiles that
# can be merged by moving left. If there aren't, the algorithm will make a
# random move.
import json, random, subprocess
move_no = 1
while True:
# we first have to read our board. The board is always a json array with 4
# nested arrays or an empty json array. You have to be able to parse this json
# yourself. Example json is:
#
#      row1    ,     row2    ,     row3    ,      row4   
# [[4, 2, 2, 0], [2, 0, 0, 0], [0, 0, 2, 0], [0, 0, 0, 0]]
# 
# which corresponds to the following board:
# 4 2 2 0
# 2 0 0 0
# 0 0 2 0
# 0 0 0 0
# empty json array [] denotes game over.
    # this single call tells us the status of the board. If the code hangs here
    # infinitely that's probably because you're not running the 2048 deamon!
    # You can call this line in any programming language, it's a system call.
    board_json = subprocess.check_output(["python", "check_board.py"])
    print(board_json, move_no)
    move_no += 1
    board = json.loads(board_json.decode("utf-8"))
    # empty board means that your game is over :(
    if board == []:
        print("game over :(")
        exit(0)
    # let's check if moving left gives us a merge
    go_left = False
    for column_no in range(4 - 1):
        for row_no in range(4):
            if board[row_no][column_no] == board[row_no][column_no + 1] and board[row_no][column_no] != 0:
                go_left = True
    print(go_left)
    if go_left:
        # this single call instructs the deamon to make a move. This can be
        # called from any programming language
        subprocess.call(["python","move.py", "left"])
    else:
        possible_moves = ["left", "up", "right", "down"]
        random_move = random.choice(possible_moves)
        print(random_move)
        subprocess.call(["python", "move.py", random_move])
