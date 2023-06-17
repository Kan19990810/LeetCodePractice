T = int(input())

for i in range(T):
    N = int(input())
    A = [int(x) for x in input().split()]
    d = [[] for _ in range(N)]
    for j in range(N - 1):
        x, y = [int(x) - 1 for x in input().split()]
        if A[x] > A[y]:
            d[x].append(y)
            for e in d[y]:
                d[x].append(e)
        if A[x] < A[y]:
            d[y].append(x)
            for e in d[x]:
                d[y].append(e)
    ma = 0
    for j in range(N):
        ma = max(ma, len(set(d[j])))

    print("Case #{}: {}".format(i + 1, ma + 1))