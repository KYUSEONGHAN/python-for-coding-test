# 난이도: 하, 메모리 제한: 128MB, facebook 인터뷰 기출
# 알파벳 대문자와 숫자(0-9)로만 구성된 문자열이 입력으로 주어진다.
# 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
# 첫째 줄에 하나의 문자열 S가 주어진다 (1<=s의 길이<=10000)
# 첫째 줄에 문제에서 요구하는 정답을 출력합니다.
def solve(data: str):
    result = []
    value = 0

    # 문자를 하나씩 확인하며
    for x in data:
        # 알파뱃인 경우 결과 리스트에 삽입
        if x.isalpha():
            result.append(x)
        # 숫자인 경우
        else:
            value += int(x)

    # 알파뱃을 오름차순으로 정렬
    result.sort()

    # 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
    if value != 0:
        result.append(str(value))

    # 최종 결과 출력 (리스트를 문자열로 변환하여 출력)
    return ''.join(result)

if __name__ == '__main__':
    s = str(input())

    print(solve(s))