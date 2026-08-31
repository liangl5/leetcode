# Hint: Dynamic Size Sliding Window
# Build the sliding window on s until you achieve all chars of t, from here, you can then shrink the LHS until it is not valid.
# Once you know the min_length of a valid substring, you can start moving LHS and RHS together
# (technically you don't have to do this step, probably for sake of clarity don't need this).
from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        # basically sliding window on S until remain_chars == 0. Then we shorten the LHS
        # as much as possible. Keep track of the min window, now we move right and left at the same
        # time
        chars = Counter(t)
        seen = defaultdict(int)
        remain_chars = len(t)
        res = ""
        min_len = float('inf')
        lhs = 0

        for i, c in enumerate(s):
            if c in chars:
                seen[c] += 1
                if seen[c] <= chars[c]:
                    remain_chars -= 1
            
            if lhs-i >= min_len:
                if s[lhs] in chars:
                    seen[s[lhs]] -= 1
                    if seen[s[lhs]] < chars[s[lhs]]:
                        remain_chars += 1
                lhs += 1


            if remain_chars == 0:
                while remain_chars == 0:
                    if s[lhs] in chars:
                        seen[s[lhs]] -= 1
                        if seen[s[lhs]] < chars[s[lhs]]:
                            remain_chars += 1

                    lhs += 1

                if i-lhs < min_len:
                    #print("remain_chars=0", i, lhs)

                    res = s[lhs-1 : i+1]
                    min_len = i-lhs
            #print(lhs, i, res)

        return res
                

            
        
