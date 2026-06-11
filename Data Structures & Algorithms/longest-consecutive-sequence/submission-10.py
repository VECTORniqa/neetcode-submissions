class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for i in range(len(nums)):
            if nums[i] - 1 not in s:
                next_num = nums[i] + 1
                max_length = 1
                while next_num in nums:
                    max_length += 1
                    next_num += 1
                
                if max_length > longest:
                    longest = max_length
        return longest
                


        