class Solution:
    def hasDuplicate(self, arr: List[int]) -> bool:
        seen = set()

        duplicate = False

        for num in arr:
            if num in seen:
                duplicate = True
                break

            seen.add(num)

        return duplicate