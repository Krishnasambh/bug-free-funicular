total = 0
def trirecursion(finalval):
    if finalval>0:
        total = finalval + trirecursion(finalval-1)
        print(total)
    else:
        total = 0
    return total


trirecursion(5)