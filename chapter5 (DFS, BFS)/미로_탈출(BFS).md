## 정리 내용
### 문제 설명
- 난이도: 중
- 시간 제한: 1초
- 메모리 제한: 128mb
- 동빈이는 n*m 크기의 직사각형 형태의 미로에 갇혀있다.
- 동빈이의 위치는 (1, 1)이고 미로의 출구는 (n, m)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다.
- 이 때 괴물이 있는 부분은 0, 괴물이 없는 부분은 1로 표시되어 있다.
- 미로는 반드시 탈출할 수 있는 형태로 제작된다.
- 이 때, 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하라.
### 문제 풀이
- BFS 알고리즘을 활용하면 효과적으로 해결할 수 있다.
- BFS는 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색하기 때문이다.

### 코드
```python
from collections import deque

n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의(상,하,좌,우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# bfs 소스코드 구현
def bfs(x, y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 떄까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:    
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny)) 
    # 가장 오른쪽 아래까지의 최단 거리 반환.
    return graph[n-1][m-1]

print(bfs(0,0))
```

## 출처 && 깃허브
[이것이 취업을 위한 코딩 테스트다 with python](http://www.yes24.com/Product/Goods/91433923)

[github](https://github.com/KYUSEONGHAN/python-for-coding-test)