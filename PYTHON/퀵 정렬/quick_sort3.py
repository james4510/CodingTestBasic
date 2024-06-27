'''
문제: K번째 수 구하기
수 N개가 주어진다. A를 오름차순 정렬했을 때 앞에서부터 K번째에 있는 수를 구하는 프로그램을 작성하시오.

입력
- 1번째 줄에 N(1 <= N <= 5,000,000)과 K(1 <= K <= N), 2번째 줄에 A1, A2, ... , An이 주어진다.

출력
- A를 정렬했을 때 앞에서부터 K번째에 있는 수를 출력한다.
'''

import sys

input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))

def quickSort(S, E, K):
    global A
    if S < E:
        pivot = partition(S, E)
        if pivot == K:              # K번째 수가 pivot이면 더는 구할 필요 없음
            return
        elif K < pivot:             # K가 pivot보다 작으면 왼쪽 그룹만 정렬
            quickSort(S, pivot-1, K)
        else:                       # K가 pivot보다 크면 오른쪽 그룹만 정렬
            quickSort(pivot+1, E, K)

def swap(i, j):
    global A
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partition(S, E):
    global A

    if S+1 == E:
        if A[S] > A[E]:
            swap(S, E)
        return E
    
    M = (S+E) // 2
    swap(S, M)
    pivot = A[S]
    i=S+1
    j=E
    while i <= j:
        while pivot < A[j] and j > 0:
            j = j - 1
        while pivot > A[i] and i < len(A) - 1:
            i = i + 1

        if i <= j:
            swap(i, j)
            i = i + 1
            j = j - 1
    # i == j 피벗의 값을 양쪽으로 분리한 가운데에 오도록 설정하기
    A[S] = A[j]
    A[j] = pivot
    return j

quickSort(0, N-1, K-1)
print(A[K-1])