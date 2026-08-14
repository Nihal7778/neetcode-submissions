class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs[0])


        if not strs:
            return ""


        for i in range(n):
            char = strs[0][i]

            for j in range(1,len(strs)):
                if i>=len(strs[j])or strs[j][i]!=char:
                    return strs[0][:i]

        return strs[0]


        