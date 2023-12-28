arr_num = int(input())
arr = []

for _ in range(arr_num):
    num = int(input())
    arr.append(num)

arr.sort()

for i in range(len(arr)):
    print(arr[i])