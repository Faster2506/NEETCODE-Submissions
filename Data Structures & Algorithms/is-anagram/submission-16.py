class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {}

        for ch in s:
            freq[ch] = freq[ch].get(ch,0) +1

        for ch in t:
            if ch not in t:
                return False

            freq -=1

            if freq[ch] <0:
                return False
        return True