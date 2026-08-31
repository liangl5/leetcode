# Hint: track using stack and difference to min at the time
# Didn't know if I could use stacks or not, my solution was two stacks to keep track of min.
# The best solution is using one stack and just keeping track of the difference between the value being appended
# and the difference to the minimum at that time.

class MinStack:

    def __init__(self):
        self.arr = [0] * 100
        self.idx = -1
        self.min_elem = [float('inf')]
        self.min_idx = 0

    def push(self, val: int) -> None:
        self.idx += 1
        if self.idx >= len(self.arr):
            self.arr.extend([0] * len(self.arr))

        self.arr[self.idx] = val

        if val <= self.min_elem[self.min_idx]:
            self.min_idx += 1
            if self.min_idx >= len(self.min_elem):
                self.min_elem.extend([0] * len(self.min_elem))

            self.min_elem[self.min_idx] = val

    def pop(self) -> None:
        if self.arr[self.idx] == self.min_elem[self.min_idx]:
            self.min_idx -= 1
        self.idx -= 1
        

    def top(self) -> int:
        return self.arr[self.idx]

    def getMin(self) -> int:
        return self.min_elem[self.min_idx]

        
