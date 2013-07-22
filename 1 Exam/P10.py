def numPens(n):
    """
    n is a non-negative integer

    Returns True if some non-negative integer combination of 5, 8 and 24 equals n
    Otherwise returns False.
    """
    for a in range(n/5+1):
        for b in range(n/8+1):
            for c in range(n/24+1):
                if a*5+b*8+c*24 == n:
                    print a
                    print b
                    print c
                    return True
    return False
