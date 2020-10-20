import random

import maze

maze_matrix = maze.maze
solution_matrix = [[]]
heuristic_matrix = maze_matrix.copy()
path = [maze.START]
score = 4
last_choice = (-1, -1)

x, y = maze.START


def simulated_annealing_solution():
    x, y = path[-1]
    # destination point
    if (x, y) == maze.END:
        print(f'found solution: {path}')
        return
    available_directions = get_available_worthy_directions(x, y)
    if available_directions:
        # pick direction in random order
        direction = random.choice(available_directions)
        path.append(calculate_direction(direction, x, y))
        simulated_annealing_solution()
    else:
        global last_choice
        if last_choice != (-1, -1):
            last_choice = (x, y)
        available_directions = get_all_available_directions(x, y)
        direction = random.choice(available_directions)
        path.append(calculate_direction(direction, x, y))
        global score
        score -= 1
        # if score == 0:
        #     path[]
        simulated_annealing_solution()


def is_direction_worthy(direction, x, y):
    return heuristic(x, y) <= heuristic(*calculate_direction(direction, x, y))


def heuristic(x, y):
    return -(abs(maze.END[0] - x) + abs(maze.END[1] - y))


def get_available_worthy_directions(x, y):
    available_directions = []
    for direction in [maze.N, maze.S, maze.E, maze.W]:
        if maze_matrix[x][y] & direction and is_direction_worthy(direction, x, y):
            available_directions.append(direction)
    return available_directions


def get_all_available_directions(x, y):
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


def print_heuristic_matrix():
    for i, line in enumerate(heuristic_matrix):
        for j, _ in enumerate(line):
            heuristic_matrix[i][j] = heuristic(i, j)
            print(f' {heuristic_matrix[i][j]} ', end='')
        print()


def get_direction_from_move():
    pass

maze.dig(maze.SIZE[0] // 2, maze.SIZE[1] // 2)
maze.draw()
# maze.check()
simulated_annealing_solution()
# print_heuristic_matrix()
