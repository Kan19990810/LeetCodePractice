class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        # 可以得出以 a, b, c 开头的字符串
        # 以 a 开头
        def dfs(a, b, c):
            n1, n2, n3 = len(a), len(b), len(c)
            # a - b - c
            # 检测头尾相同的部分
            k = min(n1,n2)
            j = -1
            for i in range(k):
                if a[n1 - i - 1:] == b[:i + 1]:
                    j = i
            # 进行拼接
            s1 = a + b[j + 1:]
            ns1 = len(s1)

            k = min(ns1, n3)
            j = -1
            for i in range(k):
                if s1[ns1 - i - 1:] == c[:i + 1]:
                    j = i
            s1 = s1 + c[j + 1:]
            ns1 = len(s1)
            # print(s1)

            # 先 b- c 再 a -b -c

            k = min(n2, n3)
            j = -1
            for i in range(k):
                if b[n2 - i - 1:] == c[:i + 1]:
                    j = i
            s3 = b + c[j + 1:]
            ns3 = len(s3)
            print(s3)
            k = min(ns3, n1)
            j = -1
            for i in range(k):
                if a[n1 - i - 1:] == s3[: i + 1]:
                    j = i
            s3 = a + s3[j + 1:]
            ns3 = len(s3)

            if ns3 < ns1:
                s1 = s3
            elif ns3 == ns1:
                if s1 > s3:
                    s1 = s3

            # a - c - b
            # 检测头尾相同的部分
            k = min(n1,n3)
            j = -1
            for i in range(k):
                if a[n1 - i - 1:] == c[:i + 1]:
                    j = i
            # 进行拼接
            s2 = a + c[j + 1:]
            # print(s2)
            ns2 = len(s2)

            k = min(ns2, n2)
            j = -1
            for i in range(k):
                # print(i, s2[ns2 - i - 1:],b[:i + 1])
                if s2[ns2 - i - 1:] == b[:i + 1]:
                    j = i
            s2 = s2 + b[j + 1:]
            ns2 = len(s2)
            # print(s2)


            # 先 c - b 再 a -b -c

            k = min(n2, n3)
            j = -1
            for i in range(k):
                if c[n2 - i - 1:] == b[:i + 1]:
                    j = i
            s3 = c + b[j + 1:]
            ns3 = len(s3)

            k = min(ns3, n1)
            j = -1
            for i in range(k):
                if a[n1 - i - 1:] == s3[: i + 1]:
                    j = i
            s3 = a + s3[j + 1:]
            ns3 = len(s3)

            if ns3 < ns2:
                s2 = s3
            elif ns3 == ns2:
                if s2 > s3:
                    s2 = s3

            if ns1 < ns2:
                return s1
            elif ns2 < ns1:
                return s2
            else:
                if s1 > s2:
                    return s2
                else:
                    return s1
                
        sa = dfs(a, b, c)
        sb = dfs(b, a, c)
        sc = dfs(c, a, b)

        print(sa, sb, sc)
        na, nb, nc = len(sa), len(sb), len(sc)
        if na < nb:
            minx = na
            ans = sa
        elif na > nb:
            minx = nb
            ans = sb
        else:
            minx = na
            if sa < sb:
                ans = sa
            else:
                ans = sb
        
        if nc < minx:
            ans = sc
        if nc == minx:
            if sc < ans:
                ans = sc
        return ans

