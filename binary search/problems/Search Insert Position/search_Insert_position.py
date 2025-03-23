# 1, 4, 10 
def searchInsert(nums: list[int], target: int) -> int:
    first = 0
    last = len(nums)-1
    res = -1
    while first <= last :
        middle = (first+last)//2
        if target == nums[middle]:
            res = middle
            return res
        elif target < nums[middle]:
            last = middle-1
        elif target > nums[middle]:
            first = middle+1
        
        print(first, last)
        print("middle", middle)
    if res == -1:
        if nums[middle]< target :
            res = middle+1
        else:
            res = middle 
    return res

print(searchInsert([1,3,5,6], 2))