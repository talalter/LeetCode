class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        idx = -1
        for operation in operations:
            if operation == "D":
                res.append(res[idx]*2)
                idx += 1
            elif operation == "C":
                res.pop(idx)
                idx -= 1
            elif operation == "+":
                res.append(res[idx] + res[idx-1])
                idx += 1 
            else:
                res.append(int(operation))
                idx+=1
        return sum(res)