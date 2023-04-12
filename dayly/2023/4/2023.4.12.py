class Solution:
    def longestDecomposition(self, text: str) -> int:
        """
        时间复杂度 O(n^2)
        空间复杂度 O(1)

        :param text:
        :return:
        """
        i, j = 0, len(text) - 1
        count = 0
        left = ''
        right = ''
        while i <= j:
            left += text[i]
            right = text[j] + right
            if i == j:
                break
            else:
                if left == right:
                    left = ''
                    right = ''
                    count += 2
            j -= 1
            i += 1
        if left != '' and right != '':
            count += 1
        return count