import sys

input = sys.stdin.readline

nums = []

for i in range(666, 2700000):
  if str(i).count("666"):
    nums.append(i)

print(nums[int(input().rstrip()) - 1])
