class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = defaultdict(int)

        for i in nums:
            hashMap[i] += 1

        hashMapSorted = dict(sorted(hashMap.items(), key = lambda x : x[1], reverse = True))

        result = []
        for key, value in hashMapSorted.items():
            result.append(key)
            k -= 1
            if(not k):
                break

        return result


        