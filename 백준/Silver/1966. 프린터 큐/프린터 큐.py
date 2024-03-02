from collections import deque

T = int(input())

for _ in range(T):
  N, M = map(int, input().split())
  prios = list(map(int, input().split()))

  result = 1
  while prios:
    if prios[0] < max(prios):
      prios.append(prios.pop(0))

    else:
      if M == 0: break

      prios.pop(0)
      result += 1

    M = M - 1 if M > 0 else len(prios) - 1

  print(result)
