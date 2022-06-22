l1 = [8,19,148,4]
l2 = [9,1,33,83]
l3 = []
for i1 in l1:
    for i2 in l2:
        result = i1*i2
        l3.append(result)
        print(str(i1)+' __ '+str(i2))
print(l3)
