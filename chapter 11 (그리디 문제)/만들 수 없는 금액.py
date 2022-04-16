# 난이도: 하, 메모리 제한: 128MB, K 대회 기출
# 첫째 줄에는 동전의 개수를 나타내는 양의 정수 n이 주어진다. (1<=n<=1000)
# 둘째 줄에는 각 동전의 화폐 단위를 나타내는 n개의 자연수가 주어지며, 각 자연수는 공백으로 구분합니다.
# 이 때, 각 화폐 단위는 1000000 이하의 자연수입니다.
# 첫째 줄에 주어진 동전들로 만들 수 없는 양의 정수 금액 중 최솟값을 출력합니다.
"""input data,  output: 8
5
3 2 1 1 9
"""
import sys

input = sys.stdin.readline

def solve(coins: list) -> int:
    coins.sort()
    result = 1

    for x in coins:
        if result < x:
            break
        result += x

    return result

if __name__ == '__main__':
    n = int(input())
    coins = list(map(int, input().split()))

    print(solve(coins))