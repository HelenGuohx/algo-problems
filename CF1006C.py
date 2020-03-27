# https://codeforces.com/contest/1006/problem/C

def main():
    n = int(input())
    dd = [int(i) for i in input().split()]

    idx1 = 0
    idx3 = n-1
    s1 = dd[idx1]
    s3 = dd[idx3]
    s1_max = 0

    while idx1 < idx3:
        if s1 < s3:
            idx1 += 1
            s1 += dd[idx1]
        elif s1 > s3:
            idx3 -= 1
            s3 += dd[idx3]
        else:
            idx1 += 1
            idx3 -= 1
            s1_max = s1
            s1 += dd[idx1]
            s3 += dd[idx3]

    print(s1_max)

main()