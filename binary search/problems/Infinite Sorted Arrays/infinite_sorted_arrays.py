arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
target = 10


def binary_search (arr, target, start, end):
    first = 0 
    last = end-start+1
    
    while first <= last :
        middle = (first+last)//2
        
        if target < arr[middle]:
            last = middle -1
        elif target > arr[middle]:
            first = middle+1
        elif target == arr[middle]:
            return middle
            
    return -1


start = 0 
end = 1 

while arr[end] < target:
    start = end 
    end = end*2
    
print(binary_search(arr, target, start, end))