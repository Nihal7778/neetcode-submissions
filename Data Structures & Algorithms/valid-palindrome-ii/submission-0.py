class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        
        left = 0
        right = n-1

        def checkPalindrome(left,right):

            while left<right:
                if s[left]!=s[right]:
                    return False

                left+=1
                right-=1

            return True

        while left<right:
            if s[left] == s[right]:
                left+=1
                right-=1

            else:
                return (
                    checkPalindrome(left+1,right)
                    or
                    checkPalindrome(left,right-1)
                )

        return True
        
        