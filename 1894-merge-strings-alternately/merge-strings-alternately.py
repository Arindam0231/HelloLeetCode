class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left = 0
        right = 0 
        answer = ""
        while(left<len(word1) and right<len(word2)):
            answer+= word1[left]
            answer+= word2[right]
            left+=1
            right+=1
        while(left<len(word1)):
            answer+=word1[left]
            left+=1
        while(right<len(word2)):
            answer+=word2[right]
            right+=1
        return answer