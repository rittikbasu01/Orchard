def hailstone(n):
    """Print the terms of the 'hailstone sequence' from n to 1, and
    return the length of the sequence."""
    assert n > 0
    print(n)
    return 1 if n==1 else \
           1 + hailstone(n//2 if n%2 == 0 else (3*n+1))

result = hailstone(10)
print(result)
