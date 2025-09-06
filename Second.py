def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example usage:
if __name__ == "__main__":
    n = 10  # Number of Fibonacci numbers to generate
    print(fibonacci(n))