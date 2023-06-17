t = int(input())

for x in range(t):
    l, n = [int(i) for i in input().split()]
    ans, dir, loc = 0, 0, 0

    for i in range(n):
        d, c = [a for a in input().split()]
        d = int(d)
        if loc == 0:
            dir = 0 if c == 'C' else 1
        if c == 'C':
            loc += d
            if dir == 0:
                ans += loc // l
            elif dir == 1 and loc > l:
                dir = 0
                if loc // l > 1:
                    ans += loc // l - 1
            loc %= l
        if c == 'A':
            loc -= d
            if dir == 0 and loc < 0:
                dir = 1
                if loc // l < -1:
                    ans -= loc // l + 1
            elif dir == 1:
                ans -= loc // l
            loc %= l
    print("Case #{}: {}".format(x + 1, ans))

Case #1: 18
Case #2: 12
Case #3: 55
Case #4: 0
Case #5: 1
Case #6: 0
Case #7: 10000
Case #8: 10000000000000
Case #9: 10000
Case #10: 0
Case #11: 500
Case #12: 253
Case #13: 2775570271
Case #14: 10000
Case #15: 6390
Case #16: 8739
Case #17: 4121
Case #18: 2169
Case #19: 1696
Case #20: 4041
Case #21: 12887
Case #22: 535
Case #23: 2841
Case #24: 9328
Case #25: 1169
Case #26: 542
Case #27: 436
Case #28: 16279
Case #29: 1448
Case #30: 6125
Case #31: 470
Case #32: 1341
Case #33: 70231
Case #34: 1490
Case #35: 1395
Case #36: 957
Case #37: 1234
Case #38: 10066
Case #39: 6346
Case #40: 3209
Case #41: 6252
Case #42: 2425
Case #43: 1523
Case #44: 207
Case #45: 2078
Case #46: 386
Case #47: 4320
Case #48: 2755
Case #49: 42649
Case #50: 1535
Case #51: 9644
Case #52: 2522
Case #53: 10650
Case #54: 1211
Case #55: 5753
Case #56: 2613
Case #57: 6297
Case #58: 2767
Case #59: 3121
Case #60: 3664
Case #61: 1405
Case #62: 12119
Case #63: 37096
Case #64: 3535
Case #65: 2729
Case #66: 3936
Case #67: 2337
Case #68: 7774
Case #69: 1711
Case #70: 1146
Case #71: 2701
Case #72: 5727
Case #73: 337
Case #74: 657
Case #75: 5086
Case #76: 256
Case #77: 665
Case #78: 2322
Case #79: 268
Case #80: 18207
Case #81: 2089
Case #82: 776
Case #83: 4201
Case #84: 686
Case #85: 85
Case #86: 3686
Case #87: 2465
Case #88: 1894
Case #89: 3640
Case #90: 18645
Case #91: 15228
Case #92: 2686
Case #93: 1265
Case #94: 10361
Case #95: 823
Case #96: 8345
Case #97: 9675
Case #98: 2769
Case #99: 5591
Case #100: 32564