
class ZeroAnswerException(Exception):
    pass


def sum_calc(a_: list):
    index = 1
    a_sum = 0
    for i in a_:
        a_sum += i * index
        index += 1

    return a_sum


def cong(sum_, d):
    if sum_ != 0 and sum_ % d == 0:
        return True
    else:
        return False


def cong_check(a_1, a_2, d):
    sum_1 = sum_calc(a_1)
    sum_2 = sum_calc(a_2)

    if sum_1 != 0 and sum_2 != 0:
        cong_1 = cong(sum_1, d)

        cong_2 = cong(sum_2, d)
        if cong_1 and cong_2:

            return 1

        return 2
    else:
        return 0


def array_check(array: list):
    only_zero_answers = False

    a = array
    n = len(a)
    # cong_check_ = cong(sum_calc(a), n + 1)
    # if not cong_check_:
    #     return 0

    a_1 = a.copy()
    a_2 = [0 for i in a]

    def decomp(s, v, r):
        r = None
        # finish condition
        if v and s == n:
            r = 2
            return s, v, r

        # 0 index
        if s == 0:
            if a_1[s] > 0:
                a_1[s] -= 1
                a_2[s] += 1
                decomp_flag = cong_check(a_1, a_2, n + 1)
                # print(a_1, a_2)
                if decomp_flag == 1:

                    return s, v, 1
                elif decomp_flag == 0:
                    return s, v, 0
                elif decomp_flag == 2:
                    return s, False, r

            if a_1[s] == 0:
                a_1[s] = a[s]
                a_2[s] = 0
                s += 1
                return s, True, r

        # move left
        if not v:
            s -= 1
            return s, False, r

        # turn left
        if v and a_1[s] > 0:
            a_1[s] -= 1
            a_2[s] += 1
            s -= 1
            decomp_flag = cong_check(a_1, a_2, n + 1)
            # print(a_1, a_2)
            if decomp_flag == 1:
                return s, False, 1
            elif decomp_flag == 0:
                return s, False, 0
            elif decomp_flag == 2:
                return s, False, r
        # keep moving right
        if v and a_1[s] == 0:
            a_1[s] = a[s]
            a_2[s] = 0
            a_1[s - 1] = a[s - 1]
            a_2[s - 1] = 0
            s += 1
            return s, True, r

    # a marker to indicate if all the values to the left from the index are equal 0
    v_ = False
    # starting index
    s_ = n - 1
    # result
    r_ = None

    # main cycle
    while True:

        s_, v_, r_ = decomp(s_, v_, r_)
        # decomposable
        if r_ == 1:
            return 1

        # indecomposable
        if r_ == 2:
            return 2

        if r_ == 0:
            continue





