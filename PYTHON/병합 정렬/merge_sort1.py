'''
병합 정렬(merge sort)
- 분할 정복(divide and conquer) 방식을 사용해 데이터를 분할하고 분할한 집합을 정렬하며 합치는 알고리즘이다.
- 시간 복잡도는 O(nlogn)이다.

문제
- N개의 수가 주어졌을 때 이를 오름차순 정렬하는 프로그램을 작성하시오.

입력
- 1번째 줄에 수의 개수 N(1 <= N <= 1,000,000), 2번째 줄부터 N개의 줄에 숫자가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수다.
수는 중복되지 않는다.

출력
- 1번째 줄부터 N개의 줄에 오름차순 정렬한 결과를 1줄에 1개씩 출력한다.

'''
def merge_sort(unsorted_list):
    # 크기가 1이면 반환
    if len(unsorted_list) <= 1:
        return unsorted_list
    
    # 리스트를 2분할
    mid = len(unsorted_list) // 2
    left = unsorted_list[:mid]
    right = unsorted_list[mid:]

    # 2분할한 리스트를 각각 merge sort 진행
    left_ = merge_sort(left)
    right_ = merge_sort(right)
    return merge(left_, right_)


def merge(left, right):
    i, j = 0, 0
    sorted_list = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i+=1
        else:
            sorted_list.append(right[j])
            j+=1
    while i<len(left):
        sorted_list.append(left[i])
        i+=1
    while j<len(right):
        sorted_list.append(right[j])
        j+=1
    return sorted_list

unsorted_list = [5, 4, 6, 2, 3, 4, 7, 8, 0, 1]
print('정렬 전 --> ', unsorted_list)
sorted_list = merge_sort(unsorted_list)
print('정렬 후 --> ', sorted_list)