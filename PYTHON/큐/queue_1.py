'''
큐 원리
- 큐에 데이터를 삽입하는 작동: enQueue()
- 데이터를 추출하는 작동: deQueue()
- 저장된 데이터 중 첫번째 데이터: front
- 저장된 데이터 중 마지막 데이터: rear
'''

queue = ["화사", "솔라", "문별", None, None]
front = -1
rear = 2

print("----- 큐 상태 -----")
print("[출구] <-- ", end=' ')
for i in range(0, len(queue), 1):
    print(queue[i], end=' ')
print('<-- [입구]')
print("---------------------")

front += 1
data = queue[front]
queue[front] = None
print('deQueue --> ', data)
print("========================")

print('----- 큐 상태 -----')
print('[출구] --> ', end=' ')
for i in range(0, len(queue), 1):
    print(queue[i], end=' ')
print('<-- [입구]')

front += 1
data = queue[front]
queue[front] = None
print('deQueue --> ', data)
print("========================")

print('----- 큐 상태 -----')
print('[출구] --> ', end=' ')
for i in range(0, len(queue), 1):
    print(queue[i], end=' ')
print('<-- [입구]')

front += 1
data = queue[front]
queue[front] = None
print('deQueue --> ', data)
print("========================")

print('----- 큐 상태 -----')
print('[출구] --> ', end=' ')
for i in range(0, len(queue), 1):
    print(queue[i], end=' ')
print('<-- [입구]')