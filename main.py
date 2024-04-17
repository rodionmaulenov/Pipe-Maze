def read_grid(input_text):
    grid = [list(line) for line in input_text.strip().split('\n')]
    return grid


connections = {
    '|': {'N', 'S'},
    '-': {'E', 'W'},
    'L': {'N', 'E'},
    'J': {'N', 'W'},
    '7': {'S', 'W'},
    'F': {'S', 'E'}
}


def find_start(grid):
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            if value == 'S':
                return (x, y)


def infer_type(grid, x, y):
    possible_types = {k: set(v) for k, v in connections.items()}
    for dx, dy, dir in [(0, -1, 'N'), (1, 0, 'E'), (0, 1, 'S'), (-1, 0, 'W')]:
        nx, ny = x + dx, y + dy
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] in connections:
            opposite_dir = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}[dir]
            if opposite_dir not in connections[grid[ny][nx]]:
                for k in list(possible_types.keys()):
                    if dir in possible_types[k]:
                        possible_types[k].remove(dir)
    for k, v in possible_types.items():
        if len(v) == 2:
            return k
    return '.'


def bfs(grid, start, connections):
    from collections import deque
    queue = deque([(start, 0)])
    visited = {start}
    max_distance = 0
    distances = {}

    x, y = start
    s_type = infer_type(grid, x, y)
    grid[y][x] = s_type

    while queue:
        (x, y), dist = queue.popleft()
        current_type = grid[y][x]
        directions = get_directions(current_type, connections)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) in visited or not is_valid(nx, ny, grid):
                continue
            visited.add((nx, ny))
            queue.append(((nx, ny), dist + 1))
            distances[(nx, ny)] = dist + 1
            max_distance = max(max_distance, dist + 1)
    return max_distance, distances


def get_directions(tile_type, connections):
    direction_map = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}
    return [direction_map[dir] for dir in connections.get(tile_type, [])]


def is_valid(x, y, grid):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)


def main(input_text):
    grid = read_grid(input_text)
    start = find_start(grid)
    max_distance, _ = bfs(grid, start, connections)
    print("Farthest distance from start:", max_distance)


input_text = """
-L|F7
7S-7|
L|7||
-L-J|
L|-JF
"""

main(input_text)
