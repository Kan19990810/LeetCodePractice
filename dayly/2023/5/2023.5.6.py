from collections import Counter


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        frogs = Counter({'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0})
        ans = 0
        for _, element in enumerate(croakOfFrogs):
            frogs[element] += 1
            ans = max(frogs['c'] - frogs['k'], ans)
            if not frogs['c'] >= frogs['r'] >= frogs['o'] >= frogs['a'] >= frogs['k']:
                return -1

        return ans if frogs['c'] == frogs['r'] == frogs['o'] == frogs['a'] == frogs['k'] else -1
