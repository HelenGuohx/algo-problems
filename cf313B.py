# -*- coding: utf-8 -*-

#https://codeforces.com/contest/313/problem/B
import sys

def main():
    ss = input()
    m = int(input())
    qq = []
    for i in range(m):
        q = sys.stdin.readline()
        q = [int(i) for i in q.split()]
        qq.append(q)

    # create sl that if at index i si = si+1
    n = len(ss)
    sl = [0] * n
    for i in range(n-1):
        if ss[i] == ss[i+1]:
            sl[i] = 1

    for q in qq:
        l,r = q
        print(sum(sl[l:r]))
main()






