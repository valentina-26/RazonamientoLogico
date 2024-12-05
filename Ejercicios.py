def findLongestSubsequence(arr):
    n = len(arr)
    
    # Sort the array in ascending order
    arr.sort()
    

    max_length = 0
    
    # Iterate through the array
    for i in range(n):
        current_length = 1
        

        sum_diff = 0
        
        # Iterate through the remaining elements
        for j in range(i + 1, n):
            # Calculate the difference between adjacent elements
            diff = arr[j] - arr[j - 1]
            
            # If the sum of differences is even, increment the current length
            if (sum_diff + diff) % 2 == 0:
                current_length += 1
                sum_diff += diff
        
        # Update the maximum length if the current length is greater
        max_length = max(max_length, current_length)
    
    return max_length


arr = input("Enter the array of integers (separated by spaces): ").split()
arr = [int(x) for x in arr]


print(f"The length of the longest valid subsequence is: {findLongestSubsequence(arr)}")