class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n =len(nums)
        hashmap = {}
        left = 0
        right = 1

        for i in range(n):
            if nums[i] in hashmap:
                if i - hashmap[nums[i]]<=k:
                    return True

            hashmap[nums[i]]=i

        return False
            








     



        