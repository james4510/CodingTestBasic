# 스택 초기화
SIZE=5
stack=[None for _ in range(SIZE)]
top=-1

top += 1
stack[top] = "커피"
top += 1
stack[top] = "녹차"
top += 1
stack[top] = "꿀물"

print("===== 스택 상태 =====")
for i in range(len(stack)-1, -1, -1):
    print(stack[i])
