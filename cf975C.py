# https://codeforces.com/contest/975/problem/C


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

def main():
    n, q = [int(i) for i in input().split()]
    aa = [int(i) for i in input().split()]
    kk = [int(i) for i in input().split()]

    ss = aa
    for i in range(1,n):
        ss[i] += ss[i-1]

    agg = 0
    for k in kk:
        agg += k
        if agg >= ss[n-1]:
            agg = 0
            print(n)
            continue

        idx = upper_bound(ss, agg)
        print(n-idx)

main()

# note: pre sum k, and using binary search to find the upper bound