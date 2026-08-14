class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n= len(nums)


        left = 0


        for i in range(n):
            if nums[i]!=val:
                nums[left]=nums[i]
                left+=1 
        return left
            
        


        
        