from decompose import *


class GeneratingArraysFinished(Exception):
    pass


def cong_precheck(a, n):
    cong_check_ = cong(sum_calc(a), n + 1)
    return cong_check_


log_ = open('log.txt', 'w')


def array_gen(n: int):
    # generating an array with n "0"
    a = [0 for i in range(1, n + 1)]

    def rec(s, v, d_=None):
        # 0 index
        if s == 0:
            if a[s] < n + 1:
                a[s] += 1
                if not cong_precheck(a, n):
                    return 0, False, 0
                indecomp = array_check(a)
                return 0, False, indecomp
            elif a[s] == n + 1:
                a[s] = 0
                s += 1
                return s, True, d_

        # move left
        if not v:
            s -= 1
            return s, False, d_

        # n index
        # finish condition
        if v and s == n:

            raise GeneratingArraysFinished

        # turn left
        elif v and (a[s] < n + 1):
            a[s] += 1
            s -= 1
            if not cong_precheck(a, n):
                return 0, False, 0
            indecomp = array_check(a)
            return 0, False, indecomp

        # keep moving right
        elif v and a[s] == n + 1:
            a[s] = 0
            a[s - 1] = 0
            s += 1
            return s, True, d_

    # starting index for the loop
    s_ = n

    # a marker to indicate if all the values to the left from the index are equal n
    v_ = False

    indecomp_count = 0
    indecomp = None
    while True:
        try:
            s_, v_, indecomp_ = rec(s_, v_, indecomp)
            if indecomp_ == 2:
                log_.write(f">>> Array {a} in indecomposable\n")
                # print(f"Array {a} in indecomposable")
                indecomp_count += 1
                continue
            elif indecomp_ == 0:
                # log_.write(f'Sum of array {a} * i in not congruent modulo {n + 1}\n')
                # print(f'Sum of array {a} * i in not congruent modulo {n + 1}')
                continue
            elif indecomp_ == 1:
                log_.write(f'Array {a} is decomposable\n')
                continue
        except GeneratingArraysFinished:
            log_.write("Generating arrays is complete\n")
            log_.write(f'Indecomposable arrays for n={n}: {indecomp_count}\n')
            # print("Generating arrays is complete")
            # print(f'Indecomposable arrays for n={n}: {indecomp_count}')

            return indecomp_count
