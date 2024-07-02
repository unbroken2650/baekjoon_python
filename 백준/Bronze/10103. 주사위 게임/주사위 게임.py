N = int(input())
scores = [100, 100]
dices = []
for _ in range(N):
    dices.append(list(map(int, input().split())))

for a, b in dices:
    if a > b:
        scores[1] -= a
    elif a < b:
        scores[0] -= b

for score in scores:
    print(score)
