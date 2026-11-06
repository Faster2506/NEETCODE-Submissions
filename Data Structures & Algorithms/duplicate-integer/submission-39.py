class Solution:
    def hasDuplicate(self, arr: List[int]) -> bool:
        n = len(arr)
        i = 0
        found = False

        while i < n:
            j = 1
            if arr[i]==arr[j]:
                found = True
                break
                j+=1

            i+=1

        return found