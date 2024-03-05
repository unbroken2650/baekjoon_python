T = int(input())
coins = [25, 10, 5, 1]
for _ in range(T):
  N = int(input())
  for i in coins:
    print(N // i, end=" ")
    N -= (N // i) * i
  print("")
