# Hint: delayed pointer w/ dummy
# My implementation felt off by one for a majority of it as I didn't properly calculate the number of steps.
# Basically the far right pointer should be ahead by n steps as this allows us to know which node to cut.
# The dummy variable at beginning allows us to remove the head more easily.

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pass
