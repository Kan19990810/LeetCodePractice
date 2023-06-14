class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        class Solution:
            def longestPalindrome(self, word1: str, word2: str) -> int:
                s = word1 + word2
                ans, n = 0, len(s)
                f = [[0] * n for _ in range(n)]
                for i in range(n - 1, -1, -1):
                    f[i][i] = 1
                    for j in range(i + 1, n):
                        if s[i] == s[j]:
                            f[i][j] = f[i + 1][j - 1] + 2
                            if i < len(word1) <= j:
                                ans = max(ans, f[i][j])  # f[i][j] 一定包含 s[i] 和 s[j]
                        else:
                            f[i][j] = max(f[i + 1][j], f[i][j - 1])
                return ans

        # @cache
        # def dfs(i, j, bo):
        #     if i + 1 == j and word[i] != word[j] and not bo:
        #         return 0
        #     if i == j:
        #         return 1
        #     if i > j:
        #         return 0
        #     if word[i] == word[j]:
        #         return dfs(i + 1, j - 1, True) + 2
        #     else:
        #         if i == a - 1 and j > a and not bo:
        #             return dfs(i, j - 1, bo)
        #         if i < a - 1 and j == a and not bo:
        #             return dfs(i + 1, j, bo)
        #         return max(dfs(i + 1, j, bo), dfs(i, j - 1, bo))
        #
        # return dfs(0, n - 1, False)
