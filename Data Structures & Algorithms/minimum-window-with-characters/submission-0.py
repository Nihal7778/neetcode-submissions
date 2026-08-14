class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""


        m = len(s)
        n = len(t)

        left = 0

        count = 0

        hashmap_n={}

        for char in t:
            if char in hashmap_n:
                hashmap_n[char]+=1
            else:
                hashmap_n[char]=1

        hashmap_m={}
        required = len(hashmap_n)

        min_length=float("inf")

        for right in range(m):

            if s[right] in hashmap_m:
                hashmap_m[s[right]] += 1
            else:
                hashmap_m[s[right]] = 1


            char = s[right]

            if char in hashmap_n and hashmap_m[char] == hashmap_n[char]:
                count+=1




            while count == required:

                curr_length = right - left + 1

                if curr_length<min_length:
                    min_length=curr_length
                    start=left

                left_char=s[left]
                hashmap_m[left_char]-=1

                if left_char in hashmap_n and hashmap_m[left_char]<hashmap_n[left_char]:
                    count-=1

                left+=1

        if min_length == float("inf"):
            return ""

        result = ""

        i=start

        while i<start+min_length:
            result+=s[i]
            i+=1

        return result









            



                



        



        

        