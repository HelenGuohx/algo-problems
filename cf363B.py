#https://codeforces.com/contest/363/problem/B
import sys

def main():
    n, k = [int(i) for i in sys.stdin.readline().strip('\n').split()]
    hh = [int(i) for i in sys.stdin.readline().strip('\n').split()]
    mi_s = float('inf')
    mi_i = 0
    for i in range(n-2):
        s = hh[i] + hh[i+1] + hh[i+2]
        if s < mi_s:
            mi_s = s
            mi_i = i
    print(mi_i + 1 )

def main2():
    n, k = [int(i) for i in input().split()]
    hh = [int(i) for i in input().split()]
    mi_s = 0
    for i in range(n-3):
        if hh[i] >= hh[i+3]:
            mi_s = i + 1
    print(mi_s)


main()

#class note:
#key word : pre sum sum[i] - sum[k]


