#Bubble Sort
# 123s < A < a
def bubsort(a):
        for i in range(len(a)):
                for x in range(0,len(a)-1):
                        if a[x] > a[x+1]:
                                a[x+1],a[x] = a[x],a[x+1]
        return a

if __name__=="__main__":
        from random import randint
        a = []
        for x in range(0,10):
                a.append(randint(0,100))
        print a
        print bubsort(a)

