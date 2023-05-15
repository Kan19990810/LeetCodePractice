class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for _, ele in enumerate(details):
            if int(ele[11: 13]) > 60:
                ans += 1

        return ans