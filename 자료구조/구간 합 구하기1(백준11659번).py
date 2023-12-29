import sys
input = sys.stdin.readline

A_index, data_num = map(int, input().split())

A = [0] + list(map(int, input().split()))
S = [0] * (A_index + 1)

for i in range(1, len(A)) :
    S[i] = S[i - 1] + A[i]

for _ in range(data_num):
    a, b = map(int, input().split())
    print(S[b] - S[a - 1])