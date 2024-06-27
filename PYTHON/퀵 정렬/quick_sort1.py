'''
퀵 정렬 (quci sort)
- 기준값(pivot) 을 선정해 해당 값보다 작은 데이터와 큰 데이터로 분류하는 것을 반복해 정렬한다.
- 기준값(pivot) 이 어떻게 선정되는지가 시간 복잡도에 많은 영향을 미친다.
- 평균적인 시간 복잡도는 O(nlogn) 이며 최악의 경우에은 시간 복잡도가 O(n^2)이 된다.
- 데이터의 수가 많을 수록 다른 정렬 알고리즘보다 더 빠른 속도로 정렬한다.

퀵 정렬 과정
1. 데이터를 분할하는 pivot을 설정한다.
2. pivot을 기준으로 다음 a~e 과정을 거쳐 데이터를 2개의 집합으로 분리한다.
    2-a. start가 가리키는 데이터가 pivot이 가리키는 데이터보다 작으면 start를 오른쪽으로 1칸 이동한다.
    2-b. end가 가리키는 데이터가 pivot이 가리키는 데이터보다 크면 end를 왼쪽으로 1칸 이동한다.
    2-c. start가 가리키는 데이터가 pivot이 가리키는 데이터보다 크고, end가 가리키는 데이터가 pivot이 가리키는 데이터보다 작으면,
    start, end가 가리키는 데이터를 swap하고 start는 오른쪽, end는 왼쪽으로 1칸씩 이동한다.
    2-d. start와 end가 만날 때까지 2-a~2-c를 반복한다.
    2-e. start와 end가 만나면 만난 지점에서 가리키는 데이터와 pivot이 가리키는 데이터를 비교하여 pivot이 가리키는 데이터가 크면
    만난 지점의 오른쪽에, 작으면 만남 지점의 왼쪽에 pivot이 가리키는 데이터를 삽입한다.
3. 분리 집합에서 각각 다시 pivot을 선정한다.
4. 분리 집합이 1개 이하가 될 때까지 과정 1~3을 반복한다.
'''

# 퀵 정렬의 간단한 구현
## 클래스와 함수 선언 부분
def quickSort(ary):
    n = len(ary)
    if n<=1:            # 정렬할 리스트의 개수가 1개 이하인 경우
        return ary 
    
    pivot = ary[n // 2] # 기준 값을 중간값으로 지정
    leftAry, rightAry = [], []

    for num in ary:
        if num < pivot:
            print("Divide: left")
            leftAry.append(num)
        elif num > pivot:
            print("Divide: right")
            rightAry.append(num)

    return quickSort(leftAry) + [pivot] + quickSort(rightAry)

## 전역 변수 선언 부분
dataAry = [188, 150, 168, 162, 105, 120, 177, 50]

## 메인 코드 부분
print('정렬 전 --> ', dataAry)
dataAry = quickSort(dataAry)
print('정렬 후 --> ', dataAry)