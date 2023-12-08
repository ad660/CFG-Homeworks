def num_in_seq(n):
    if n == 1:
        return 8
    else:
        return num_in_seq(n - 1) + 7

# Test cases
print(num_in_seq(1))
print(num_in_seq(5))
print(num_in_seq(10))
