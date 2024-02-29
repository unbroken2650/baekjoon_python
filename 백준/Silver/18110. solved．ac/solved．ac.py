import sys
import math

input = sys.stdin.readline

N = int(input().rstrip())


def _round(num):
  tmp = num % 1 / 0.1
  return math.floor(num) if tmp < 5 else math.ceil(num)


if N == 0:
  print(0)
else:
  nums = sorted(int(input().rstrip()) for _ in range(N))

  percentage = _round(N * 0.15)

  nums = nums[percentage:N - percentage]
  print(_round(sum(nums) / len(nums)))
