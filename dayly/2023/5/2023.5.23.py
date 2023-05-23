import numpy as np
from collections import Counter
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        values = np.array(values)
        labels = np.array(labels)
        valueInd = np.array(values).argsort()
        values = values[valueInd[::-1]]
        labels = labels[valueInd[::-1]]
        count = Counter()
        num = 0
        ans = 0
        for idx, ele in enumerate(values):
            if num == numWanted:
                break
            if count[labels[idx]] < useLimit:
                ans += int(ele)
                num += 1
                count[labels[idx]] += 1

        return ans
  