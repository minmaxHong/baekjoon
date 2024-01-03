# 9,8은 index 값
# CCTGGATTG는 문자
# 2 0 1 1은 맞아야하는 개수이다.

# A, C, G, T를 개수를 입력받는 변수와 그 변수의 개수를 확인하는 변수가 있어야한다.

import sys
input = sys.stdin.readline

all_length, sub_length = map(int, input().split())
DNAString = list(input())
verifiedWord = list(map(int, input().split()))

# checkEachList는 verifiedWord마다 각 자리보다 이상이여야하며,
# 만약 그 이상인 값을 가지면 check는 +1의 값을 가진다.
# 만약 check가 4가 된다면, result는 +1의 값을 가진다.
checkEachList = [0] * 4
check = 0
result = 0

def add(c): # c가 DNAString의 각 자리임
    global verifiedWord, checkEachList, check
    
    # verifiedWord값이 0일때는 무조건 check가 +1 값을 가지는 것을 유의
    if c == "A":
        checkEachList[0] += 1
        if checkEachList[0] == verifiedWord[0]:
            check += 1
    
    elif c == "C":
        checkEachList[1] += 1
        if checkEachList[1] == verifiedWord[1]:
            check += 1
    
    elif c == "G":
        checkEachList[2] += 1
        if checkEachList[2] == verifiedWord[2]:
            check += 1
    
    elif c == "T":
        checkEachList[3] += 1
        if checkEachList[3] == verifiedWord[3]:
            check += 1

def remove(c):
    global verifiedWord, checkEachList, check
    
    if c == "A":
        if checkEachList[0] == verifiedWord[0]:
            check -= 1
        checkEachList[0] -= 1
    
    elif c == "C":
        if checkEachList[1] == verifiedWord[1]:
            check -= 1
        checkEachList[1] -= 1
    
    elif c == "G":
        if checkEachList[2] == verifiedWord[2]:
            check -= 1
        checkEachList[2] -= 1
    
    elif c == "T":
        if checkEachList[3] == verifiedWord[3]:
            check -= 1
        checkEachList[3] -= 1


# 처음은 무조건 알아야함
for i in range(4):
    if verifiedWord[i] == 0:
        check += 1

for i in range(sub_length):
    add(DNAString[i])
    
if check == 4:
    result += 1

# 처음이 아닌 이제 이어나감
for i in range(sub_length, all_length):
    j = i - sub_length
    add(DNAString[i])
    remove(DNAString[j])
    
    if check == 4:
        result += 1

print(result)