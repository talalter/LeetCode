from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.current_sum = 0
        self.queue = deque()


    def next(self, val: int) -> float:

        self.queue.append(val)        
        self.current_sum += val
        if len(self.queue) > self.size:
            self.current_sum -= self.queue.popleft()
        return self.current_sum / len(self.queue)

        

        



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)