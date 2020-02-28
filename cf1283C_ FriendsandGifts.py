# https://codeforces.com/contest/1283/problem/C



# note:
# 1):
# ij = [] index of 0
# ab = []
# backward



a = input()
b = input()

a = int(a)
b = [int(i) for i in b.split(' ')]


def swap(x,y):
    temp = x
    x = y
    y = temp
    return x, y


zero_idx = [i+1 for i, v in enumerate(b) if v == 0]
rest_idx = []
for i in range(a):
    if i+1 not in b:
        rest_idx.append(i+1)

for i in range(len(zero_idx)):
    if zero_idx[i] == rest_idx[i]:
        zero_idx[i], zero_idx[-1] = swap(zero_idx[i], zero_idx[-1])


if zero_idx[-1] == rest_idx[-1]:
    zero_idx[0],zero_idx[-1] = swap(zero_idx[0], zero_idx[-1])

for i in range(len(zero_idx)):
    b[zero_idx[i] - 1] = rest_idx[i]

print(" ".join([str(i) for i in b]))

# 2) cycles


