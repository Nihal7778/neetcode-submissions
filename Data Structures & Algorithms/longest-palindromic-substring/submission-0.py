class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlength = 0

        result = ""


        def expand(left,right):
            nonlocal maxlength
            nonlocal result

            while left>=0 and right<len(s) and s[left]==s[right]:
                curr_length = right-left+1

                if curr_length>maxlength:
                    maxlength = curr_length
                    result = s[left:right+1]

                left-=1

                right+=1

        for i in range(len(s)):
            expand(i,i)

            expand(i,i+1)


        return result
            
        