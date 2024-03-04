sums = [0, 1, 2, 4]

for i in range(4, 12):
  sums.append(sum(sums[i - 3:i]))

for _ in range(int(input())):
  print(sums[int(input())])
