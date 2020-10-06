# def fib(n):  # O(2^n) 
    # if n <= 1:
        # return n
        # 2 recursive f() calls create the exponential big O factor 
        # by repeating the f() calls w/o solving or storing anything
    # return fib(n-1) + fib(n-2)

print(fib(100)) # <--will run for a really long time if it doesn't break your computer first

# add memoization & caching

cache = {}
# so now each time the recursion is run, it's O(1)
def fib(n):
    if n <= 1: 
        return n
    if n in cache: 
        return cache[n]
    result = fib(n-1) + fib(n-2) # <-- except here where the f() is still called 2x so O(n)
                # because # of constants drop when calculating n for big O
    cache[n] = result

    return result
    
