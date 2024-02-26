times = int(input())
for i in range(0, times):
  h, w, n = map(int, input().split())
  num = n // h + 1
  fl = n % h
  if fl == 0:
    fl = h
    num -= 1
  answer = fl * 100 + num
  print(answer)
