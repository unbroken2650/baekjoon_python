T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = [(x, y)]
    matrix[x][y] = 0
    while queue:
        x, y = queue.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if matrix[nx][ny]:
                queue.append((nx, ny))
                matrix[nx][ny] = 0


for _ in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0] * (N) for _ in range(M)]
    cnt = 0
    for _ in range(K):
        x, y = map(int, input().split())
        matrix[x][y] = 1

    for i in range(M):
        for j in range(N):
            if matrix[i][j]:
                bfs(i, j)
                cnt += 1

    print(cnt)
