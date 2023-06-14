
T = int(input())

for i in range(T):
    a = input()
    b = input()
    n, m = len(a), len(b)
    if n > m:
        print('Case #{}: {}'.format(i, 'IMPOSSIBLE'))
        continue

    first, second = 0, 0
    while first < n and second < m:
        if a[first] == b[second]:
            first += 1
            second += 1
        else:
            second += 1
    if first == n:
        print('Case #{}: {}'.format(i + 1, m - n))
    else:
        print('Case #{}: {}'.format(i + 1, 'IMPOSSIBLE'))
