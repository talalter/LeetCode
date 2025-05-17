class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.v1_turn = True
        self.v1_idx = 0
        self.v2_idx = 0

    def next(self) -> int:
        if self.hasNext():
            if self.v1_turn:
                self.v1_turn = False 
                if self.v1_idx < len(self.v1):
                    res = self.v1[self.v1_idx]
                    self.v1_idx += 1
                    return res
                else:
                    res = self.v2[self.v2_idx]
                    self.v2_idx += 1 
                    return res
            else:
                self.v1_turn = True
                if self.v2_idx < len(self.v2):
                    res = self.v2[self.v2_idx]
                    self.v2_idx += 1
                    return res
                else:
                    res = self.v1[self.v1_idx]
                    self.v1_idx += 1 
                    return res
                
    


    def hasNext(self) -> bool:
        return self.v1_idx < len(self.v1) or self.v2_idx < len(self.v2)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())