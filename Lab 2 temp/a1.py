def calculate_square(x):
    return x ** 2

cache = {}

def cached_square(x):
    if x in cache:
        return cache[x]
    else:
        result = calculate_square(x)
        cache[x] = result
        return result

# Example usage
print(cached_square(2))  
print(cached_square(2))  
print(cached_square(4))  
print(cached_square(4))  