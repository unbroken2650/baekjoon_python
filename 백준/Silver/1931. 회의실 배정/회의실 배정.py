N = int(input())

last = 0
cnt = 0
times = []

for _ in range(N):
    start, end = map(int, input().split())
    times.append(list([start, end]))
times.sort(key=lambda x: (x[1], x[0]))

for time in times:
    if last <= time[0]:
        last = time[1]
        cnt += 1
print(cnt)
