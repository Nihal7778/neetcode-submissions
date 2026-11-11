class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        def solve(low,high):
            if low == high:
                return nums[low]


            mid = (low+high)//2

            left_sum = solve(low,mid)
            right_sum = solve(mid+1,high)

            curr_sum = 0

            left_cross_sum = float('-inf')

            for i in range(mid,low-1,-1):
                curr_sum+=nums[i]
                left_cross_sum=max(left_cross_sum,curr_sum)



            curr_sum = 0
            right_cross_sum = float('-inf')

            for i in range(mid+1,high+1):
                curr_sum+=nums[i]
                right_cross_sum=max(right_cross_sum,curr_sum)

            cross_sum = left_cross_sum+right_cross_sum

            return max(left_sum,right_sum,cross_sum)

        return solve(0,len(nums)-1)