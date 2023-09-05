class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        n = [[0, 1, 2, 3], [2, 1, 0, 3], [0, 3, 2, 1], [2, 3, 0, 1]]

        for sub_n in n:
            
            if all(s1[i] == s2[sub_n[i]] for i in range(4)):
                return True
            
        return False