import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
cnt = 0

for i in range(len(arr)):
    find = arr[i]
    start, end = 0, len(arr) - 1

    while start < end:
        S = arr[start] + arr[end]
        if S == find:
            if start != i and end != i: # 서로 다른 두 수 이므로
                cnt += 1
                break
            elif start == i:
                start += 1
            elif end == i:
                end -= 1
        elif S > find:
            end -= 1
        elif S < find:
            start += 1

print(cnt)