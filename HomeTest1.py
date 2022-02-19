import random

def array_gen(n):
    array3 = {}
    for I in range(n):
        array = []
        while True:
            ma = random.randint(1,50)
            if array3.setdefault(ma) == None:
                break
        for J in range (ma):
            array.append(random.randint(1,50))
        array3.update({ ma: array})

    switch = False
    result = []
    for v in array3.values():
        if switch:
            v.sort()
        else:
            v.sort(reverse=True)
        switch = not switch
        result.append(v)

    return result


n = random.randint(1,50)
print (array_gen(n))