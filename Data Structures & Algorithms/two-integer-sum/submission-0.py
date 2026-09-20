class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}

        for index, number in enumerate(nums):
            complement = target - number
            if complement in dic:
                return [dic[complement], index]
            dic[number] = index
        
        return []