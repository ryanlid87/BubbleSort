#Bubble Sort
# 123s < A < a
def bubsort(a):
        for i in range(len(a)):
                for x in range(0,len(a)-1):
                        if a[x] > a[x+1]:
                                a[x+1],a[x] = a[x],a[x+1]
        return a

def mergesort(a):
        if len(a)>1:
                mid = len(a)//2
                left=a[:mid]
                right=a[mid:]
                mergesort(left)
                mergesort(right)

                i=0
                j=0
                k=0
                print left,right
                while i<len(left) and j<len(right):
                        if left[i] < right[j]:
                                a[k]=left[i]
                                i=i+1
                        else:
                                a[k]=right[j]
                                j=j+1
                        k=k+1
                while i< len(left):
                        a[k]=left[i]
                        i=i+1
                        k=k+1
                while j < len(right):
                        a[k]=right[j]
                        j=j+1
                        k=k+1
                print a
