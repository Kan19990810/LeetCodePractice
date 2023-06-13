
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

Case #1: 99851
Case #2: IMPOSSIBLE
Case #2: IMPOSSIBLE
Case #4: 10
Case #5: IMPOSSIBLE
Case #6: 58619
Case #7: IMPOSSIBLE
Case #7: IMPOSSIBLE
Case #9: 0
Case #10: IMPOSSIBLE
Case #10: IMPOSSIBLE
Case #11: IMPOSSIBLE
Case #13: 63
Case #13: IMPOSSIBLE
Case #15: 99916
Case #16: 90937
Case #17: 1
Case #17: IMPOSSIBLE
Case #19: IMPOSSIBLE
Case #20: 95
Case #21: 99859
Case #22: IMPOSSIBLE
Case #22: IMPOSSIBLE
Case #24: 99815
Case #25: 1
Case #26: 3
Case #27: 0
Case #27: IMPOSSIBLE
Case #29: IMPOSSIBLE
Case #30: IMPOSSIBLE
Case #31: 53
Case #32: IMPOSSIBLE
Case #32: IMPOSSIBLE
Case #34: 99999
Case #35: 64
Case #35: IMPOSSIBLE
Case #36: IMPOSSIBLE
Case #38: IMPOSSIBLE
Case #38: IMPOSSIBLE
Case #40: 99612
Case #41: 54466
Case #42: IMPOSSIBLE
Case #43: 2351
Case #43: IMPOSSIBLE
Case #44: IMPOSSIBLE
Case #46: 99968
Case #47: 99909
Case #47: IMPOSSIBLE
Case #49: IMPOSSIBLE
Case #50: 99911
Case #51: 5
Case #52: 99905
Case #53: 99928
Case #54: IMPOSSIBLE
Case #55: IMPOSSIBLE
Case #56: 65353
Case #57: 85859
Case #58: 50
Case #59: 26229
Case #59: IMPOSSIBLE
Case #60: IMPOSSIBLE
Case #62: 99945
Case #63: 1
Case #64: 72
Case #65: 99999
Case #65: IMPOSSIBLE
Case #66: IMPOSSIBLE
Case #68: IMPOSSIBLE
Case #68: IMPOSSIBLE
Case #70: IMPOSSIBLE
Case #71: 99882
Case #72: 99131
Case #73: 42981
Case #74: 5
Case #74: IMPOSSIBLE
Case #76: IMPOSSIBLE
Case #76: IMPOSSIBLE
Case #78: 82
Case #78: IMPOSSIBLE
Case #80: 24
Case #81: 34291
Case #82: IMPOSSIBLE
Case #83: 50000
Case #84: 99986
Case #85: 5
Case #86: 99299
Case #87: 85092
Case #88: IMPOSSIBLE
Case #89: IMPOSSIBLE
Case #89: IMPOSSIBLE
Case #90: IMPOSSIBLE
Case #92: 3641
Case #92: IMPOSSIBLE
Case #94: 70007
Case #95: 99901
Case #95: IMPOSSIBLE
Case #97: 79623
Case #98: 1
Case #99: 84332
Case #100: IMPOSSIBLE