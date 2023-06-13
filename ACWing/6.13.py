from sys import stdin

n = int(stdin.readline().split()[0])
cattle = str(stdin.readline().split()[0])

odd = [0] * (n // 2)
even = [0] * (n //2)
ans = 0
for i in range(n // 2):
    if cattle[2 * i] == 'G':
        odd[i] = 1
    if cattle[2 * i + 1] == 'G':
        even[i] = 1

buff = True

for i in range(n // 2 - 1, -1, -1):
    if odd[i] > even[i] and buff:
        buff = False
        ans += 1
    if even[i] > odd[i] and not buff:
        buff = True
        ans += 1

print(ans)