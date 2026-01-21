from collections import deque
import sys


def solve_fossil():
    input = sys.stdin.read
    data = input().split()

    idx = 0
    R = int(data[idx]);
    idx += 1
    C = int(data[idx]);
    idx += 1
    A_min = int(data[idx]);
    idx += 1
    K = int(data[idx]);
    idx += 1

    grid = []
    start = None
    goal = None
    for r in range(R):
        row = data[idx]
        idx += 1
        grid.append(list(row))
        for c in range(C):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'F':
                goal = (r, c)

    if not start or not goal:
        print("Фосилът се оказа просто камък...")
        return

    directions = [(1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R'), (-1, 0, 'U')]


    queue = deque([(start[0], start[1], 0, 0, "")])
    visited = set()
    visited.add((start[0], start[1], 0, 0))

    best_path = None
    best_len = float('inf')
    best_age = 0

    while queue:
        r, c, age, used_T, path = queue.popleft()
        steps = len(path)


        if steps >= best_len:
            continue


        cell = grid[r][c]
        new_age = age
        new_used_T = used_T

        if cell.isdigit():
            new_age += int(cell)
        elif cell == 'T':
            new_age *= 2
            new_used_T += 1
            if new_used_T > K:
                continue


        if (r, c) == goal and new_age >= A_min:
            if steps < best_len or (steps == best_len and (best_path is None or path < best_path)):
                best_len = steps
                best_age = new_age
                best_path = path
            continue


        for dr, dc, d in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#':
                state = (nr, nc, new_age, new_used_T)
                if state not in visited:
                    visited.add(state)
                    queue.append((nr, nc, new_age, new_used_T, path + d))

    if best_path is not None:
        print(best_len)
        print(best_age)
        print(best_path)
        print("Открихме истински ФОСИЛ!")
    else:
        print("Фосилът се оказа просто камък...")



solve_fossil()


