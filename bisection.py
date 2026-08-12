def square_root_bisection(n_to_sqrt:float, tolerance:float = 0.01, max_iter:int = 5):
    if n_to_sqrt < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    if n_to_sqrt == 0 or n_to_sqrt == 1:
        print(f"The square root of {n_to_sqrt} is {n_to_sqrt}")
        return n_to_sqrt

    lo:float = 0.0
    hi:float = max(n_to_sqrt, 1.0)
    iter_count:int = 0
    sqrt_of_n:float = None

    while iter_count < max_iter:
        mid:float = (lo + hi)/2
        if hi - lo <= tolerance:
            sqrt_of_n = mid
            break
        elif pow(mid,2) < n_to_sqrt:
            lo = mid
        else:
            hi = mid
        iter_count += 1
    
    if sqrt_of_n is None:
        print(f"Failed to converge within {max_iter} iterations")
    else:
        print(f"The square root of {n_to_sqrt} is approximately {sqrt_of_n}")
    return sqrt_of_n

print(square_root_bisection(0.001, 1e-7, 50))