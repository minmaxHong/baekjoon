import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

ingred = list(map(int, input().split()))
ingred.sort()

start, end, cnt = 0, len(ingred) - 1, 0


while start != end:
    S = ingred[start] + ingred[end]
    if S > M:
        end -= 1
    elif S == M:
        cnt += 1
        end -= 1
    elif S < M:
        start += 1

print(cnt)

