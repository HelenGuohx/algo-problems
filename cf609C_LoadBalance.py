#https://codeforces.com/contest/609/problem/C

a = input()
b = input()

a = int(a)
b = [int(i) for i in b.split(' ')]

mi = min(b)
ma = max(b)
i = 0
while ma - mi > 1:
    b.remove(mi)
    b.remove(ma)
    b.append(mi + 1)
    b.append(ma - 1)
    mi = min(b)
    ma = max(b)
    i += 1
print(i)


##### method1 ####
# average
# a0 = sum // n, a1 = a0 + 1
# sorting list of servers, b
