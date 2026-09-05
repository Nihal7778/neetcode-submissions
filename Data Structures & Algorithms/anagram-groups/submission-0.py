class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for word in strs:
            count = [0]*26


            for char in word:
                count[ord(char)-ord('a')]+=1

            key = tuple(count)


            if key in hashmap:
                hashmap[key].append(word)
            else:
                hashmap[key]=[word]

        return list(hashmap.values())



           