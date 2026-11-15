class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            if num in hashmap:
                hashmap[num]+=1

            else:
                hashmap[num]=1

        count = [[] for _ in range(len(nums)+1)]

        for num,freq in hashmap.items():
            count[freq].append(num)

        
        result = []


        for i in range(len(count)-1,0,-1):
            for num in count[i]:
                result.append(num)

            if len(result)==k:
                return result

        return result
        
        