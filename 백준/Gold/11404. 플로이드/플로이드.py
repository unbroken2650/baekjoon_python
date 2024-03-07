INF = int(1e9)

N = int(input())
M = int(input())
graph = [[INF] * (N + 1) for _ in range(N + 1)]

# 출발지와 도착지가 같은 경우 거리는 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            graph[i][j] = 0

# 입력
for _ in range(M):
    a, b, c = map(int, input().split())
    if c < graph[a][b]:
        graph[a][b] = c

# 플로이드-워셜 알고리즘
for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
