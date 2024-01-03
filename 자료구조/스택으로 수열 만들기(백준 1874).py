# 주의사항
# 1. push하는 순서는 오름차순(1,2,3,4 ~)
# 2. push 연산은 "+"
# 3. pop 연산은 "-"로 출력
# 4. 불가능할때는 "NO" 출력

import sys
input = sys.stdin.readline

num = int(input())
stack = []
n = 0
output = []

flag = True

for i in range(num):
    stack_num = int(input())
    
    if stack_num >= n:
        while True:
            n += 1
            stack.append(n)
            output.append("+")
            if stack_num == n:
                stack.pop()
                output.append("-")
                break
            
    else:
        top = stack.pop()
        
        if top < stack_num:
            print("NO")
            flag = False
            break
        else:
            output.append("-")

if flag:
    for i in range(len(output)):
        print(output[i])