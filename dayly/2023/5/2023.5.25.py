class Solution:
    def oddString(self, words: List[str]) -> str:
        n, m = len(words), len(words[0])
        diff = [0] * (m - 1)
        cmt = ['a'] * (m - 1)
        for i in range(m - 1):
            diff[i] = ord(words[0][i + 1]) - ord(words[0][i])

        for i in range(m - 1):
            cmt[i] = chr(ord(words[1][i]) + diff[i])

        if ''.join(cmt) != words[1][1:]:
            for i in range(m - 1):
                cmt[i] = chr(ord(words[2][i]) + diff[i])
            if ''.join(cmt) != words[2][1:]:
                return words[0]
            else:
                return words[1]

        else:
            for j in range(2, n):
                for i in range(m - 1):
                    cmt[i] = chr(ord(words[j][i]) + diff[i])
                if ''.join(cmt) != words[j][1:]:
                    return words[j]


