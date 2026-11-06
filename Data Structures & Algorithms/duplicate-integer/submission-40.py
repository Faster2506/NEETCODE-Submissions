class Solution:
    def hasDuplicate(self, arr: List[int]) -> bool:
        n = len(arr)
        i = 0
        j = 1
        found = False

        while i < n:
            if arr[i] == arr[j]:
                found = True
                j+=1
                break

            i+=1

        return found