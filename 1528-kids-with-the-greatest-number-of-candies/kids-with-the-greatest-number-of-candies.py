class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        answer=[0]*len(candies)
        m = max(candies)
        for i in range(len(candies)):
            answer[i]=((candies[i]+extraCandies)>=m)
        return answer