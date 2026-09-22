class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        right_max = -1

        for i in range(n-1,-1,-1):
            current_val = arr[i]

            arr[i] = right_max

            if current_val > right_max:
                right_max = current_val

        return arr

            
             


       
            

        