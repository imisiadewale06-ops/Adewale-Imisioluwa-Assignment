#Do a recursion to sum first 10 numbers
def sum_recursive(n):
    if n == 1:
        return 1
    else:
        return n + sum_recursive(n - 1)

# Sum of first 10 numbers
total = sum_recursive(10)
print("Sum of first 10 numbers:", total)

