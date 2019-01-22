array = [
    [1,2],
    [2,1],
    [-1, -2],
    [1, -2],
    [-2, 1],
    [-1, 2],
    [2, -1],
    [1, 1],
    [0, 0],
    [-1, -1]
    ]

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def test(array):
    result = []
    index = 0
    for x in array:
        a = x[0]
        b = x[1]
        if (sub(a, b) === 0):
            if(sub(b, a)):
                result[index] = 0
            
