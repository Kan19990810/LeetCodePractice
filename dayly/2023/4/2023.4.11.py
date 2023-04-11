class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """
        :param instructions:
        记录每个朝向的步数，有1， 2， 3次转向就成环， 4次转向就需要比较每个朝向的步数
        :return:
        """
        lnum = instructions.count('L')
        rnum = instructions.count('R')
        gnum = instructions.count('G')
        print (lnum - rnum)
        if gnum == 0:
            return True
        if lnum - rnum == 0:
            return False
        match (lnum - rnum) % 4:
            case 0:
                n = len(instructions)
                to = [0] * 4
                idx = 0
                for i in range(n):
                    match instructions[i]:
                        case 'G':
                            to[idx] += 1
                        case 'L':
                            idx = (idx + 1) % 4
                        case 'R':
                            if idx ==0:
                                idx = 4
                            idx -= 1
                print(to)
                if to[0] == to[2] and to[1] == to[3]:
                    return True
                return False
            case _:
                return True