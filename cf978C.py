#https://codeforces.com/contest/978/problem/C

def main():
    n,m = [int(i) for i in input().split()]
    aa = [int(i) for i in input().split()]
    bb = [int(i) for i in input().split()]

    pre_s = 0
    idx = 0
    for b in bb:
        while idx < n and pre_s + aa[idx] < b:
            pre_s += aa[idx]
            idx += 1
        print(idx + 1, b - pre_s)



main()

# note: pre_s, calculate the sum of rooms less than the bj, room num in letter
# idx: the indicates the dorm number - 1