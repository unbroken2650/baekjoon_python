import sys

input = sys.stdin.readline

N = int(input().rstrip())
people = []
for _ in range(N):
    x, y = input().rstrip().split()
    people.append([int(x), y])
people.sort(key=lambda x: (x[0]))
for i in people:
    print(i[0], i[1])
