N, M, B = map(int, input().split())

blocks = []
for _ in range(N):
  blocks.extend(map(int, input().split()))

time = [0 for _ in range(257)]
max_height = 0

for target in range(257):
  inv_blocks = B

  for j in blocks:
    if j <= target:
      time[target] += target - j
      inv_blocks -= target - j
    else:
      time[target] += 2 * (j - target)
      inv_blocks += j - target

  if inv_blocks >= 0 and time[target] <= time[max_height]:
    max_height = target

print(time[max_height], max_height)
