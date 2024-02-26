import sys

input = sys.stdin.readline

inp = input().rstrip()

cnt = [0, 0]

before = inp[0]
cnt[int(before)] += 1

for i in range(1, len(inp)):
  if before != inp[i]:
    cnt[int(inp[i])] += 1
  before = inp[i]
print(min(cnt))
