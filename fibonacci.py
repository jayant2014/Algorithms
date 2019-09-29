def get_nthfib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return get_nthfib(n - 1) + get_nthfib( n - 2)

nth_fib = get_nthfib(5)
print('Nth Fibonacci is : %d' %(nth_fib))
