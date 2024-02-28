import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

nums = deque()
result = []
for i in range(1, N + 1):
    nums.append(i)

while True:
    if len(nums) == 1:
        result.append(nums.popleft())
        break
    for _ in range(K - 1):
        nums.append(nums.popleft())
    result.append(nums.popleft())

print("<" + ', '.join(map(str, result)) + ">")
