# 난이도: 하, 메모리 제한: 128MB
# 첫째 줄에 모험가의 수 N이 주어진다. (1 <= n <= 100000)
# 둘째 줄에 각 모험가의 공포도 값을 n 이하의 자연수로 주어지며, 각 자연수는 공백으로 구분합니다.
# 여행을 떠날 수 있는 그룹 수의 최댓값을 출력하라.
""" input data
5
2 3 1 2 2
"""
""" output data
2
"""
import sys

input = sys.stdin.readline

def solve(gongpo: list) -> int:
    result = 0

    while gongpo:
        max_num = max(gongpo)
        del(gongpo[gongpo.index(max_num)])
        gongpo.sort()
        gongpo = gongpo[max_num:]
        result += 1

    return result

if __name__ == '__main__':
    n = int(input())
    gongpo = list(map(int, input().split()))

    print(solve(gongpo))