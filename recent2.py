#Write a fibonacci series of 8
def fibonacci(n):
    fib_series = [0, 1]  # starting two numbers
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

# Fibonacci series of 8 numbers
fib_8 = fibonacci(8)
print("Fibonacci series of 8 numbers:", fib_8)
