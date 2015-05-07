def theproduct(lists2,lists3):
    z = 0
    for (a,b) in zip(lists2,lists3):
        z = z + (a*b)
    return z

lists1=[1,2,3,4,5]
lists2=[1,2,3,4]
lists3=[2,4,5,6]
print(theproduct(lists2,lists3))
