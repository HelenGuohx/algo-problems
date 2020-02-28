#https://codeforces.com/contest/368/problem/B


import sys
n, m = [ int(i) for i in input().split()]
a = [int(i) for i in input().split()]
l = [int(i.strip('\n')) for i in sys.stdin.readlines()]


cnt = 0
cnt_l = [0]*len(a)
dist = {}

for i in range(len(a)-1, -1, -1):
    if not dist.get(a[i]):
        dist[a[i]] = 1
        cnt += 1
        cnt_l[i] = cnt
    else:
        cnt_l[i] = cnt


for i in l:
    print(cnt_l[i-1])


# class note: dp[i] = dp[i+1] + 1