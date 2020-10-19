import maze

AVAILABLE_EAST = [4, 5, 6, 7, 12, 13, 14, 15]
AVAILABLE_NORTH = [1, 3, 5, 7, 9, 11, 13, 15]
AVAILABLE_WEST = [8, 9, 10, 11, 12, 13, 14, 15]
AVAILABLE_SOUTH = [2, 3, 6, 7, 10, 11, 14, 15]


# num => 2^3 / 2^2 / 2^1 / 2^0
# 14
# 6
# 2
# 0
# 1 0 1 1


def backtracking_solution(maze_matrix):
    solution_matrix = [[0 for j in range(maze.SIZE[0])] for i in range(maze.SIZE[1])]
    if find_path(maze_matrix, 0, 0, solution_matrix) is False:
        print("No solution found for solving the maze")
        return False
    print('\nBacktracking solution: ')
    maze.print_solution_matrix(solution_matrix)
    return True


def is_direction_safe(current_maze_cell, target_x, target_y, solution_matrix,
                      direction_number):  # check if direction is available and cell has not been visited before
    if current_maze_cell & direction_number and solution_matrix[target_x][target_y] == 0:
        return True
    return False


def find_path(maze_matrix, current_x, current_y, solution_matrix):
    if current_x == maze.SIZE[0] - 1 and current_y == maze.SIZE[1] - 1:
        solution_matrix[current_x][current_y] = 'X'
        return True

    if 0 <= current_x < maze.SIZE[0] and 0 <= current_y < maze.SIZE[1]:
        current_maze_cell = maze_matrix[current_x][current_y]

        if is_direction_safe(current_maze_cell, current_x, current_y + 1, solution_matrix,
                             maze.E):  # east is safe
            solution_matrix[current_x][current_y] = '→'
            if find_path(maze_matrix, current_x, current_y + 1, solution_matrix):
                return True

        if is_direction_safe(current_maze_cell, current_x - 1, current_y, solution_matrix,
                             maze.N):  # north is safe
            solution_matrix[current_x][current_y] = '↑'
            if find_path(maze_matrix, current_x - 1, current_y, solution_matrix):
                return True

        if maze_matrix[current_x][current_y] in AVAILABLE_WEST \
                and solution_matrix[current_x][current_y - 1] == 0:  # west is safe
            solution_matrix[current_x][current_y] = '←'
            if find_path(maze_matrix, current_x, current_y - 1, solution_matrix):
                return True

        if maze_matrix[current_x][current_y] in AVAILABLE_SOUTH \
                and solution_matrix[current_x + 1][current_y] == 0:  # south is safe
            solution_matrix[current_x][current_y] = '↓'
            if find_path(maze_matrix, current_x + 1, current_y, solution_matrix):
                return True
        solution_matrix[current_x][current_y] = 0
        return False


maze.dig(maze.SIZE[0] // 2, maze.SIZE[1] // 2)
maze.draw()
maze.check()
backtracking_solution(maze.maze)
