import random
from collections import deque
import time

import maze

maze_matrix = maze.maze
solution_matrix = [[]]
deq = deque()


# the deque holds paths
# a path is a list which contains tuples (x0, y0), (x1, y1) ... (xk, yk)
# xi is the line index and yi is the column index
def bfs_solution():
    while len(deq) > 0:
        path = deq.pop()
        x, y = path[-1]  # get last tuple

        # destination point
        if x == maze.END[0] and y == maze.END[1]:
            print(f'found solution: {path}')
            return

        available_directions = get_available_directions(x, y)
        # pick direction in random order
        while len(available_directions) != 0:
            direction = random.choice(available_directions)
            available_directions.remove(direction)

            if is_direction_safe(direction, path, x, y):
                p = path.copy()
                p.append(calculate_direction(direction, x, y))
                deq.appendleft(p)

    print('No solution found.')


# prevent oscillation
def is_direction_safe(direction, path, x, y):
    if len(path) > 1 and path[-2] == calculate_direction(direction, x, y):
        return False
    return True


def get_available_directions(x, y):
    available_directions = []
    for direction in [maze.N, maze.S, maze.E, maze.W]:
        if maze_matrix[x][y] & direction:
            available_directions.append(direction)
    return available_directions


def calculate_direction(direction, x, y):
    if direction == maze.N:
        x -= 1
    elif direction == maze.S:
        x += 1
    elif direction == maze.E:
        y += 1
    elif direction == maze.W:
        y -= 1

    return x, y


maze.dig(maze.SIZE[0] // 2, maze.SIZE[1] // 2)
maze.draw()
maze.check()
deq.append([maze.START])
bfs_solution()
