#https://codeforces.com/contest/160/problem/A

a = input()
b = input()

a = int(a)
b = [int(i) for i in b.split()]

s = sum(b)
b.sort(reverse=True)
cnt = 0
my_s = 0
for i in b:
    if s - my_s < my_s:
        break
    else:
        my_s += i
        cnt += 1

print(cnt)
