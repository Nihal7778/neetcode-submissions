class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding= ""

        for word in strs:
            encoding += str(len(word))+ '#' + word

        return encoding
        

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
      

        while i < len(s):
            j = i
        

            while s[j]!='#':
                j+=1

            length = int(s[i:j])

            word_start = j+1

            word_end = word_start+length

            result.append(s[word_start:word_end])

            i = word_end

        return result 



        