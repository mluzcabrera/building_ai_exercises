portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

def permutations(route, ports):
    # Base case: when there are no more ports left to add
    if not ports:
        print(' '.join([portnames[i] for i in route]))
        return

    # Recursive case: try each remaining port
    for i in range(len(ports)):
        newroute = route + [ports[i]]
        newports = ports[:i] + ports[i+1:]
        permutations(newroute, newports)
        
    # Base case: when there are no more ports left to add
    if not ports:
        print(' '.join([portnames[i] for i in route]))

# Start recursion with PAN (index 0) as the first stop
print(portnames)
permutations([0], list(range(1, len(portnames))))
