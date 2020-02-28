# https://codeforces.com/contest/1245/problem/C

# w -> uu, m -> nn
# number of u/n is i, how many combination of u/n
# dp[i] = dp[i-1] + dp[i-2] which is fibonacci sequence

MD = 10 ** 9 + 7

def main():
    s = input()
    n = len(s)
    fib = [0]*(n+1)
    fib[0] = fib[1] = 1
    i = 2
    while i <= n:
        fib[i] = (fib[i-1] + fib[i-2])%MD
        i += 1

    i = 0
    ans = 1
    while i < n:
        si = s[i]
        if si == 'w' or si == 'm':
            print(0)
            return
        j = i + 1
        if si == 'u' or si == 'n':
            while j < n and s[j] == si:
                j += 1
            ans = (ans * fib[j - i])%MD
        i = j
    print(ans)

main()



