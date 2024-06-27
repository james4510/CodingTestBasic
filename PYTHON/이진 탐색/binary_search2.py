'''
이진 탐색(binary search)
- 오름차순으로 정렬된 배열을 반복적으로 반으로 나누어 target이 선택될 때까지 탐색하는 알고리즘

이진 탐색의 조건
- 반드시 오름차순으로 정렬된 상태에서 시작해야 한다.

이진 탐색 알고리즘
- 시간 복잡도: O(logN)
- 반복문 or 재귀
    1. 자료를 오름차순으로 정렬한다.
    2. 자료의 중간값(mid)이 찾고자 하는 값(target) 인지 비교한다.
    3. mide 값이 target과 다르다면 대소관계를 비교하여 탐색 범위를 좁히고, target과 mid값이 같을 때까지
    아래 조건게 따라 2, 3번을 반복한다.
        a. target이 mid값 보다 작으면 end를 mid 왼쪽 값으로 바꿔준다. (절반의 왼쪽 탐색)
        b. target이 mid값 보다 크면 start를 mid 오른쪽 값으로 바꿔준다. (절반의 오른쪽 탐색)
'''

# 이진 탐색 함수 (반복문)
def binary_search(target, data):
    data.sort()
    start = 0               # 맨 처음 위치
    end = len(data) - 1     # 맨 마지막 위치

    while start <= end:
        mid = (start + end) // 2 # 중간값

        if data[mid] == target:
                return mid      # target 위치 반환
        elif data[mid] > target:    # target이 중간값보다 작으면 왼쪽을 더 탐색
             end = mid - 1
        else:                   # target이 중간값보다 크면 오른쪽을 더 탐색
             start = mid + 1

# 이진 탐색 함수 (재귀)
def binary_search(target, start, end):
     if start > end:        # 범위를 넘어도 못찾는다면 -1을 반환
          return -1
     
     mid = (start + end) // 2 # 중간값

     if data[mid] == target: # 중간값의 데이터가 target과 같다면 mid를 반환
          return mid
     elif data[mid] > target: # target이 작으면 왼쪽 탐색
          end = mid - 1
     else:                    # target이 크면 오른쪽 탐색
          start = mid + 1

     return binary_search(target, start, end)    # 줄어든 범위를 더 탐색

def solution(target, data):
     data.sort()    # 정렬(필수)
     start = 0
     end = len(data) - 1
     return binary_search(target, start, end)