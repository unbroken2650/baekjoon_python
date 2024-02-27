import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
boards = []
nums = []


def calculate_color(t1, t2, first, second):
    cnt = 0
    if t1 + 8 > N or t2 + 8 > M:
        return
    for j in range(t1, t1 + 8, 2):
        for k in range(t2, t2 + 8, 2):
            if boards[j][k] != first:
                cnt += 1
            if boards[j][k + 1] != second:
                cnt += 1

        for k in range(t2, t2 + 8, 2):
            if boards[j + 1][k] != second:
                cnt += 1
            if boards[j + 1][k + 1] != first:
                cnt += 1
    return cnt


for _ in range(N):
    boards.append(list(input().rstrip()))
for i in range(N - 7):
    for j in range(M - 7):
        nums.append(calculate_color(i, j, 'W', 'B'))
        nums.append(calculate_color(i, j, 'B', 'W'))

print(min(nums))
