import math 

arr = [6, 7, 8, 9, 10]

target = 7

first = 0 
last = len(arr)-1
final = 0

while first <= last : 
    middle = (first + last)//2
    
    if target > arr[middle] : 
        first = middle+1
    elif target < arr[middle] :
        last = middle-1
    elif target == arr[middle]:
        final = middle
        break
		
print("Final: ", final)
	
