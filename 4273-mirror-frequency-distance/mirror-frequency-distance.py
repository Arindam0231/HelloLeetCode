class Solution:
    def mirrorFrequency(self, s: str) -> int:
        letter = "abcdefghijklmnopqrstuvwxyz"
        number = "0123456789"
        freq = {}
        a = set()
        for c in s:
            freq[c.lower()] = freq.get(c.lower(),0)+1
            a.add(c)
        return_sum=0
        # print(freq)
        res = ""
        for c in a:
            if c in number:
                index = ord(c) - ord("0")
                m=number[(-index-1)]
            else:
                index= ord(c.lower())-ord("a")
                m=letter[(-index-1)]
            if (m not in res) and (c not in res):
                # print(m,c)
                return_sum +=abs(freq.get(m,0)-freq.get(c,0))
                res+= (m+c)
        return(return_sum)