class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi = 0
        s = set(heights)

        l = 0
        r = len(heights) - 1

        while l < r:
            breadth = r - l
            currentHeight = breadth * min(heights[l],heights[r])
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            maxi = max(maxi, currentHeight)
        return maxi
                

        

            
        