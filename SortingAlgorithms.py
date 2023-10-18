# For quicksort, we choose any element as a pivot. We compare the pivot with
# all elements of the array and place it at an index where the left side has 
# elements lesser and the right side has elements greater than the pivot. This
# is a process of putting the pivot at its sorted position. 
# For left and right sides, we keep on performing this method recursively.


def partition(array, start, end):

    # In our case, we choose last element as pivot. We can choose any element.
    pivot = array[end]

    # i is the index of the pivot. We initialize this as start - 1.
    # We will return this position of the pivot
    
    i = start - 1

    # We iterate over the array.
    # If any element is lesser than pivot, we increment the index position, 
    # Now since we want all smaller elements to be on the left side of the pivot, we will # swap array[j] and array[i] (i has been incremented). i + 1 is our partition index. 


    # Once we are done will all elements, we will swap array[i + 1] with the last element, that we orignally chose as pivot. i + 1 is the sorted index for pivot

    for j in range(start, end):

        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[end] = array[end], array[i + 1] 

    return i + 1


def quickSort(array, start, end):

    if start < end:
        
        # Put pivot at sorted position. Partition returns index value
        p = partition(array, start, end)

        # Do for right side
        quickSort(array, start, p - 1)

        # Do for left side
        quickSort(array, p + 1, end)
        

# For mergeSort, we use recursion. We keep on splitting the array into smaller arrays, 
# and then compare the two arrays. We go through each element of the array and combine 
# /merge the subarrays.



def mergeSort(array):

    # We separate until the array is on length 1
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        # Recursive calls
        mergeSort(left)
        mergeSort(right)

        # For the first time, length of array left and right is 1
        
        # We define 3 vars, one for indexing left, one for indexing right and for indexing the new subarray

        i = j = k = 0

        print(left, right)

        # We compare each element of array left and right.
        while i < len(left) and j < len(right):

            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1

            k += 1

        # If i is still left, we add all elements from i to array. We do the
        # same thing for right
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

array = [10, 2, 3, 4, 5, 6 ,6]

quickSort(array, 0, len(array) - 1)
print("Array after quicksort : ", array)


array = [10,2,3,4,5,6,6,6,7,8,2,3,4,5,6,7,8,8]

mergeSort(array)
print("Array after quicksort : ", array)
