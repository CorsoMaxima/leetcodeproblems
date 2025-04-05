# leetcode, april 5th
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        numberLength = len(nums)
        if numberLength % 2 != 0:
            return False
        
        for szám in nums: 
            if nums.count(szám) % 2 != 0:
                return False

            if nums.count(szám) < 2:
                return False
        else:
            return True
