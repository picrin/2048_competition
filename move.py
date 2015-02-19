import sys
args = sys.argv[1:]
if not args or not (args[0] == "left" or args[0] == "right" or args[0] == "up" or args[0] == "down"):
    print("USAGE:\n\tpython move.py <left|right|up|down>")
    exit(1)
with open("write_move", "w") as pipe:
    pipe.write(args[0] + "\n")
