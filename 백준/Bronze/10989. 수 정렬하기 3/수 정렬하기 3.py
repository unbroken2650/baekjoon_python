nums = [0] * 10001

for i in range(int(input())):
  nums[int(input())] += 1
for i in range(10001):
  if nums[i]:
    for _ in range(nums[i]):
      print(i)
