'''
너비 우선 탐색(Breadth-First-Search)
- 그래프를 완전 탐색하는 방법 중 하나
- 시작 노드에서 출발해 시작 노드를 기준으로 가까운 노드를 먼저 방문하면서 탐색하는 알고리즘이다.
- 선입선출(FIFO, First In First Out) 으로 탐색하므로 큐를 이용해 구현한다.
- 가까운 노드를 우선하여 탐색하므로 목표 노드에 도착하는 경로가 여러 개일 때 최단 경로를 보장한다.

BFS 특징
- FIFO(First In First Out) 탐색
- Queue 자료구조 이용

시간 복잡도(노드 수: V, 엣지 수: E)
- O(V+E)

BFS 핵심 이론
1. BFS를 시작할 노드를 정한 후 사용할 자료구조 초기화하기
2. 큐에서 노드를 꺼낸 후 꺼낸 노드의 인접 노드를 다시 큐에 삽입하기
3. 큐 자료구조에 값이 없을 때까지 반복한다
'''

from collections import deque
N, M, Start = map(int, input().split())
A = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)          # 양방향 엣지이므로 양쪽에 엣지를 더하기
    A[e].append(s)

for i in range(N+1):
    A[i].sort()             # 번호가 작은 노드부터 방문하기 위해 정렬하기

def DFS(v):
    print(v, end=' ')
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)
visited = [False] * (N+1)
DFS(Start)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_Node = queue.popleft()
        print(now_Node, end=' ')
        for i in A[now_Node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

print()
visited = [False]*(N+1) # 리스트 초기화
BFS(Start)