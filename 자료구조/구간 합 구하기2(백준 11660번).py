import sys
input = sys.stdin.readline

N, num = map(int, input().split())

A = [[0] * (N + 1)]
S = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(N):
    val = [0] + list(map(int, input().split()))
    A.append(val)

for y in range(1, N + 1):
    for x in range(1, N + 1):
        S[y][x] = -S[y - 1][x - 1] + S[y - 1][x] + S[y][x - 1] + A[y][x]

for _ in range(num):
    x1, y1, x2, y2 = map(int, input().split())
    print(S[x2][y2] - S[x1 - 1][y2] - S[x2][y1 - 1] + S[x1 - 1][y1 - 1])