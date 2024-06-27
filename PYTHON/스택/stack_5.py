'''
문제[011] 스택으로 수열 만들기
- 1부터 n까지의 수를 스택에 저장하고 출력하는 방식으로 하나의 수열을 만들 수 있다. 이때, 스택에 push 하는 순서는 반드시 오름차순을 지키도록 한다고 가정한다.
수열이 주어졌을 때 이러한 방식으로 스택을 이용해 주어진 수열을 만들 수 있는지 확인하고 만들 수 있다면 어떤 순서로 push 와 pop을 수행하여야 하는지 확인하는 프로그램을 작성해 보자.

입력
- 1번째 줄에 수열의 개수가 주어진다. 2번째 줄에서 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 1개씩 순서대로 주어진다. 이때, 같은 정수는 2번 이상 나오지 않는다.

출력
- 수열을 만들기 위한 연산 순서를 출력한다. push 연산은 +, pop 연산은 -로 출력하고, 불가능할 때에는 NO를 출력한다.
'''
N = int(input("N 입력: "))
A = [0]*N

for i in range(N):
    A[i] = int(input())

stack = []
num = 1
result = True
answer = ""

for i in range(N):
    su = A[i]
    if su >= num:   # 현재 수열 값 >= 오름차순 자연수: 값이 같아질 때까지 append() 수행
        while su >= num:
            stack.append(num)
            num += 1
            answer += "+\n"
        stack.pop()
        answer += "-\n"
    else:   # 현재 수열 값 < 오름차순 자연수 : pop() 을 수행해 수열 원소를 꺼냄
        n = stack.pop()
        # 스택의 가장 ㅜ이의 수가 만들어야 하는 수열의 수보다 크면 수열을 출력할 수 없음
        if n > su:
            print("N0")
            result = False
            break
        else:
            answer += "-\n"
if result:
    print(answer)