import sys

input = sys.stdin.readline

N = int(input().rstrip())
nums = list(map(int, input().rstrip().split(" ")))
M = int(input().rstrip())
targets = list(map(int, input().rstrip().split(" ")))

mapList = [0 for _ in range(-10000000, 10000001, 1)]

for i in nums:
  mapList[i] += 1

for target in targets:
  print(mapList[target], end=" ")
