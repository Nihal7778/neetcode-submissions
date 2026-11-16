class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}

        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1

   
        for num,val in hashmap.items():
            if val>1:
                return True

        return False

        