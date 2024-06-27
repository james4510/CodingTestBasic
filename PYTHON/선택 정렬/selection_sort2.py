# 개선된 선택 정렬
def selectionSort(ary, count):
    n = len(ary)
    count += 1
    for i in range(0, n-1):
        count += 1
        minIdx=i
        for k in range(i+1, n):
            if(ary[minIdx] > ary[k]):
                count += 1
                minIdx=k
        tmp = ary[i]
        ary[i] = ary[minIdx]
        ary[minIdx] = tmp
    return ary

## 전역 변수 선언 부분
dataAry = [188, 162, 168, 120, 50, 150, 177, 105]
count = 0
## 메인 코드 부분
print('정렬 전 --> ', dataAry)
dataAry = selectionSort(dataAry, count)
print('정렬 후 --> ', dataAry)

print('count = %d'%count)