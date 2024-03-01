import sys

input = sys.stdin.readline

while True:
  inp = input().rstrip()
  if inp == '.':
    break
  stack = []
  balanced = True
  for char in inp:
    if char in "([":
      stack.append(char)
    elif char in ")]":
      if not stack:
        balanced = False
        break
      elif char == ")" and stack[-1] == "(":
        stack.pop()
      elif char == "]" and stack[-1] == "[":
        stack.pop()
      else:
        balanced = False
        break
  if not stack and balanced:
    print("yes")
  else:
    print("no")
