class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False

        hashSet = collections.defaultdict(int)

        for i in range(0,len(s)):
            hashSet[s[i]] += 1
            hashSet[t[i]] -= 1
        
        for i in hashSet:
            if hashSet[i] != 0:
                return False
        
        return True