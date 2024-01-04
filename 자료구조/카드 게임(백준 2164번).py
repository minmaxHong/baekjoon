import sys
from collections import deque
input = sys.stdin.readline

myQueue = deque()
N = int(input())

for i in range(1, N + 1):
    myQueue.append(i)

while len(myQueue) != 1:
    myQueue.popleft()
    n = myQueue.popleft()
    
    myQueue.append(n)
print(myQueue[0])
    