# https://codeforces.com/contest/1187/problem/B
import sys
def sol():
    n = int(input())
    s = input()
    m = int(input())
    for _ in range(m):
        name = sys.stdin.readline().strip('\n')

        dd = {}
        for n in name:
            if dd.get(n):
                dd[n] += 1
            else:
                dd[n] = 1
        cnt = 0
        while dd:
            key = s[cnt]
            if dd.get(key):
                dd[key] -= 1
                if dd[key] == 0:
                    dd.pop(key)
            cnt += 1

        print(cnt)

# timeout

def sol2():
    nn = int(input())
    ss = input()
    A = 26
    ll = [0]*A
    mm = []
    for s in ss:
        j = ord(s) - ord('a')
        ll[j] += 1
        mm.append(ll.copy())

    m = int(input())
    for _ in range(m):
        name = sys.stdin.readline().strip('\n')
        ll = [0]*A
        for n in name:
            ll[ord(n) - ord('a')] += 1

        l = 0
        r = nn
        while r - l > 1 :
            mid = (r+l) //2
            flag = True
            for j in range(26):
                if mm[mid-1][j] < ll[j]:
                    flag = False
                    break
            if flag:
                r = mid
            else:
                l = mid
        print(r)

sol2()
