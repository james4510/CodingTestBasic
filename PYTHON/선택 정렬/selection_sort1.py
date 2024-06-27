'''
선택 정렬(selection sort)
- 대상 데이터에서 최대나 최소 데이터를 데이터가 나열된 순으로 찾아가며 선택하는 방법
- 선택 정렬은 구현이 복잡하고 시간 복잡도도 O(n^2)으로 효율적이지 않다.
- 코딩 테스트에서는 많이 사용하지 않는다.
'''

# 배열에서 최솟값 위치를 찾는 함수
def findMinIdx(ary):
    minIdx = 0
    for i in range(1, len(ary)):
        if(ary[minIdx] > ary[i]):
            minIdx = i
    return minIdx

testAry = [55, 88, 77, 33]
minPos = findMinIdx(testAry)
print('최솟값 위치 --> ', minPos)
print('최솟값 --> ', testAry[minPos])