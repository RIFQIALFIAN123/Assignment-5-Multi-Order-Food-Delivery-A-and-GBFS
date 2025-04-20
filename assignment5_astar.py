import heapq
import time

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

def a_star_single(grid, start, goal):
    open_set = []
    heapq.heappush(open_set, (0 + manhattan(start, goal), 0, start, [start]))
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        if current == goal:
            return path, g, len(visited)
        if current in visited:
            continue
        visited.add(current)
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            ni, nj = current[0]+dx, current[1]+dy
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                if grid[ni][nj] != '#' and (ni, nj) not in visited:
                    new_g = g + 1
                    heapq.heappush(open_set, (new_g + manhattan((ni,nj), goal), new_g, (ni,nj), path + [(ni,nj)]))
    return [], float('inf'), len(visited)

def a_star_multi_delivery(grid):
    start = find_all(grid, 'R')[0]
    customers = find_all(grid, 'C')
    total_path = []
    total_cost = 0
    total_visited = 0

    current = start
    for customer in customers:
        path, cost, visited = a_star_single(grid, current, customer)
        if not path:
            continue
        total_path.extend(path[1:])  # skip repeat node
        total_cost += cost
        total_visited += visited
        current = customer

    return total_path, total_cost, total_visited

# Eksekusi
start_time = time.time()
path, cost, nodes = a_star_multi_delivery(grid5)
time_taken = (time.time() - start_time) * 1000

# Output
print("A* Multi-Delivery Path:", path)
print("Total cost (steps):", cost)
print("Execution time (ms):", round(time_taken, 2))
print("Visited nodes:", nodes)
