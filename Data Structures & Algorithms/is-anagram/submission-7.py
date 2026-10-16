class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i, char in enumerate(s):
            countS[char] = countS.get(char, 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

        return countS == countT
        
