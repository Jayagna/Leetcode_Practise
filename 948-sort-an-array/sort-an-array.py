class Solution(object):
    def sortArray(self, nums):
        
        def mergeSort(arr, s, e):
            if s >= e:
                return

            m = (s + e) // 2
            mergeSort(arr, s, m)
            mergeSort(arr, m + 1, e)
            merge(arr, s, m, e)

        def merge(arr, s, m, e):
            temp = []
            i, j = s, m + 1

            while i <= m and j <= e:
                if arr[i] <= arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1

            while i <= m:
                temp.append(arr[i])
                i += 1

            while j <= e:
                temp.append(arr[j])
                j += 1

            for i in range(len(temp)):
                arr[s + i] = temp[i]

        mergeSort(nums, 0, len(nums) - 1)
        return nums
