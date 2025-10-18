def climb(x):
    # keep climbing until we've found a summit
    summit = False

    # edit here
    while not summit:
        summit = True
        for x_new in range(max(0, x-5), min(99, x+5)):
            if h[x_new] > h[x]:
                x = x_new         # here is higher, go here 
                summit = False    # and keep going
    return x
