def power(base, exponent):
    """Return base raised to the power of exponent (exponent >= 0)."""
    result = 1
    for _ in range(exponent):
        result *= base
    return result


a = 2
n = 4
value = power(a, n)

print(f"{a} to the power of {n} is {value}")
