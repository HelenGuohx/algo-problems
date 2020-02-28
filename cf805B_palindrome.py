# https://codeforces.com/contest/805/problem/B

# 1): generate aabbaabbaabb....

a = input()
a = int(a)

fg = 1
res = ''
for i in range(a):
    if i % 2 == 0:
        fg *= -1
    if fg == 1:
        res += 'b'
    else:
        res += 'a'

print(res)


# note: in max/ min problem, think about extreme situation. In this case, c is used as less as possible