class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}

        for ch in strs:
            key = "".join(sorted(ch))
            
            if key not in freq:
                freq[key] = []

            freq[key].append(ch)

        return list(freq.values())