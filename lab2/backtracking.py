import maze

maze_matrix = maze.maze
solution_matrix = [[]]


# solve the problem using backtracking
def backtracking_solution():
    global solution_matrix
    solution_matrix = [[0 for j in range(maze.SIZE[0])] for i in range(maze.SIZE[1])]

    if not find_path(0, 0):
        print("No solution found for solving the maze.")
        return False

    print('\nBacktracking solution: ')
    maze.print_solution_matrix(solution_matrix)
    return True


# check if direction is available and cell has not been visited before
def is_direction_safe(direction, x, y):
    if maze_matrix[x][y] & direction:

        if direction == maze.N:
            x -= 1
        elif direction == maze.S:
            x += 1
        elif direction == maze.E:
            y += 1
        elif direction == maze.W:
            y -= 1

        return solution_matrix[x][y] == 0
    return False


def find_path(x, y):
    if x == maze.SIZE[0] - 1 and y == maze.SIZE[1] - 1:
        solution_matrix[x][y] = 'X'
        return True

    if 0 <= x < maze.SIZE[0] and 0 <= y < maze.SIZE[1]:

        # check if EAST is safe
        if is_direction_safe(maze.E, x, y):
            solution_matrix[x][y] = '→'
            if find_path(x, y + 1):
                return True

        # check if NORTH is safe
        if is_direction_safe(maze.N, x, y):
            solution_matrix[x][y] = '↑'
            if find_path(x - 1, y):
                return True

        # check if WEST is safe
        if is_direction_safe(maze.W, x, y):
            solution_matrix[x][y] = '←'
            if find_path(x, y - 1):
                return True

        # check if SOUTH is safe
        if is_direction_safe(maze.S, x, y):
            solution_matrix[x][y] = '↓'
            if find_path(x + 1, y):
                return True
        solution_matrix[x][y] = 0
        return False


maze.dig(maze.SIZE[0] // 2, maze.SIZE[1] // 2)
maze.draw()
# maze.check()
backtracking_solution()
