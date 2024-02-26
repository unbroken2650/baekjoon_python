import sys

input = sys.stdin.readline

N = int(input())
for i in sorted(sorted(set(input().rstrip() for _ in range(N))), key=len):
  print(i)
