'''
이진 탐색(Binary search)
- 데이터가 정렬되어 있는 상태에서 원하는 값을 찾아내는 알고리즘이다.
- 대상 데이터의 중앙값과 찾고자 하는 값을 비교해 데이터의 크기를 절반씩 줄이면서 대상을 찾는다.
- 정렬 데이터에서 원하는 데이터를 탐색할 때 사용하는 가장 일반적인 알고리즘이다.

이진 탐색 과정
1. 현재 데이터셋의 중앙값(median)을 선택한다.
2. 중앙값 > 타겟 데이터 일 때, 중앙값 기준으로 왼쪽 데이터셋을 선택한다.
3. 중앙값 < 타겟 데이터 일 때, 중앙값 기준으로 오른쪽 데이터셋을 선택한다.
4. 과정 1~3을 반복하다가 중앙값 == 타겟 데이터일 때 탐색을
'''

N, M = map(int, input().split())
A = list(map(int, input().split()))
start = 0
end = 0

for i in A:
    if start < i:
        start = i   # 레슨 최댓값을 시작 인덱스로 저장
    end += i        # 모든 레슨의 총합을 종료 인덱스로 저장

while start <= end:
    middle = int((start + end) / 2)
    sum = 0
    count = 0

    for i in range(N):  # 중간값으로 모든 레슨을 저장할 수 있는지 확인
        if sum + A[i] > middle:
            count += 1
            sum = 0
        sum += A[i]
    if sum != 0:
        count += 1
    if count > M:
        start = middle + 1
    else:
        end = middle - 1

print(start)