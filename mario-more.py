from cs50 import get_int

while True:
    height = get_int("Give me a pyramid's height, please\n")
    if height >= 1 and height <= 8:
        break

h = height
for i in range(h):

        #first pyramid spaces
        for k in range (h - i - 1):
            print(" ", end="")
        #first pyramid #
        for j in range (i+1):
            print("#", end="")
        #2 spaces
        print("  ", end="")
        #second pyramid #
        for j in range (i+1):
            print("#", end="")
        print("\n", end="")
