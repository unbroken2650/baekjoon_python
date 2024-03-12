from collections import deque

M, N = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

matrix = [list(map(int, input().split())) for _ in range(N)]
queue = deque([])
ans = 0


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])


for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            queue.append([i, j])

bfs()

for i in matrix:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(i))

print(ans - 1)
