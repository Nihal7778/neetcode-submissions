class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = []
        
        for ch in s:
            if ch.isalnum():
                cleaned.append(ch.lower())

        original = "".join(cleaned)
        reversed_string = original[::-1]

        return original == reversed_string

        