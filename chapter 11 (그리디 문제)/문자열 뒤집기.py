# 난이도: 하, 메모리 제한: 128MB, boj 1439
# https://www.acmicpc.net/problem/1439

# 풀이: 전부 0으로 바꾸는 경우와 전부 1로 바꾸는 경우 중에서 더 적은 횟수를 가지는 경우를 계산하면 된다.
def solve(data: str) -> int:
    count0, count1 = 0, 0

    if data[0] == '1':
        count0 += 1
    else:
        count1 += 1

    # 두 번째 원소부터 모든 원소를 확인
    for i in range(len(data)-1):
        if data[i] != data[i + 1]:
            # 다음 수에서 1로 바뀌는 경우
            if data[i+1] == '1':
                count0 += 1
            # 다음 수에서 0으로 바뀌는 경우
            else:
                count1 += 1

    return min(count0, count1)

if __name__ == '__main__':
    s = str(input())

    print(solve(s))