# 그리디 알고리즘, 큰 수의 법칙, python3

""" 문제
- 난이도: 하
- 시간 제한: 1초
- 메모리 제한: 128mb제
1. 첫째 줄에 n(2<=n<=1000), m(1<=m<=10000), k(1<=k<=10000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
2. 둘째 줄에 n개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10000이하의 수로 주어진다.
3. 입력으로 주어지는 k는 항상 m보다 작거나 같다.
4. 첫째 줄에 큰 수의 법칙에 따라 더해진 답을 출력한다.
5. 큰 수의 법칙: 주어진 수들을 m번 더하여 가장 큰 수를 만드는 법칙
6. 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수는 없다.
ex) 3,4,3,4,3  m=7, k=2 -> 4+4+4+4+4+4+4 = 28
"""

""" 문제 풀이
- 그리디 알고리즘을 활용
- 입력값 중엫서 가장 큰 수와 두 번째로 큰 수만 저장하면 된다.
- 연속으로 더할 수 있는 횟수는 최대 k번이므로 '가장 큰 수를 k번 더하고 두 번째로 큰 수를 한번 더하는 연산을 반복'하면 문제를 풀 수 있다.
"""

# 풀이1
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()         # 입력받은 수들 정렬하기

first = data[n-1]   # 가장 큰 수
second = data[n-2]  # 두 번째로 큰 수
result = 0

while True:
    for i in range(k):  # 가장 큰 수를 K번 더하기
        if m == 0:
            break
        result += first
        m -= 1  # 더할 때마다 1씩 빼기
    if m == 0:
        break
    result += second  # 두 번째로 큰 수를 한 번 더하기
    m -= 1  # 더할 때마다 1씩 빼기
    # m이 0이 될 때까지 위 사이클 계속 반복

print(result)   # 답 출력


# 풀이 1 코드는 m의 크기가 100억 이상으로 커진다면 시간 초과 판정임

# 더 효율적인 풀이2
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()         # 입력받은 수들 정렬하기

first = data[n-1]   # 가장 큰 수
second = data[n-2]  # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 연산
count = int(m/(k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first  # 가장 큰 수 더하기
result += (m - count) * second  # 두 번째로 큰 수 더하기

print(result)  # 정답 출력
