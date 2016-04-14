def bubsort(a):
        for i in range(len(a)):
                for x in range(len(a)-1,0,-1):
                        if a[x] < a[x-1]:
                                temp = a[x]
                                a[x] = a[x-1]
                                a[x-1] = temp
        return a

print bubsort(a)
