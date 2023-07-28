class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        # 按行进行排序
        for i in grid:
            i.sort()

        # zip(*) 解压 相当于将矩阵转置    
        return sum([max(i) for i in zip(*grid)])