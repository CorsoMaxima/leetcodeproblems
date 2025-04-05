# leetcode, april 5th

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        unitedPrefix = ""
        pointer = 0
        lastSavedPrefix = ""
        caseNumber = 0
        shouldRun = True

        while shouldRun:
            for szöveg in strs:
                if pointer > len(szöveg)-1:
                    shouldRun = False
                    break

                if lastSavedPrefix == "":
                    lastSavedPrefix = szöveg[pointer]
                    caseNumber += 1
                    continue

                if szöveg[pointer] == lastSavedPrefix:
                    caseNumber += 1
                else:
                    shouldRun = False
                    break
                
                if caseNumber > len(strs):
                    unitedPrefix += lastSavedPrefix
                    lastSavedPrefix = ""
                    caseNumber = 0
                    pointer += 1
                    break
        
        return unitedPrefix

asd = [34]
coun
