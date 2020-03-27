#https://codeforces.com/contest/1008/problem/C

n = int(input())
aa = [int(i) for i in input().split()]

aa_s = sorted(aa)
ans = 0
i = 1
for j in range(n):
    while i < n :
        if aa_s[i] > aa_s[j]:
            ans += 1
            i += 1
            break
        i += 1

print(ans)


# Help Vasya to permute integers in such way that the number of positions in a new array,
# where integers are greater than in the original one, is maximal.
# 对原数组进行排列，使得在同个index上， 新数组的元素大于原数组的个数最多