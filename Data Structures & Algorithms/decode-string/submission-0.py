class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr = ""
        count = 0

        for ch in s:
            if ch.isdigit():
                count = count*10+int(ch)

            elif ch.isalpha():
                curr+=ch

            elif ch == '[':
                stack.append((curr,count))

                curr = ""
                count = 0

            else: 
                prev_string,repeat = stack.pop()

                curr = prev_string+curr*repeat

        return curr


        