def interpolation_error_bound(M, a, b, n):
    """
    Calculate the upper bound of the interpolation error using the theorem.
    
    :param M: Maximum of the (n+1)th derivative of f(x)
    :param a: Start of the interval [a, b]
    :param b: End of the interval [a, b]
    :param n: Degree of the interpolation polynomial
    :return: Upper bound of the error
    """
    # Length of the interval
    interval_length = b - a
    
    # Calculate the error bound
    error_bound = (M / (4 * (n + 1))) * (interval_length / n) ** (n + 1)
    return error_bound

# Example usage:
M = 1  # Assume maximum value of the (n+1)th derivative is 1
a, b = 0, 1  # Interval [a, b]
n = 5  # Degree of the polynomial

error = interpolation_error_bound(M, a, b, n)
print(f"Interpolation error bound: {error}")
