from sys import stdin

n, t = [int(x) for x in stdin.readline().split()]

di = [0 for _ in range(n + 10)]
bi = [0 for _ in range(n + 10)]

for i in range(1, n + 1):
    di[i], bi[i] = [int(x) for x in stdin.readline().split()]

di[n + 1], bi[n + 1] = t + 1, 0

ans = 0
cnt = 0
last = 0

for i in range(1, n + 2):
    d, b = di[i], bi[i]

    if cnt >= d - last:
        ans += d - last
        cnt = cnt - (d - last) + b
        last = d
    else:
        ans += cnt
        cnt = b
        last = d

print(ans)
