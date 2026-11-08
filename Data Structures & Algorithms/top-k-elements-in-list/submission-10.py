class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # STEP 1: Count frequency of each number
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # STEP 2: Create buckets
        # Maximum possible frequency is len(nums)
        buckets = [[] for i in range(len(nums) + 1)]

        # STEP 3: Place numbers into their frequency buckets
        for num in freq:

            frequency = freq[num]

            buckets[frequency].append(num)

        # STEP 4: Collect k most frequent elements
        result = []

        # Start from highest frequency
        i = len(buckets) - 1
        while i >= 0:
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
            i -= 1
        return result