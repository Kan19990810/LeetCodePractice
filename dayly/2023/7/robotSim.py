class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direct = 0
        ans = 0
        start = [0, 0]
        end = [0, 0]

        obstacles_x = obstacles.sort(key = lambda i: i[0])
        obstacles_y = obstacles.sort(key = lambda i: i[1])

        for i in commands:
            if commands == -1:
                direct += 1
                direct %= 4
            elif commands == -2:
                direct -= 1
                direct %= 4
            else:
                if direct == 0:
                    end[0] = start[0]
                    end[1] = start[1] + commands



                elif direct == 1:
                    end[0] = start[0] + commands
                    end[1] = start[1]
                elif direct == 2:
                    end[0] = start[0]
                    end[1] = start[1] - commands
                else:
                    end[0] = start[0] -commands
                    end[1] = start[1]
            
