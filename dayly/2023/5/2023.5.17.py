class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:

        ans = False
        for hour in range(24):
            for mini in range(60):
                if hour == int(event1[0][0: 2]) and mini == int(event1[0][3: 5]):
                    if not ans:
                        ans = True
                    else:
                        return True
                if hour == int(event2[0][0: 2]) and mini == int(event2[0][3: 5]):
                    if not ans:
                        ans = True
                    else:
                        return True
                if hour == int(event1[1][0: 2]) and mini == int(event1[1][3: 5]):
                    ans = False
                if hour == int(event2[1][0: 2]) and mini == int(event2[1][3: 5]):
                    ans = False



        return False


