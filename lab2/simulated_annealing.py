import random

import maze


def heuristic(x, y):
    return -(((maze.END[0] - x) ** 2 + (maze.END[1] - y) ** 2) ** (1 / 2))


maze_matrix = maze.maze
INITIAL_SCORE = abs(heuristic(maze.SIZE[0] // 2, maze.SIZE[1] // 2)) * 2
solution_matrix = [[]]
path = [maze.START]
heuristic_matrix = maze_matrix.copy()
for index, line in enumerate(heuristic_matrix):
    heuristic_matrix[index] = line.copy()

score = INITIAL_SCORE
took_wrong_turn = False
last_choice = (-1, -1)

x, y = maze.START


def simulated_annealing_solution():
    global took_wrong_turn
    global score
    global last_choice
    print()
    print(f'last_choice = {last_choice}')
    print(f'path = {path}')
    x, y = path[-1]
    print(f'score={score}')
    # destination point
    if (x, y) == maze.END:
        print(f'found solution: {path}')
        return
    if took_wrong_turn:
        score -= abs(heuristic(*path[-2]) - heuristic(*path[-1]))
    if score <= 0:
        print('before')
        maze.check()
        maze_matrix[last_choice[0]][last_choice[1]] -= get_direction_from_move(last_choice,
                                                                               path[path.index(last_choice) + 1])
        print('after')
        maze.check()
        path[path.index(last_choice) + 1:] = []
        x, y = last_choice
        last_choice = (-1, -1)
        took_wrong_turn = False
        score = INITIAL_SCORE
    available_directions = get_available_worthy_directions(x, y)
    print(f'get_available_worthy_directions: {available_directions}')
    if available_directions:
        # pick direction in random order
        direction = random.choice(available_directions)
        path.append(calculate_direction(direction, x, y))
    else:
        available_directions = get_all_available_directions(x, y)
        print(f'get_all_available_directions: {available_directions}')
        if not available_directions:
            print('No solution found')
            return
        took_wrong_turn = True
        if last_choice == (-1, -1):
            last_choice = (x, y)
        direction = random.choice(available_directions)
        path.append(calculate_direction(direction, x, y))
    print()
    simulated_annealing_solution()


def is_direction_worthy(direction, x, y):
    return heuristic(x, y) <= heuristic(*calculate_direction(direction, x, y))


def get_available_worthy_directions(x, y):
    available_directions = []
    for direction in [maze.N, maze.S, maze.E, maze.W]:
        if len(path) > 1 and path[-2] == calculate_direction(direction, x, y):
            continue
        if maze_matrix[x][y] & direction and is_direction_worthy(direction, x, y):
            available_directions.append(direction)
    return available_directions


def get_all_available_directions(x, y):
    available_directions = []
    for direction in [maze.N, maze.S, maze.E, maze.W]:
        if len(path) > 1 and path[-2] == calculate_direction(direction, x, y):
            continue
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


def get_direction_from_move(t1, t2):
    t3 = (t2[0] - t1[0], t2[1] - t1[1])
    if t3 == (0, 1):
        return maze.E
    elif t3 == (0, -1):
        return maze.W
    elif t3 == (1, 0):
        return maze.S
    elif t3 == (-1, 0):
        return maze.N


maze.dig(maze.SIZE[0] // 2, maze.SIZE[1] // 2)
maze.draw()
print_heuristic_matrix()
# maze.check()
simulated_annealing_solution()
