# Hint: alphanumeric, 2 pointers
# Did not fully read checking only alphanumeric numbers, use .isalphanum().
# Smart usage of continue, was too lazy to write while l < r and not l.isalphanum(),
# so did if l.isalphanum(): .. continue

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        l, r = 0, len(s)-1

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue

            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1

        return True
