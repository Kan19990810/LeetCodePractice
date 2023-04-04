"""
你正在探访一家农场，农场从左到右种植了一排果树。这些树用一个整数数组 fruits 表示，其中 fruits[i] 是第 i 棵树上的水果 种类 。

你想要尽可能多地收集水果。然而，农场的主人设定了一些严格的规矩，你必须按照要求采摘水果：

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/fruit-into-baskets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, right, ans = 0, 0, 0
        ln, rn = fruits[left], fruits[right]
        while right < len(fruits):
            if fruits[right] == rn or fruits[right] == ln:
                ans = max(ans, right - left + 1)
                right += 1
            else:
                left = right - 1
                ln = fruits[left]
                while left >= 1 and fruits[left - 1] == ln:
                    left -= 1
                rn = fruits[right]
                ans = max(ans, right - left + 1)
        return ans


