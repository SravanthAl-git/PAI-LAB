import heapq

WIDTH, HEIGHT = 5, 3
start = (0, 0)
goal = (4, 2)
obstacles = {(1, 1), (2, 1)}

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance

def greedy(start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic(start, goal), start))
    parent = {}
    visited = set()

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]

        visited.add(current)
        x, y = current
        neighbors = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]

        for nx, ny in neighbors:
            neighbor = (nx, ny)
            if (0 <= nx < WIDTH and 0 <= ny < HEIGHT and
                neighbor not in obstacles and neighbor not in visited):
                
                heapq.heappush(open_list, (heuristic(neighbor, goal), neighbor))
                parent[neighbor] = current

    return None

print("Path:", greedy(start, goal))
