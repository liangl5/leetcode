# Hint: number of chars and a signal char
# First thought was a delimiter that isn't a UTF-8 character, but this is not possible.
# I need to then switch to what can I add at the beginning of every string so that I can grab all of it instantly,
# and need the length and a signal character.
from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res = res + str(len(s)) + "?" + s

        #print(res)
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        num = ''
        while i < len(s):
            #print(i)
            if s[i] == '?':
                
                skip = int(num)
                num = ''
                #print(skip, s[i+1:i+1+skip])
                res.append(s[i+1:i+1+skip])
                i += 1 + skip
            else:
                num += s[i]
                i += 1

        return res
