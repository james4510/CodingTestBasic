'''
검색 알고리즘의 종류
1. 순차 검색
    - 검색할 집합이 정렬되어 있지 않은 상태
    - 처음부터 차례대로 찾아보는 것으로, 쉽지만 비효율적임
    - 집합의 데이터가 정렬되어 있지 않다면 이 검색 외에 특별한 방법 없음
2. 이진 검색
    - 데이터가 정렬되어 있다면 이진 검색도 사용 가능
    - 순차 검색에 비해 월등히 효율적이라 데이터가 몇 천만 개 이상이어도 빠르게 찾아낼 수 잇음
3. 트리 검색
    - 데이터 검색에는 상당히 효율적이지만 트리의 삽입, 삭제에는 부담
'''

# 순차 검색 - 정렬되지 않은 데이터의 순차 검색
## 클래스와 함수 선언 부분
def seqSearch(ary, fData):
    pos = -1
    size = len(ary)
    print('## 비교한 데이터 ==> ', end=' ')
    for i in range(size):
        print(ary[i], end=' ')
        if ary[i] == fData:
            pos = i
            break
    print()
    return pos

## 전역 변수 선언 부분
dataAry = [188, 150, 168, 162, 105, 120, 177, 50]
findData = 0

## 메인 코드 부분
findData = int(input('*찾을 값을 입력하세요. --> '))
print('배열 --> ', dataAry)

position = seqSearch(dataAry, findData)
if position == -1:
    print(findData, '(이)가 없네요.')
else:
    print(findData, '(은)는 ', position, '번째 위치에 있습니다.')