# deque 구조를 불러온다.
from collections import deque

# N 크기 입력
N = int(input("N 입력: "))

myQueue = deque()

for i in range(1, N+1):
    myQueue.append(i)

while len(myQueue) > 1:                 # 카드가 한 장 남을 때까지 반복
    myQueue.popleft()                   # 맨 위의 카드를 버린다
    myQueue.append(myQueue.popleft())   # 맨 위의 카드를 가장 아래 카드 밑으로 이동

print(myQueue[0])                       # 마지막으로 남은 카드 출력