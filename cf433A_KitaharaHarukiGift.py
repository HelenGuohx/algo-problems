#https://codeforces.com/contest/433/problem/A

a = input()
b = input()

a = int(a)
b = [int(i) for i in b.split(' ')]

c1 = c2 = 0
for i in b:
    if i == 100:
        c1 += 1
    else:
        c2 += 1
c2 %= 2   # 0,1
c1 -= c2 * 2
if c1 < 0 or c1 % 2 == 1:
    print("NO")
else:
    print("YES")


# when c1 is odd, print no
# when c1 is even , if c2 is odd, odd * 2 < even; if c2 is even, yes
# when c1 = 0, if c2 is odd, no; if even, yes




