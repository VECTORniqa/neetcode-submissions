class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0
        r = len(numbers) - 1
       
        while l < r:
            m = numbers[r] + numbers[l]
            if target > m:
                l += 1
                continue
            elif target < m:
                r -= 1
                continue
            else:
                return [l + 1, r + 1]
        return []
            


        