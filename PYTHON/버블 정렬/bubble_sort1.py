'''
버블 정렬의 핵심 이론
- 버블 정렬은 두 인접한 데이터의 크기를 비교해 정렬하는 방법이다.
- 시간 복잡도는 O(n^2)으로 다른 정렬 알고리즘보다 속도가 느린 편이다.
- 간단하게 구현할 수 있다.
'''

# 클래스와 함수 선언 부분(1) - 오름차순
def bubbleSortUpper(ary):
    n = len(ary)
    for end in range(n-1, 0, -1):
        for cur in range(0, end):
            if(ary[cur] > ary[cur+1]):  # 오름차순 핵심 코드
                ary[cur], ary[cur+1] = ary[cur+1], ary[cur]
    return ary

# 클래스와 함수 선언 부분(2) - 내림차순
def bubbleSortLower(ary):
    n = len(ary)
    for end in range(n-1, 0, -1):
        for cur in range(0, end):
            if(ary[cur] < ary[cur+1]):  # 내림차순 핵심 코드
                ary[cur], ary[cur+1] = ary[cur+1], ary[cur]
    return ary

# 전역 변수 선언 부분
dataAry = [188, 162, 120, 50, 150, 177, 105]

# 메인 코드 부분
print('정렬 전 --> ', dataAry)
dataAry = bubbleSortUpper(dataAry)
print('정렬 후 (오름차순 정렬) --> ', dataAry)
dataAry = bubbleSortLower(dataAry)
print('정렬 후 (오름차순 정렬) --> ', dataAry)