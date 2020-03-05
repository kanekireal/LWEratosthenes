# coding=utf-8
import time


def crible_era(n):
    start = time.time()
    firsts = {1, 2}
    actual_first = 3
    list_checker = [False] * n
    while actual_first < n:
        if not list_checker[actual_first]:
            firsts.add(actual_first)
            deleting = actual_first
            while deleting < n:
                list_checker[deleting] = True
                deleting += actual_first
        actual_first += 2
    end = time.time() - start
    print("\nTime of execution : " + str(end) + " secondes.")
    return firsts


x = int(input("x= "))
Q = crible_era(x + 1)
print("\bFirst numbers (to " + str(x) + ") :")
for i in Q:
    print("-> " + str(i))
