# -*- coding: utf-8 -*-
# https://codeforces.com/contest/1196/problem/B

# odd + odd = even, even + even = even, odd + even = odd
# yes: num of odd > num of subsegment and when k is even(odd), num of odd is even(odd) 同奇同偶


import sys
a = input()
b = sys.stdin.readlines()
b = [ i.strip('\n') for i in b]
for i in range(0,len(b),2):
    line1 = b[i]
    line2 = b[i+1]
    n,k = [int(i) for i in line1.split(' ')]
    line2 = [int(i) for i in line2.split(' ')]
    odd_num = 0
    odd_index = []
    for idx, l in enumerate(line2):
        if l & 1 == 1:
            odd_num += 1
            odd_index.append(idx+1)

    if odd_num >= k and (odd_num & 1) == (k & 1):
        print("YES")
        print(" ".join([str(o) for o in odd_index[:k-1]] + [str(n)]))
    else:
        print("NO")




# note: odd_num > k and k is odd