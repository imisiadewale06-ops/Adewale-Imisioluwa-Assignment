#insert the following value into a dynamic array of capacity 2: 10,20,30,40,50
class DynamicArray:
    def __init__(self, capacity=2):
        self.capacity = capacity   # Total space
        self.size = 0              # Number of elements in array
        self.array = [None] * self.capacity  # Underlying fixed-size array

    def insert(self, value):
        # Check if array is full
        if self.size == self.capacity:
            self.resize()

        # Insert the value
        self.array[self.size] = value
        self.size += 1

    def resize(self):
        # Double the capacity
        self.capacity *= 2
        new_array = [None] * self.capacity

        # Copy old elements
        for i in range(self.size):
            new_array[i] = self.array[i]

        self.array = new_array

    def __str__(self):
        # Print only the filled elements
        return str(self.array[:self.size])

# Example usage
arr = DynamicArray()
for value in [10, 20, 30, 40, 50]:
    arr.insert(value)
    print(f"Array: {arr}, Size: {arr.size}, Capacity: {arr.capacity}")

