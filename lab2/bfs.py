import random
from collections import deque

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
        # print(path)
        # time.sleep(.5)
        # print(path)
        # print(path[-1:][0])
        x, y = path[-1]  # get last tuple

        # destination point
        if x == maze.SIZE[0] - 1 and y == maze.SIZE[1] - 1:
            print(f'found solution: {path}')
            break

        available_directions = get_available_directions(x, y)

        # pick direction in random order
        while len(available_directions) != 0:
            new_path = path.copy()
            direction = random.choice(available_directions)
            available_directions.remove(direction)

            if direction == maze.N:
                if len(new_path) > 1 and new_path[-2] == (x - 1, y):
                    continue
                new_path.append((x - 1, y))
            elif direction == maze.S:
                if len(new_path) > 1 and new_path[-2] == (x + 1, y):
                    continue
                new_path.append((x + 1, y))
            elif direction == maze.E:
                if len(new_path) > 1 and new_path[-2] == (x, y + 1):
                    continue
                new_path.append((x, y + 1))
            elif direction == maze.W:
                if len(new_path) > 1 and new_path[-2] == (x, y - 1):
                    continue
                new_path.append((x, y - 1))

            deq.append(new_path)


# def is_direction_safe(direction, path, x, y):


def get_available_directions(x, y):
    available_directions = []
    for direction in [maze.N, maze.S, maze.E, maze.W]:
        if maze_matrix[x][y] & direction:
            available_directions.append(direction)
    return available_directions


maze.dig(maze.SIZE[0] // 2, maze.SIZE[1] // 2)
maze.draw()
maze.check()
deq.append([(0, 0)])
bfs_solution()
