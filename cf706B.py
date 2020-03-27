# -*- coding: utf-8 -*-

# https://codeforces.com/contest/706/problem/B
import sys

# dp array
def main():
    n = int(input())
    xl = [int(i) for i in sys.stdin.readline().strip('\n').split()]
    q = int(input())
    ml = []
    for i in range(q):
        t = sys.stdin.readline()
        t = int(t)
        ml.append(t)
    X = 100000
    l = [0]*(X+1)
    for x in xl:
        l[x] += 1

    for x in range(1,X+1):
        l[x] += l[x-1]

    for m in ml:
        if m > X:
            m = X
        print(l[m])


# binary search
def main2():
    n = int(input())
    xl = [int(i) for i in sys.stdin.readline().strip('\n').split()]
    q = int(input())
    ml = []
    for i in range(q):
        t = sys.stdin.readline()
        t = int(t)
        ml.append(t)

    xl.sort()
    for m in ml:
        low_b, upp_b = 0, n
        diff = n

        if m >= xl[upp_b-1]:
            print(n)
            continue

        elif m < xl[low_b]:
            print(0)
            continue

        while diff > 1:
            mid = (low_b + upp_b) // 2
            if m >= xl[mid]:
                low_b = mid
            else:
                upp_b = mid
            diff = upp_b - low_b
        print(low_b+1)



main2()



# class note
# keyword: binary search 二分法
# sort price
# find lower bound and upper bound
# init lower = 0, upper = length, diff = upper - lower,
# if diff > 1, then m = (lower + upper)/2， if val > m, lower = m; else upper = m

# method2
# keyword: dp array

