# https://codeforces.com/contest/327/problem/A

a = input()
b = input()

a = int(a)
b = [int(i) for i in b.split(' ')]

ma = -1    # max difference, at least one move.
diff = 0   # num of 0 - num of 1
s = 0     # sum of 1
for i in b:
    if i == 0:
        diff += 1
    else:
        diff -= 1
    if diff > ma:
        ma = diff
    elif diff < 0:
        diff = 0
    s += i
s += ma
print(s)


# 1. prefix sum


# 2.