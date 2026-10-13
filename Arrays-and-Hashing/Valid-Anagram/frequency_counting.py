class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Make comparison case-insensitive.
        s = s.casefold()
        t = t.casefold()

        if len(s) != len(t):
            return False

        # Count each character in s.
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        # Match each character in t against the counts.
        for ch in t:
            if ch not in count or count[ch] == 0:
                return False
            count[ch] -= 1

        return True


# Average time: O(n)
# Extra space: O(k), where k is the number of distinct characters.
# This version compares strings case-insensitively.
