number = input()

total = [0] * 2
for i in number[:len(number) // 2]:
  total[0] += int(i)
for i in number[len(number) // 2:]:
  total[1] += int(i)

print("LUCKY") if total[0] == total[1] else print("READY")
