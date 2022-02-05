## 정리 내용
### 문제 설명
- 난이도: 중
- 시간 제한: 1초
- 메모리 제한: 128mb
- n*m 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
- 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
- 이 때, 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하라.
- ex) 4*5 -> 00110, 00011, 11111, 00000 에서는 총 3개가 생성된다.

### 문제 풀이
- DFS 알고리즘을 활용하여 풀 수 있다.
1. 특정한 지점의 주변 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문한다.
2. 방문한 지점에서 다시 상, 하, 좌, 우를 살펴보면서 방문을 다시 진행하면, 연결된 모든 지점을 방문할 수 있다.
3. 1 ~ 2번의 과정을 모든 노드에 반복하여 방문하지 않은 지점의 수를 센다.

### 코드
```python
# n, m을 공백을 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# dfs로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        
        return True
        
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 dfs 수행
        if dfs(i, j) == True:
            result += 1

print(result) 
```

## 출처 && 깃허브
[이것이 취업을 위한 코딩 테스트다 with python](http://www.yes24.com/Product/Goods/91433923)

[github](https://github.com/KYUSEONGHAN/python-for-coding-test)