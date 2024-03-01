import sys

input = sys.stdin.readline

N = int(input())

people = []

for _ in range(N):
  x, y = map(int, input().rstrip().split())
  people.append([x, y, 1])

for i in range(N):
  for j in range(N):
    if i != j:
      if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
        people[i][2] += 1
for i in people:
  print(i[2], end=" ")
