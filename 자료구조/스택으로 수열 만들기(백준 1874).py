import sys
input = sys.stdin.readline

stack_length = int(input())
stack = []
sign = []
n = 0
flag = True

for i in range(stack_length):
    stack_num = int(input())
    
    if stack_num >= n:
        while True:
            n += 1
            if stack_num == n:
                stack.append(n)
                sign.append("+")
                stack.pop()
                sign.append("-")
                break
            stack.append(n)
            sign.append("+")
    else:
        top = stack.pop()
        if top < stack_num:
            print("NO")
            flag = False
            break

        sign.append("-")

if flag == True:
    for i in range(len(sign)):
        print(sign[i])
    
