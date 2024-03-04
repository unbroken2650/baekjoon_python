data = [1]

for i in range(1, 30):
  data.append(data[i - 1] * i)
for _ in range(int(input())):
  a, b = map(int, input().split())
  print(data[b] // (data[a] * data[b - a]))
