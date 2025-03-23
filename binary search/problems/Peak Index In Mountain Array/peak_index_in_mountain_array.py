def peakIndexInMountainArray( arr: list[int]) -> int:
    first = 0
    last = len(arr)-1
    while first <= last:
        middle = (first+last)//2
        if arr[middle] >  arr[middle-1] and arr[middle]> arr[middle+1]:
            return middle
        elif arr[middle] < arr[middle+1]:
            first = middle+1
        elif arr[middle] < arr[middle-1]:
            last = middle-1
    return -1

array = [0, 1, 0]
print(peakIndexInMountainArray(array)) # 1