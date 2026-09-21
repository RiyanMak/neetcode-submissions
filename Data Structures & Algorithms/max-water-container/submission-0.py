class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        currentStore = 0
        maxStore = 0

        while l < r:
            currentWidth = r - l
            currentHeight = min(heights[l], heights[r])
            currentArea = currentWidth * currentHeight
            maxStore = max(maxStore, currentArea)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxStore
        






            

        