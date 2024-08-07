# 퀵 정렬의 간단한 구현 (중복된 값 고려)
## 클래스와 함수 선언 부분
def quickSort(ary):
    n = len(ary)
    if n<=1:            # 정렬할 리스트의 개수가 1개 이하인 경우
        return ary 
    
    pivot = ary[n // 2] # 기준 값을 중간값으로 지정
    leftAry, midAry, rightAry = [], [], []

    for num in ary:
        if num < pivot:
            print("Divide: left")
            leftAry.append(num)
        elif num > pivot:
            print("Divide: right")
            rightAry.append(num)
        else:
            midAry.append(num)

    return quickSort(leftAry) + midAry + quickSort(rightAry)

## 전역 변수 선언 부분
dataAry = [188, 150, 168, 162, 105, 120, 177, 50]

## 메인 코드 부분
print('정렬 전 --> ', dataAry)
dataAry = quickSort(dataAry)
print('정렬 후 --> ', dataAry)