class Solution:
    def countSteppingNumbers(self, low:str, high:str) -> int:
        MOD = 10 ** 9 + 7
        def calc(s: str) -> int:
            @cache
            def f(i: int, pre:int, is_limit: bool, is_num: bool) -> int:
                # 最后一位
                if i == len(s):
                    return int(is_num)
                res = 0
                # 跳过这一位
                if not is_num:
                    res = f(i + 1, pre, False, False)
                # 该位置选择， 还不是数字则必须大于0
                low = 0 if is_num else 1
                # 是否到最顶
                up = int(s[i]) if is_limit else 9
                for d in range(low, up + 1):
                    if not is_num or abs(d - pre) == 1:
                        res += f(i + 1, d, is_limit and d == up, True)
                return res % MOD
            return f(0, 0, True, False)
        return (calc(high) - calc(str(int(low) - 1))) % MOD