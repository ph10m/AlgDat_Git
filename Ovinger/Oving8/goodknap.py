def memoize(f):
    """ Memoization decorator for functions taking one or more arguments. """
    class memodict(dict):
        def __init__(self, f):
            self.f = f
        def __call__(self, *args):
            return self[args]
        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)

# @memoize
# def fib(i):
    # if i < 2: return 1
    # return fib(i-1) + fib(i-2)
    
# print(fib(50))
    
def unbound_knap(w, v, c): # Weights, values and capacity
    @memoize # m is memoized
    def m(r): # Max val. w/remaining cap. r
        if r == 0: return 0 # No capacity? No value
        val = m(r-1) # Ignore the last cap. unit?
        for i, wi in enumerate(w): # Try every object
            if wi > r: continue # Too heavy? Ignore it
            val = max(val, v[i] + m(r-wi)) # Add value, remove weight
        return val # Max over all last objects
    return m(c) # Full capacity available 

    
coins = [1000, 500, 200, 100, 50, 20, 10, 5, 4, 1]
weights = [1000, 500, 200, 100, 50, 20, 10, 5, 4, 1]
capacity = 48

print (unbound_knap(weights, coins, capacity))