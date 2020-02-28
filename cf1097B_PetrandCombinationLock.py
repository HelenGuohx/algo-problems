# https://codeforces.com/contest/1097/problem/B


# RECURSION + -
import sys

a = input()
b = []
for i in range(a):
    b.append(int(sys.stdin.readline()) )


def recurr(point,idx, l ):
    """

    :param point: total degree
    :param idx: current index  in l
    :param l: list
    :return:
    """
    if idx >= len(l):
        point %= 360
        if point == 0:
            return True
        return False
    return max(recurr(point + l[idx], idx + 1, l), recurr(point - l[idx], idx + 1, l))


if recurr(0, 0, b):
    print("YES")
else:
    print("NO")
