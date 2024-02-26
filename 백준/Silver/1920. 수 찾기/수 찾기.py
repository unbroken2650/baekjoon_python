import sys

input = sys.stdin.readline

N = int(input().rstrip())
nums = set(map(int, input().rstrip().split(" ")))
M = int(input().rstrip())
targets = list(map(int, input().rstrip().split(" ")))

for target in targets:
  print(1 if target in nums else 0)
