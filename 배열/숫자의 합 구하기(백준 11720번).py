n = input()
numbers = list(input())

sum = 0

for i in range(len(numbers)):
    sum += int(numbers[i])
print(sum)