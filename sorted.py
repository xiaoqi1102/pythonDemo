print sorted([23,212,5,2345,99,57])

def revered_cmp(x,y):
    if x > y:
        return -1
    if x<y:
        return 1
    return 0

print sorted([44,12,445,99,233],revered_cmp)
