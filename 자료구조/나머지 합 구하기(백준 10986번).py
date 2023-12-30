import sys
input = sys.stdin.readline

N, M = map(int, input().split())
C = [0] * (M)
sum = 0

A = [0] + list(map(int, input().split()))
S = [0] * (N + 1)

reminder = 0

for i in range(1, len(A)):
    S[i] = (A[i] + S[i - 1]) % M
    reminder = S[i]
    if reminder == 0:
        sum += 1
    C[reminder] += 1

for i in range(M):
    if C[i] > 0:
        sum += ((C[i] * (C[i] - 1)) // 2)
print(sum)