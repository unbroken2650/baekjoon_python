N = int(input())

total = 0
count = [0] * 8001
numbers = list()

for _ in range(N):
  inp = int(input())
  total += inp
  count[inp + 4000] += 1
  numbers.append(inp)

numbers.sort()
print(round(total / N))
print(numbers[N // 2])

max_count = max(count)
max_candidates = [i - 4000 for i, v in enumerate(count) if v == max_count]
print(max_candidates[0] if len(max_candidates) == 1 else max_candidates[1])

print(max(numbers) - min(numbers))
