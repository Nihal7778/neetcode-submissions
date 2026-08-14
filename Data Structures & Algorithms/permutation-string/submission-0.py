class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False


        hashmap_s1 = {}


        for char in s1:
            if char in hashmap_s1:
                hashmap_s1[char]+=1
            else:
                hashmap_s1[char] =1
                

        window_s2 = {}

        left = 0


        for right in range(len(s2)):
            char = s2[right]

            if char in window_s2:
                window_s2[char]+=1

            else:
                window_s2[char]=1

            window_length = right-left+1

            if window_length >len(s1):
                left_char = s2[left]

                window_s2[left_char]-=1


                if window_s2[left_char]==0:
                    del window_s2[left_char]

                left+=1

            if window_s2 == hashmap_s1:
                return True

        return False






        


    
        