import random
import sys

SIZE = (4, 4)
START = (0, 0)
END = (SIZE[0] - 1, SIZE[1] - 1)

if sys.getrecursionlimit() < SIZE[0] * SIZE[1]:
    sys.setrecursionlimit(SIZE[0] * SIZE[1])
# if max recursion limit is lower than needed, adjust it

N, S, E, W = 1, 2, 4, 8
# directions translated into bitnums to store information on all cleared walls in one variable per cell

GO_DIR = {N: (0, -1), S: (0, 1), E: (1, 0), W: (-1, 0)}
# dictionary with directions translated to digging moves

REVERSE = {E: W, W: E, N: S, S: N}
# when a passage is dug from a cell, the other cell obtains the reverse passage (logically)

maze = list(list(0 for i in range(SIZE[0])) for j in range(SIZE[1]))

seed = random.randint(0, 1000)
random.seed(seed)


def print_solution_matrix(solution_matrix):
    for i in solution_matrix:
        for j in i:
            print(str(j) + " ", end="")
        print("")
    print('\n\n')


# build the maze
def dig(x, y):
    # digs passage from a cell (x, y) to some unvisited cell
    directions = [N, E, W, S]
    random.shuffle(directions)
    # shuffles directions each time for more randomness
    for direction in directions:
        new_x = x + GO_DIR[direction][0]
        new_y = y + GO_DIR[direction][1]
        if (new_y in range(SIZE[1])) and \
                (new_x in range(SIZE[0])) and \
                (maze[new_y][new_x] == 0):
            # checks if the new cell is not visited
            maze[y][x] |= direction
            maze[new_y][new_x] |= REVERSE[direction]
            # if so, apply info on passages to both cells
            dig(new_x, new_y)
            # repeat recursively


def check():
    # displays the cells' values for check-up
    for i in range(SIZE[1]):
        for j in range(SIZE[0]):
            print(" " * (1 - (maze[i][j] // 10)) +
                  str(maze[i][j]), end='|')
        print('')


def draw():
    # displays the maze
    print("\nSeed #" + str(seed) + " (" + str(SIZE[0]) + "x" + str(SIZE[1]) + ")")
    # prints the seed (for reference) and the lab size
    print("_" * (SIZE[0] * 2))
    for j in range(SIZE[1]):
        if j != START[0]:
            print("|", end='')
        else:
            print("_", end='')
        for i in range(SIZE[0]):
            if maze[j][i] & S != 0:
                print(" ", end='')
            else:
                print("_", end='')
            if maze[j][i] & E != 0:
                if (maze[j][i] | maze[j][i + 1]) & S != 0:
                    print(" ", end='')
                else:
                    print("_", end='')
            elif (j == END[0]) & (i == END[1]):
                print("_", end='')
            else:
                print("|", end='')
        print("")


def isSafe(maze_matrix, target_x, target_y):
    pass

# if __name__ == "__main__":
#     seed = random.randint(0, 1000)
#     random.seed(seed)
#     dig(SIZE[0] // 2, SIZE[1] // 2)
#     draw()
#     print('\n')
#     check()
