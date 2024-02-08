from array_gen_while import *


results = open("results.txt", "w")


def main(m: int):
    for i in range(1, m + 1):
        count = array_gen(i)
        results.write(f'n = {i}: {count}\n')


main(8)
log_.close()
results.close()
