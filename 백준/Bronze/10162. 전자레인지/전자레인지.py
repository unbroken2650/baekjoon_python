T = int(input())
buttons = [300, 60, 10]
answer = []
for button in buttons:
    answer.append(str(T // button))
    T %= button
if T:
    print(-1)
else:
    print(*answer)
