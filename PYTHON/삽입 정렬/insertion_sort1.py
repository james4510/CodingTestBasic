'''
삽입 정렬(insertion sort)
- 이미 정렬된 데이터 범위에 정렬되지 않은 데이터를 적절한 위치에 삽입시키는 방식
- 평균 시간 복잡도는 O(n^2) 으로 느린 편이지만 구현하기가 쉽다.

삽입 정렬 과정
1. 현재 index에 있는 데이터 값을 선택한다.
2. 현재 선택한 데이터가 정렬된 데이터 범위에 삽입될 위치를 탐색한다.
3. 삽입 위치부터 index에 있는 위치까지 shift 연산을 수행한다.
4. 삽입 위치에 현재 선택한 데이터를 삽입하고 index++ 연산을 수행한다.
5. 전체 데이터의 크기만큼 index가 커질 때까지, 즉 선택할 데이터가 없을 때까지 반복한다.
'''

# 클래스와 함수 선언 부분
def findInsertIdx(ary, data):
    findIdx = -1    # 초기값은 없는 위치로
    for i in range(0, len(ary)):
        if(ary[i] > data):
            findIdx = i
            break
    if findIdx == -1:    # 큰 값을 못 찾음 == 제일 마지막 위치
        return len(ary)
    else:
        return findIdx
    
# 전역 변수 선언 부분
before = [188, 162, 168, 120, 50, 150, 177, 105]
after = []

# 메인 코드 부분
print('정렬 전 --> ', before)
for i in range(len(before)):
    data = before[i]
    insPos = findInsertIdx(after, data)
    after.insert(insPos, data)
print('정렬 후 --> ', after)