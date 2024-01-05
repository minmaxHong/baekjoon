import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

myQueue = deque()

for i in range(1, N + 1):
    myQueue.append(i)

while len(myQueue) != 1:
    myQueue.popleft()
    front = myQueue.popleft()
    
    myQueue.append(front)
print(myQueue[0])
    
