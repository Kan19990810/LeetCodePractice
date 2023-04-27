def isPre(wordA: List[str], wordB: List[str]) -> bool:
    lenA, lenB = len(wordA), len(wordB)
    if lenB == lenA + 1:
        idx = 0
        for _, element in enumerate(wordB):
            if element == wordA[idx]:
                idx += 1
        if idx == lenA:
            return True

    return False


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        cnt = defaultdict(int)
        words.sort(key=len)
        res = 0
        for word in words:
            cnt[word] = 1
            for i in range(len(word)):
                prev = word[:i] + word[i + 1:]
                if prev in cnt:
                    cnt[word] = max(cnt[word], cnt[prev] + 1)
            res = max(res, cnt[word])
        return res

