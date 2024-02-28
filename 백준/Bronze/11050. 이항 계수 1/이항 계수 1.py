N, K = map(int, input().split())

answer = 1
for i in range(N, N - K, -1):
    answer = answer * i
for i in range(1, K + 1):
    answer = answer // i
print(answer)
