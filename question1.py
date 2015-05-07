def findthethrees(m):
    sum = 0
    for p in m:
        if(p % 3 == 0):
            sum = sum + p
    return sum

l = []
print ("Write stop in order to stop the program")
n = (input("Give me a number: "))
while (n!="stop"):
    l+= [int(n)]
    n = (input("Give me another number: "))
print(findthethrees(l))
