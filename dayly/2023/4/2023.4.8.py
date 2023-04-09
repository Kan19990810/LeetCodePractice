"""
作为项目经理，你规划了一份需求的技能清单 req_skills，并打算从备选人员名单 people 中选出些人组成一个「必要团队」（ 编号为 i 的备选人员 people[i] 含有一份该备选人员掌握的技能列表）。

所谓「必要团队」，就是在这个团队中，对于所需求的技能列表 req_skills 中列出的每项技能，团队中至少有一名成员已经掌握。可以用每个人的编号来表示团队中的成员：

例如，团队 team = [0, 1, 3] 表示掌握技能分别为 people[0]，people[1]，和 people[3] 的备选人员。
请你返回 任一 规模最小的必要团队，团队成员用人员编号表示。你可以按 任意顺序 返回答案，题目数据保证答案存在。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/smallest-sufficient-team
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import List
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n, m = len(req_skills), len(people)
        skill_index = {v: i for i, v in enumerate(req_skills)}
        dp = [None] * (1 << n)
        dp[0] = []
        for i, p in enumerate(people):
            cur_skill = 0
            for s in p:
                cur_skill |= 1 << skill_index[s]
            for prev in range(1 << n):
                if dp[prev] == None:
                    continue
                comb = prev | cur_skill
                if dp[comb] == None or len(dp[comb]) > len(dp[prev]) + 1:
                    dp[comb] = dp[prev] + [i]
        return dp[(1 << n) - 1]