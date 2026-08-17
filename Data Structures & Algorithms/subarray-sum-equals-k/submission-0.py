class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n =len(nums)
        hashmap = {0:1}
        
        count = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum+=num

            needed = prefix_sum - k

            if needed in hashmap:
                count+= hashmap[needed]


            if prefix_sum in hashmap:
                hashmap[prefix_sum]+=1
            else:
                hashmap[prefix_sum]=1

        return count        
            
        


            
            

      

        