import sys
input = sys.stdin.readline

N = int(input())
arr = [0] * N

for i in range(N):
    arr[i] = int(input())

for y in range(N - 1):
    for x in range(y + 1, N):
        if arr[y] > arr[x]:
            temp = arr[y]
            arr[y] = arr[x]
            arr[x] = temp
            
for i in range(N):
    print(arr[i])