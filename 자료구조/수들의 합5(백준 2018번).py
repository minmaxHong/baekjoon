import sys
input = sys.stdin.readline

N = int(input())

start_index, end_index = 1, 1
result = 1
sum = 1

while end_index != N:
    if sum == N:
        end_index += 1
        result += 1
        sum += end_index
    elif sum > N:
        sum -= start_index
        start_index += 1
    elif sum < N:
        end_index += 1
        sum += end_index

print(result)