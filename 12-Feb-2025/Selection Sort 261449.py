# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

class Solution: 
    def selectionSort(self, arr):
        #code here
        n = len(arr)
        i = 0
        while i  <  n:
            max_index  =  i
            j  =  i
            while j < n:
                if arr[j] < arr[max_index]:
                    arr[max_index],arr[j] = arr[j],arr[max_index]
                j += 1
            i += 1
        return arr
