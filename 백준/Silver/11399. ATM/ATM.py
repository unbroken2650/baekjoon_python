N = int(input())
numbers = sorted(list(map(int, input().split())))

print(sum([sum(numbers[:i]) for i in range(1, N + 1)]))
