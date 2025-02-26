# TO-DO: complete the helpe function below to merge 2 sorted arrays
import math

def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    if len(arrA) < len(arrB):
        hold = arrA
        arrA = arrB
        arrB = hold
    for i in range(elements):
        if not not arrA and (not arrB or arrA[0] < arrB[0]):
            merged_arr[i] = arrA[0]
            arrA.pop(0)
        else:
            merged_arr[i] = arrB[0]
            arrB.pop(0)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len (arr) <= 1:
        return arr
    if len(arr) == 2:
        return merge([arr[0]], [arr[1]])
    firtHalf = arr[0: math.ceil(len(arr) // 2)]
    secondHalf = arr[math.ceil(len(arr) // 2):]

    return merge(merge_sort(firtHalf), merge_sort(secondHalf))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
