# Hint: sort then calculate using time
# Got a bit confused on the wording, 2 cars can be at the same position, ex 9 & 10 is not a fleet.
# Was thinking too much about positions when instead you can calculate the time it takes to reach the end,
# will always stay the same or go up, if it goes up compared to previous then it is a new fleet.
from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        fleets = 1
        prevTime = (target - pair[0][0]) / pair[0][1]
        for i in range(1, len(pair)):
            currCar = pair[i]
            currTime = (target - currCar[0]) / currCar[1]
            if currTime > prevTime:
                fleets += 1
                prevTime = currTime
        return fleets
