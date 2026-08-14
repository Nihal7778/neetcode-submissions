class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        longest = 1
        st = set(nums)

        for it in st:
            if it-1 not in st:
                cnt =1

                x = it

                while x+1 in st:
                    x +=1
                    cnt +=1

                longest = max(longest,cnt)

        return longest

        