class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        s = []
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + nums[i] == 0:
                    if [nums[i], nums[l], nums[r]] not in s:
                        s.append([nums[i], nums[l], nums[r]])
                    else:
                        l += 1
                        r -= 1
                    
                    
                elif nums[l] + nums[r] + nums[i] > 0:
                    if r-1 != l:
                        r -= 1
                        continue
                    else:
                        break
                elif nums[l] + nums[r] + nums[i] < 0:
                    if l+1 != r:
                        l += 1
                        continue
                    else:
                        break
                
        return list(s)
                




        