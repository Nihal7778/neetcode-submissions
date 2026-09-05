class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0

        write = 0

        while i < len(chars):
            curr = chars[i]

            j = i+1

            count = 1

            while j<len(chars) and chars[j]==curr:
                count+=1
                j+=1

            chars[write] = curr
            write+=1

            if count>1:
                for digit in str(count):
                    chars[write]=digit
                    write+=1

            i=j

        return write
        