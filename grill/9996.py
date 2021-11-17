import sys


def solution():
    # f = open(f'/Users/ollie/Downloads/contest6_testdata/vjeko/vjeko.in.{num}')
    # n = int(f.readline().strip())
    # p = f.readline().strip()
    n = int(sys.stdin.readline().strip())
    p = sys.stdin.readline().strip()
    # f_result = open(f'/Users/ollie/Downloads/contest6_testdata/vjeko/vjeko.out.{num}')

    def is_match(input_str, pattern_str):
        prefix, postfix = pattern_str.split('*')
        # print(prefix, postfix, input_str[:len(prefix)], input_str[len(postfix):])
        return prefix == input_str[:len(prefix)] and postfix == input_str[-len(postfix):] \
            and len(prefix) - 1 < len(input_str) - len(postfix)

    for _ in range(n):
        filename = sys.stdin.readline().strip()
        # filename = f.readline().strip()
        if is_match(filename, p):
            print("DA")
            # assert f_result.readline().strip() == "DA", f"error: num: {num}, pattern: {p}, filename: {filename}"
        else:
            # assert f_result.readline().strip() == "NE", f"error: num: {num}, pattern: {p}, filename: {filename}"
            print("NE")


# for i in [1, 2, 3, 4, 5, '6a', '6b', '7a', '7b', '8a', '8b', '9a', '9b', '10a', '10b']:
#     solution(i)
solution()
