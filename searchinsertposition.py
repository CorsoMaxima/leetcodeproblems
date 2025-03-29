# search insert position
# leetcode, mar 29th
# screenshot:
# https://cdn.discordapp.com/attachments/729627416867110922/1355625954919186693/image.png?ex=67e99c8d&is=67e84b0d&hm=bd94a3292e98d585ccba56a13336110ef3ff16a3edf5b078b6020c9e704f3eb8&

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        lastnumber = 0
        for szám in nums:
            if min(nums) > target:
                return 0

            if max(nums) < target:
                return len(nums)

            if target < szám:
                return index

            if target == szám:
                return index
            
            lastnumber = szám
            index += 1
