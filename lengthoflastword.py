# lengthOfLastWord
# leetcode, mar 29th
# screenshot:
# https://cdn.discordapp.com/attachments/729627416867110922/1355628721465200832/image.png?ex=67e99f21&is=67e84da1&hm=9c61a7a29a7c866bf30ec080db499001bce648314ebf6e4c977f0066659873f8&
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        space = s.split(" ")
        hashmap = []

        for szó in space:
            if szó == "": continue
            hashmap.append(szó)

        return len(hashmap[-1])
