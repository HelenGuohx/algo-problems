#https://codeforces.com/contest/709/problem/B

# greedy

l1 = [ int(i) for i in input().split(' ') ]
l2 = [ int(i) for i in input().split(' ') ]
n, a = l1


# sort list l1 with a
l = l1.append(a).sort()

# start position, two directions, stop until find n-1 checkpoints.
curr = l.indexOf(a)
left = curr - 1
right = curr + 1
minDis = 0
c = 0 # num of check points
while left >= 0 and left <= len(l) and c < n-1:
    minDis += l(curr) - l[left]
    curr -= 1
    left -= 1
    c += 1
