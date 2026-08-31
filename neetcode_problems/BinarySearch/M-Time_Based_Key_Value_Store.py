# Hint: BS
# Messed up the binary search, instead of making it end on the lower value (which you can do by setting m=math.ceil((l+r)/2)
# and making sure l=m, you can simply do a tracker where if vals[m][0] <= timestamp keep track of the value,
# any other cases that trigger this found will be higher timestamp (which we want).

import math

class TimeMap:
    def __init__(self):
        pass

    def set(self, key: str, value: str, timestamp: int) -> None:
        pass

    def get(self, key: str, timestamp: int) -> str:
        pass
