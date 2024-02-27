import sys

input = sys.stdin.readline

N = int(input().rstrip())
coords = []
for _ in range(N):
    x, y = map(int, input().rstrip().split())
    coords.append([x, y])
coords.sort(key=lambda x: (x[0], x[1]))
for i in coords:
    print(i[0], i[1])
