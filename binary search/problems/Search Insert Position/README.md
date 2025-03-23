# **Search Insert Position - LeetCode 35**  

## **Problem Link:**  
[LeetCode 35 - Search Insert Position](https://leetcode.com/problems/search-insert-position/description/)  

## **Asked In:**  
- Microsoft  
- Amazon  
- Google  

## **Topic:**  
- **Binary Search**  

---

## **Prerequisites**  
- Understanding of **Binary Search**  
- Concept of **midpoint calculation** to optimize search in sorted arrays  

---

## **Problem Statement**  
Given a **sorted array** and a **target value**, return the **index** if the target is found.  
If not, return the **index where it would be inserted** in order while maintaining the sorted order.  

### **Example**  

#### **Example 1**  
```python
Input: nums = [1,3,5,6], target = 5
Output: 2
```


## **Intuition**  

### **Why Binary Search?**  
Since the array is **sorted**, the best approach is **Binary Search**, which reduces time complexity to **O(log n)** instead of **O(n)** for linear search.  

---

## **Approach**  

### **Initialize Two Pointers:**  
- `first = 0` (start of the array)  
- `last = len(nums) - 1` (end of the array)  

### **Perform Binary Search:**  
1. Find `middle = (first + last) // 2`  
2. If `nums[middle] == target`, return `middle`  
3. If `target < nums[middle]`, move `last = middle - 1`  
4. If `target > nums[middle]`, move `first = middle + 1`  

### **If Target Is Not Found:**  
- The correct position to insert is `first`, since it determines the lowest index where the target can be placed while maintaining order.  
