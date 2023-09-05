class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        n = len(arr)
        arr = sorted(arr)

        dp = [1] * n
        res, mod = 0, 10 ** 9 + 7

        for i in range(n):
            left, right = 0, i - 1
            while left <= right:
                while right >= left and arr[left] * arr[right] > arr[i]:
                    right -= 1
                if right >= left and arr[left] * arr[right] == arr[i]:
                    if right != left:
                        dp[i] = (dp[i] + dp[left] * dp[right] * 2) % mod
                    else:
                        dp[i] = (dp[i] + dp[left] * dp[right]) % mod
                left += 1
            res = (res + dp[i]) % mod
        return res
        # n = len(arr)
        # arr.sort()
        # s = [] * n

        # def find(x, i):
        #     l, r = 0, i
        #     while l < r:
        #         mid = (l + r) // 2
        #         if arr[mid] >= x: r = mid
        #         else: l = mid + 1
        #     return r


        # # 预处理乘积集合
        # for i in range(n):
        #     for j in range(i):
        #         if (arr[i] % arr[j] == 0):
        #             k = find(arr[i] // arr[j], i - 1)
        #             if [arr[i] == arr[j] * arr[k]]:
        #                 s[i].append([j, k])

 
        # MOD = 1e9 + 7
        # # 下标为i 的树为根节点所能构造的二叉树数量
        # @cache
        # def dfs(i):
        #     res = 1

        #     for k in range(len(s[i])):
        #         res += (dfs(s[i][k][0]) + dfs(s[i][k][1]))
        #         res %= MOD
            
        #     return res
        
        # ans = 0
        # for i in range(n):
        #     ans += dfs(i)
        #     ans %= MOD

        # return ans