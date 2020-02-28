# https://codeforces.com/contest/579/problem/A

# 1) int to bit, then count 1


a = int(input())
print( '{0:b}'.format(a).count('1') )
