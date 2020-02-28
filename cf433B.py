# https://codeforces.com/contest/433/problem/B

import sys


def main1():
    n = int(input())
    v = [int(i) for i in input().split()]
    m = int(input())

    v_cp = sorted(v)
    idx = 0
    ans = []
    while True:
        if idx >= m:
            break
        idx += 1
        t, l, r = [int(i) for i in sys.stdin.readline().split()]
        if t == 1:
            ans.append(sum(v[l - 1:r]))
        elif t == 2:
            ans.append(sum(v_cp[l - 1:r]))

    for i in ans:
        print(i)


# class note: presum
# O(mn) is slow
# [sum(1:1), sum(1:2), sum(1:3), ...., sum(1:l), ..., sum(1:r), ...]
# sum(l,r) = sum(1:r) - sum(1:l)

def main2():
    n = int(input())
    v = [int(i) for i in input().split()]
    m = int(input())
    v_cp = sorted(v)
    for i in range(1, len(v)):
        v[i] += v[i - 1]
        v_cp[i] += v_cp[i - 1]

    while m > 0:
        m -= 1
        t, l, r = [int(i) for i in sys.stdin.readline().split()]
        l -= 1
        r -= 1
        if t == 1:
            print(v[r] - v[l - 1] if l > 0 else v[r])
        else:
            print(v_cp[r] - v_cp[l - 1] if l > 0 else v_cp[r])


main2()
