'''
5개짜리 빈 큐를 생성하는 코드 (1)
queue = [None, None, None, None, None]

5개짜리 빈 큐를 생성하는 코드 (2)
SIZE = 5 # 큐 크기
queue = [None for _ in range(SIZE)]
front = rear = -1
'''

def isQueueFull():
    global SIZE, queue, front, rear
    if (rear == SIZE - 1):
        return True
    else:
        return False
SIZE = 5
queue = ["화사", "솔라", "문별", "휘인", "선미"]
front = -1
rear = 4

print("큐가 꽉 찼는지 여부 ==> ", isQueueFull())
