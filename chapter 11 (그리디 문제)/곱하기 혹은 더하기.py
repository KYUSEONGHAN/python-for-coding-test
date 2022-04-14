# 난이도: 하, 메모리 제한: 128MB, facebook 기출
# 각 자리가 숫자 0 ~ 9로만 이루어진 문자열s가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 x 혹은 + 연산자를
# 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하라.
# 첫째 줄에 여러 개의 숫자로 구성된 하나의 문자열 s가 주어집니다. (1<=s<=20)
# 첫째 줄에 만들어질 수 있는 가장 큰 수를 출력합니다.

###### 풀이
# 두 수에 대하여 연산을 수행할 때, 두 수 중에서 하나라도 1 이하인 경우에는 더하며, 두 수가 모두 2 이상인 경우에는 곱하면 된다.
""" input data
02984
"""
""" output data
576
"""
""" input data
567
"""
""" output data
210
"""
import sys

input = sys.stdin.readline

def solve(num: str) -> int:
    result = int(num[0])

    for x in range(1, len(num)):
        if int(num[x]) <= 1 or result <= 1:
            result += int(num)
        else:
            result *= int(num)

    return result

if __name__ == '__main__':
    num = str(input())

    print(solve(num))