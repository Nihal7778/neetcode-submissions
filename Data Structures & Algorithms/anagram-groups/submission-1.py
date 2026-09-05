class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for char in strs:

            count = [0]*26

            for word in char:

                count[ord(word)-ord('a')]+=1

            key = tuple(count)

            if key in hashmap:
                hashmap[key].append(char)
            else:
                hashmap[key]=[char]

        return list(hashmap.values())


            
        
    



           