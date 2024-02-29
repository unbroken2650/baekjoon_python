K = int(input())

nums = []

for _ in range(K):
  num = int(input())
  if num == 0 and nums:
    nums.pop()
  else:
    nums.append(num)

print(sum(nums))
