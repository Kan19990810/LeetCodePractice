class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        dic = {'01': 0, '02': 31, '03': 59, '04': 90, '05': 120, '06': 151, '07': 181, '08': 212, '09': 243, '10': 273, '11': 304, '12': 334}

        alice, bob = [0, 0], [0, 0]

        alice[0] = dic[arriveAlice[0:2]] + int(arriveAlice[3:5])

        alice[1] = dic[leaveAlice[0:2]] + int(leaveAlice[3:5])

        bob[0] = dic[arriveBob[0:2]] + int(arriveBob[3:5])

        bob[1] =dic[leaveBob[0:2]] + int(leaveBob[3:5])

        ans = min(alice[1], bob[1]) - max(alice[0], bob[0]) + 1

        return ans if ans > 0 else  0


