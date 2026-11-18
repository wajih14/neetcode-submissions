class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = dict()
        d2 = dict()
        for c in s:
            if c in d1.keys():
                d1[c] += 1
            else:
                d1[c] = 1
        
        for c in t:
            if c in d2.keys():
                d2[c] += 1
            else:
                d2[c] = 1
            
        print(d1)
        print(d2)
        return d1 == d2
