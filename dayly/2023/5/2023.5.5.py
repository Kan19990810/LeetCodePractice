class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        ansId = logs[0][0]
        maxTime = logs[0][1]

        for idx, log in enumerate(logs):
            if idx == 0:
                continue
            if logs[idx][1] - logs[idx - 1][1] == maxTime:
                ansId = min(ansId, logs[idx][0])
            elif logs[idx][1] - logs[idx - 1][1] > maxTime:
                ansId = logs[idx][0]
                maxTime = logs[idx][1] - logs[idx - 1][1]

        return ansId




