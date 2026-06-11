class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = sorted(set(nums))
        maxLength = 1
        currentLength = 1

        if len(nums) == 0:
            return 0

        for i in range(0, len(nums)-1):
            if nums[i] + 1 == nums[i + 1]:
                currentLength += 1
                if currentLength > maxLength:
                    maxLength = currentLength
            else:
                currentLength = 1
                continue

        return maxLength
            

            
        
        

        