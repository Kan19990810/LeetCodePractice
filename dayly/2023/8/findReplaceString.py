class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        n, m = len(s), len(indices)
        sort_indices = sorted(enumerate(indices), key=lambda x:x[1])
        index = [i[0] for i in sort_indices]
        ans = ""
        idx = 0
        for i in range(m):
            # idx 表示上次匹配结束的位置 indices[i] 本次匹配的位置
            ans += s[idx: indices[index[i]]]
            # 匹配成功
            if s[indices[index[i]]: indices[index[i]] + len(sources[index[i]])] == sources[index[i]]:
                ans += targets[index[i]]
                idx = indices[index[i]] + len(sources[index[i]])
            else:
                idx = indices[index[i]]
        ans += s[idx:]
        return ans
            