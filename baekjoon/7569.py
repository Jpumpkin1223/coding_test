import sys

m, n, h = map(int, sys.stdin.readline().rstrip().split())
graph = [[list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)] for _ in range(h)]
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
# checked로 구분하고 다 이루어진 다음에 graph에 0이 남아 있으면 -1 리턴

stack_unit = []
for i in range(m):
    for j in range(n):
        for k in range(h):
            if graph[k][j][i] == 1:
                stack_unit.append((i, j, k))

count = 0
stack = [stack_unit]
while stack:
    unit_list: list = stack.pop()
    next_unit_list = []
    for cx, cy, cz in unit_list:
        for i in range(6):
            nx, ny, nz = cx + dx[i], cy + dy[i], cz + dz[i]
            if graph[cz][cy][cx] == 1:
                if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and graph[nz][ny][nx] == 0:
                    graph[nz][ny][nx] = 1
                    next_unit_list.append((nx, ny, nz))
    if next_unit_list:
        stack.append(next_unit_list)
        count += 1

is_finish = True
for i in range(m):
    for j in range(n):
        for k in range(h):
            if graph[k][j][i] == 0:
                is_finish = False

print(count if is_finish else -1)
