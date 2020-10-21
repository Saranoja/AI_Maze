import random
import maze

maze_matrix = maze.maze
solution_matrix = [[]]
path = [maze.START]
heuristic_matrix = maze_matrix.copy()
for index, line in enumerate(heuristic_matrix):
    heuristic_matrix[index] = line.copy()

x, y = maze.START


def hillclimbing_solution():
    x, y = path[-1]
    # destination point
    if (x, y) == maze.END:
        print(f'found solution: {path}')
        return
    available_directions = get_available_directions(x, y)
    if not available_directions:
        print('No worthy solution found')
        return
    # pick direction in random order
    direction = random.choice(available_directions)
    path.append(calculate_direction(direction, x, y))
    hillclimbing_solution()


def is_direction_worthy(direction, x, y):
    return heuristic(x, y) <= heuristic(*calculate_direction(direction, x, y))


def heuristic(x, y):
    return -(abs(maze.END[0] - x) + abs(maze.END[1] - y))


def get_available_directions(x, y):
    available_directions = []
    for direction in [maze.N, maze.S, maze.E, maze.W]:
        if maze_matrix[x][y] & direction and is_direction_worthy(direction, x, y):
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


maze.dig(maze.SIZE[0] // 2, maze.SIZE[1] // 2)
maze.draw()
print_heuristic_matrix()
maze.check()
hillclimbing_solution()
