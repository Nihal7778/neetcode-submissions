class Solution:
    def scoreOfString(self, s: str) -> int:
        #we initialize the total score
        total_score=0

        #we iterate it up to len(s) - 1 because we access s[i+1]
        for i in range(len(s)-1):
            #ord() converts  char to  its ASCII integer value
            current_char_val = ord(s[i])
            next_char_val = ord(s[i + 1])

            #add absolute value diff to our total running value
            total_score += abs(current_char_val - next_char_val)

        return total_score

