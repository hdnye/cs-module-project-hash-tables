# Your code here

cache = {}
def expensive_seq(x, y, z):
    # Your code here
    if x <= 0:
        return y + z
    if x in cache:
        return cache[x]
    if x > 0:
        first_return = expensive_seq(x-1,y+1,z)
        second_return = expensive_seq(x-2,y+2,z*2)
        third_return = expensive_seq(x-3,y+3,z*3)        
    results = tuple([first_return, second_return, third_return])    
    cache[x] = results
    return results


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))

