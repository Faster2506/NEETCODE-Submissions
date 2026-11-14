class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        pre, post = 1, 1

        for i in range(0, len(nums)):
            res[i] = pre
            pre = nums[i] * pre

            i+=1

        for i in range(len(nums)-1, -1,-1):
            res[i] = res[i] * post
            post = post * nums[i]
            i-=1
            
        return res

