import sys

input = sys.stdin.readline

N = int(input().rstrip())

methods = []
stack = []
loc = 1
availability = True

for i in range(N):
  num = int(input().rstrip())
  while loc <= num:
    stack.append(loc)
    methods.append("+")
    loc += 1

  if stack[-1] != num:
    availability = False
  else:
    stack.pop()
    methods.append("-")

if availability:
  for i in methods:
    print(i)
else:
  print("NO")
