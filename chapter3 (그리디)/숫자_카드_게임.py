# 그리디 알고리즘, 숫자 카드 게임, python3

""" 문제 설명
- 난이도: 하
- 시간 제한: 1초
- 메모리 제한: 128mb
- 숫자 카드 게임의 룰은 다음과 같다.
1. 숫자가 쓰인 카드들이 n * m 형태로 놓여 있다. 이 때 n은 행의 개수를 의미하며, m은 열의 개수를 의미한다.
2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
3. 그 다음 선택된 행에 포함된 카드들중 가장 숫자가 낮은 카드를 뽑아야 한다.
4. 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을것을 고려하여
   최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.
"""

""" 문제 조건
- 첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 m이 공백을 기준으로 하여 각각 자연수로 주어진다.
- 둘째 줄부터 n개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1 이상 10000이하의 자연수이다.
- 첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.
"""

""" ex)
3 3
3 1 2
4 1 4
2 2 2
답: 2
"""

""" 문제 풀이
- 그리디 알고리즘을 활용
- '각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수'를 찾으면 된다.
"""

# min() 함수를 이용한 풀이
n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)  # 현재 줄에서 가장 작은 수
    result = max(result, min_value)  # 가장 작은 수중에서 가장 큰 수 찾기

print(result)


# 2중 반복문을 이용한 풀이
n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001

    for a in data:
        min_value = min(min_value, a)

    result = max(result, min_value)  # 가장 작은 수중에서 가장 큰 수 찾기

print(result)
