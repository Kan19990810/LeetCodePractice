from typing import List
def kill(monster: List[int]) -> int:
    n = len(monster)
    monster.sort()
    # 累计刀数
    res = 0

    # 累计转圈圈数
    cum = 0
    # 残血
    leave = [0] * n

    for i in range(n):
        target = monster[i] // 2
        # 当前血量不能转圈圈
        if monster[i] - cum >= target:
            res += monster[i] - cum - target
            cum += 1
            # 转圈圈后残血血量
            leave[i] = target - 1
            # 更新残血状态， 之前的怪会遭受后面转圈圈的影响
            if target - 1 - (n - i - 1) > 0:
                leave[i] = target - 1 - (n - i - 1)
            else:
                leave[i] = 0
        # 当前血量满足转圈圈，则不需要再刀
        else:
            cum += 1
            leave[i] = monster[i] - cum
            if monster[i] - n > 0:
                leave[i] = monster[i] - n
            else:
                leave[i] = 0

    
    res += sum(leave)
    return res
    

if __name__ == "__main__":
    monster = [1, 8, 8, 8, 8, 8, 8]
    print(kill(monster))




        