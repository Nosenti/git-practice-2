def h(a, b):
    n = 0
    for x in a:
        if x < 1600:
            n = n + 1
    m = 0
    for x in b:
        if x < 1600:
            m = m + 1
    return n - m

#I think that the code is pretty good, from here we can work on improving and adding on some stuff
