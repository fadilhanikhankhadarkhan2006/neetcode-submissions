class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        total=1
        for i in range (len(nums)):
            total= total*nums[i]
        for i in range (len(nums)):
            if nums[i]==0:
                output[i]=-6
            else:
                output[i]= total//nums[i]
        return output