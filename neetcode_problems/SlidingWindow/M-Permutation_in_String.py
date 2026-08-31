# Hint: Dynamic Size Sliding Window
# Build the sliding window until you either hit a repeat (move left boundary up) or if you hit a character not useful at all then completely reset.
from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        # s1 < s2 for sure

        chars = Counter(s1)

        #print(seen)
        start = 0
        remain_char = len(s1)
        seen = defaultdict(int)

        for i in range(len(s2)):
            if s2[i] in chars:
                if chars[s2[i]] - seen.get(s2[i], 0) < 1:
                    # move right boundary up to 
                    while start <= i and s2[start] != s2[i]:
                        if s2[start] in chars:
                            remain_char += 1
                            seen[s2[start]] -= 1
                            start += 1
                else:
                    seen[s2[i]] += 1
                    remain_char -= 1
            else:
                start = i+1
                remain_char = len(s1)
                seen = defaultdict(int)

            if remain_char == 0:
                return True

        return False