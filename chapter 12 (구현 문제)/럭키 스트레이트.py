# https://www.acmicpc.net/problem/18406
# 난이도: 하, 메모리 제한: 256MB, boj 18406
def solve(n: str) -> str:
    l = list(map(int, str(n)))

    return 'LUCKY' if sum(l[:len(n)//2]) == sum(l[len(n)//2:]) else 'READY'

if __name__ == '__main__':
    n = str(input())

    print(solve(n))