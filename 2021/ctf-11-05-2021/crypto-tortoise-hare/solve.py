def find_collision(h):
    x = 'test'
    tortoise = h(x)
    hare = h(h(x))
    while tortoise != hare:
        tortoise = h(tortoise) 
        hare = h(h(hare))
    tortoise = x
    while h(tortoise) != h(hare):
        tortoise = h(tortoise) 
        hare = h(hare)
    return tortoise, hare

# prints a pair of strings whose hash values will collide
print(find_collision(lambda x: str(hash(x) % 2**48)))
