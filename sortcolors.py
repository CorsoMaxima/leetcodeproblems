# 19th april
# sort colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        R = 0
        W = 0
        B = 0

        for num in nums:
            if num == 0:
                R += 1
            elif num == 1:
                W += 1
            elif num == 2:
                B += 1
        
        nums[:R] = [0] * R
        nums[R:R+W] = [1] * W
        nums[R+W:] = [2] * B
