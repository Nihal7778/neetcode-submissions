class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        max_length = 0
        seen =set()
        left = 0

        for right in range(n):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1

            seen.add(s[right])

            max_length = max(max_length,len(seen))

          

        return max_length



    
        