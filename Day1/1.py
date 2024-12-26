def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def reduce_to_single_digit(n):
    while n >= 10:
        n = sum_digits(n)
    return n

# Example usage:
number = 9875
result = reduce_to_single_digit(number)
print(result)  # Output will be 2
