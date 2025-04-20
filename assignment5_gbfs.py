import heapq
import time

# Grid yang sama seperti A*
grid5 = [
    ['R', '.', '.', '.', '#', '.', '.', '.', '.', 'C'],
    ['.', '#', '#', '.', '#', '.', '#', '#', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
    ['.', '#', '#', '#', '#', '.', '#', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '#', '.', 'C', '.']
]

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def find_all(grid, symbol):
    return [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == symbol]

def gbfs_single(grid, start, goal):
    open_set = []
    heapq.heappush(open_set, (manhattan(start, goal), start, [start]))
    visited = set()

    while open_set:
        h, current, path = heapq.heappop(open_set)
        if current == goal:
            return path, len(visited)
        if current in visited:
            continue
        visited.add(current)
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            ni, nj = current[0] + dx, current[1] + dy
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                if grid[ni][nj] != '#' and (ni, nj) not in visited:
                    heapq.heappush(open_set, (manhattan((ni, nj), goal), (ni, nj), path + [(ni, nj)]))
    return [], len(visited)

def gbfs_multi_delivery(grid):
    start = find_all(grid, 'R')[0]
    customers = find_all(grid, 'C')
    total_path = []
    total_visited = 0
    current = start

    for customer in customers:
        path, visited = gbfs_single(grid, current, customer)
        if not path:
            continue
        total_path.extend(path[1:])  # skip repeat node
        total_visited += visited
        current = customer

    return total_path, total_visited

# Eksekusi
start_time = time.time()
path, nodes = gbfs_multi_delivery(grid5)
time_taken = (time.time() - start_time) * 1000

# Output
print("GBFS Multi-Delivery Path:", path)
print("Execution time (ms):", round(time_taken, 2))
print("Visited nodes:", nodes)
