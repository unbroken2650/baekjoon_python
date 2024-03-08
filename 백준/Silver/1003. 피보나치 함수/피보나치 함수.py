T = int(input())

result = [[1, 0], [0, 1], [1, 1]]
for i in range(2, 41):
    result.append([result[i][0] + result[i - 1][0], result[i][1] + result[i - 1][1]])
for _ in range(T):
    print(*result[int(input())])
