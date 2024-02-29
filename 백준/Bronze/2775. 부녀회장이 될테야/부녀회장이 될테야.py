T = int(input())

people = [[0 for i in range(14)] for i in range(15)]
for i in range(14):
  people[0][i] = i + 1
for i in range(1, 15):
  for j in range(14):
    people[i][j] = sum(people[i - 1][:j + 1])

for _ in range(T):
  n = int(input())
  k = int(input())
  print(people[n][k - 1])
