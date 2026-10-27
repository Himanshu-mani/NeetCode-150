from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        # Time: O(N + K), Space: O(N + K)
        # N = total characters across all strings, K = number of strings
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        # Time: O(M), Space: O(M)
        # M = length of the encoded string
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res
