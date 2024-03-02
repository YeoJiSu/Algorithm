class MergeSort:
    def recursiveCode(self, arr):
        if len(arr)>1:
            mid = len(arr)//2
            left = arr[:mid]
            right = arr[mid:]
            self.recursiveCode(left)
            self.recursiveCode(right)
            
            i, j, k = 0, 0, 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i+=1
                else:
                    arr[k] = right[j]
                    j+=1
                k+=1
            while i < len(left):
                arr[k] = left[i]
                i+=1
                k+=1
            while j < len(right):
                arr[k] = right[j]
                j+=1
                k+=1
            
arr = [12,11,13,4,2,5,6]
MergeSort().recursiveCode(arr)
print(arr)