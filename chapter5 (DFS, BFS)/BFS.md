## 정리 내용
### BFS란
- breadth first sesarch의 약자
- 너비 우선 탐색을 뜻하며 **가까운 노드부터 탐색하는 알고리즘**이다.
- BFS는 **큐 자료구조**를 이용하는 것이 정석이다.
- BFS의 동작 방식은 아래와 같다.
1) 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
2) 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
3) 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.
- BFS를 구현함에 있어서 deque라이브러리를 사용하는게 유용하다.
- 탐색을 수행함에 있어서 O(N)의 시간이 소요된다.
- 일반적인경우 DFS보다 탐색 수행 시간이 더 빠르다.

### BFS 예제
```python
# BFS 메서드 정의
from collections import deque

def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end='')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)
```

## 출처 && 깃허브
[이것이 취업을 위한 코딩 테스트다 with python](http://www.yes24.com/Product/Goods/91433923)

[github](https://github.com/KYUSEONGHAN/python-for-coding-test)