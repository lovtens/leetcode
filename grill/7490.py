import sys
from functools import reduce


def solution():
    case_count = int(sys.stdin.readline().strip())

    def evaluate_string(s: str):
        if sum(map(int, list(map(lambda x: reduce(lambda a, b: int(a) - int(b), x.split('-')),
                                 "".join(s.split()).split('+'))))) == 0:
            print(s)

    def print_possible_case(n: int, cur: int, s: str):
        if cur == n + 1:
            try:
                evaluate_string(s)
                return
            except RecursionError:
                print(s)
        print_possible_case(n, cur + 1, s + f' {cur}')
        print_possible_case(n, cur + 1, s + f'+{cur}')
        print_possible_case(n, cur + 1, s + f'-{cur}')

    for _ in range(case_count):
        n = int(sys.stdin.readline().strip())
        print_possible_case(n, 2, str(1))
        print('', end='\n')


solution()
