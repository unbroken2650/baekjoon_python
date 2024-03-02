N = int(input())
sent = input()

total = 0
for i in range(N):
  tmp = ord(sent[i]) - 96
  for _ in range(i):
    tmp *= 31
  total += tmp
print(total % 1234567891)
