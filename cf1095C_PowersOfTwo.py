# https://codeforces.com/contest/1095/problem/C

# k > n , no
# divide n into a series of power of two, keep dividing the biggest power of two until k or reach 1.


def main():
    a = input()
    n, k = [int(i) for i in a.split(' ')]
    if k > n:
        print("NO")
        return

    c = [0]*30
    cnt = 0
    for i in range(30):
        if n & 1 << i != 0:
            c[i] += 1
            cnt += 1
    if cnt > k:
        print("NO")
        return
    print("YES")
    k -= cnt
    for i in range(29, 0, -1):
        while k > 0 and c[i] > 0:
            k -= 1
            c[i] -= 1
            c[i-1] += 2
    res = ''
    for i in range(29, -1, -1):
        while c[i] > 0:
            c[i] -= 1
            res += str(1 << i) + ' '
    print(res)


main()







