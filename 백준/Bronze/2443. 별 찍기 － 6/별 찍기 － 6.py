N = int(input())
for i in range(N, 0, -1):
  print(" " * (N - i), end="")
  print("*" * (2 * i - 1), end="")
  if i != 1:
    print(" ")
