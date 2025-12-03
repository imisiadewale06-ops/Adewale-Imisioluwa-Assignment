#Perform a linear search on an array with value 2,5,7,10,14,20. Target is 10
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return index if found
    return -1  # Return -1 if not found

arr = [2, 5, 7, 10, 14, 20]
target = 10

index = linear_search(arr, target)
if index != -1:
    print(f"Target {target} found at index {index}.")
else:
    print(f"Target {target} not found in the array.")
