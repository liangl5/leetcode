# Hint: BS
# Messed up the binary search, instead of making it end on the lower value (which you can do by setting m=math.ceil((l+r)/2)
# and making sure l=m, you can simply do a tracker where if vals[m][0] <= timestamp keep track of the value,
# any other cases that trigger this found will be higher timestamp (which we want).

class TimeMap:

    def __init__(self):
        self.vals = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.vals:
            self.vals[key].append((timestamp, value))
        else:
            self.vals[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        res, vals = "", self.vals.get(key, [])

        l, r = 0, len(vals)-1

        while l <= r:
            m = (l+r)//2

            if vals[m][0] <= timestamp:
                res = vals[m][1]
                l = m + 1
            else:
                r = m-1
        
        return res
