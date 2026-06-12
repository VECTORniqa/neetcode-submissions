class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0

        for i in range(len(heights)):
            for j in range(i, len(heights)):
                
                breadth = j - i
                if heights[i] > heights[j]:
                    currentArea = heights[j] * breadth
                else:
                    currentArea = heights[i] * breadth
            
                if currentArea > maxArea:
                    maxArea = currentArea
        
        return maxArea
        

                
        



        

        
        