class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for i in range(min(len(str1),len(str2)),0,-1):
            if ((str1[:i]*(len(str2)//i) == str2) and (str2[:i]*(len(str1)//i)==str1)):
                return str1[:i]
        return ""