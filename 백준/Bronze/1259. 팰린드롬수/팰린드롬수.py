import sys

input = sys.stdin.readline

while True:
    sent = str(int(input().rstrip()))
    if sent == '0':
        break
    while True:
        if len(sent) <= 1:
            print('yes')
            break
        elif sent[0] != sent[-1]:
            print('no')
            break
        else:
            sent = sent[1:-1]
