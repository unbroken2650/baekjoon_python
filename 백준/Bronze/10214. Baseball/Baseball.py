N = int(input())
for _ in range(N):
    y, k = 0, 0
    for _ in range(9):
        a, b = map(int, input().split())
        y += a
        k += b
    if y > k:
        print("Yonsei")
    elif y < k:
        print("Korea")
    else:
        print("Draw")
