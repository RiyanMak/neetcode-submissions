class Solution:
    def canJump(self, nums: List[int]) -> bool:

        lastPos = 0
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i
            
        return lastPos == 0


            



