class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        import collections
        hashMap = collections.defaultdict(list)

        for i in strs:            
            hashMap["".join(sorted(i))].append(i)
            
        result = []
        for j in hashMap.items():
            result.append(j[1])
        
        return result