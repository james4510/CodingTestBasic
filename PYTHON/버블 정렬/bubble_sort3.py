def bubbleSort(ary):
    n = len(ary)
    for end in range(n-1, 0, -1):
        changeYN = False

        for tmp in range(0, end):
            ary[tmp], ary[tmp+1] = ary[tmp+1], ary[tmp]
            changeYN = True
        if not changeYN:
            break
    return ary

# 변수 입력 부분
N = int(input("입력할 숫자의 개수를 입력하세요: "))
A = [0]*N

for i in range(N):
    A[i] = int(input("숫자 입력: "))

print('정렬 전 --> ',  A)
A = bubbleSort(A)
print('정렬 후 --> ', A)