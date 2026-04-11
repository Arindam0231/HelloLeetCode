class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        a = 0
        mp = {}
        limit = int(n ** (1/3)) + 1
        for a in range(limit):
            a3 =a**3
            if a3>n:
                break
            for b in range(a):
                b3= b**3
                if a3+ b3 > n:
                    break
                mp[a3+b3] = mp.get(a3+b3,0)+1
        result = []
        for i, j in mp.items():
            if j>1:
                result.append(i)
        return sorted(result)