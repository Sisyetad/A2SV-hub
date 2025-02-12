# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

class Solution: 
    def selectionSort(self, arr):
        #code here
        n = len(arr)
        i = 0
        while i < n:
            min_index = i
            j = i
            while j < n:
                if arr[j] < arr[min_index]:
                    min_index = j
                j += 1
            arr[min_index],arr[i] = arr[i],arr[min_index]
            i += 1
        return arr
