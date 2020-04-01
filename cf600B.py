#https://codeforces.com/contest/600/problem/B


def main():
    n, m = [int(i) for i in input().split()]
    aa = [int(i) for i in input().split()]
    bb = [int(i) for i in input().split()]

    aa.sort()
    ans = []
    for b in bb:
        cnt = 0
        for a in aa:
            if a <= b:
                cnt += 1
        ans.append(str(cnt))
    print(' '.join(ans))


def upper_bound(lst,target):
    l = 0
    r = len(lst)-1
    res = -1
    while l <= r:
        mid = (l + r)//2
        if lst[mid] <= target:
            res = mid
            l = mid + 1
        else:
            r = mid - 1

    return res + 1

def main2():
    n, m = [int(i) for i in input().split()]
    aa = [int(i) for i in input().split()]
    bb = [int(i) for i in input().split()]

    aa.sort()
    ans = ''
    for b in bb:
        k = upper_bound(aa, b)
        ans += str(k) + ' '

    print(ans)



if __name__ == '__main__':
    main2()