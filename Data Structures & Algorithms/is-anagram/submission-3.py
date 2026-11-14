class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_1 = {}
        hashmap_2 = {}

        for char in s:
            if char in hashmap_1:
                hashmap_1[char]+=1

            else:
                hashmap_1[char]=1


        for string in t:
            if string in hashmap_2:
                hashmap_2[string]+=1

            else:
                hashmap_2[string]=1


        if hashmap_1 == hashmap_2:
            return True


        return False
        
        
        
        