from re import L


l = [(2,5),(1,2),(4,4),(2,3),(2,1)]
i = 0
print("The unsorted element is:", l)
for i in range(len(l)):
    for j in range (i+1,len(l)):
      if (l[i]>l[j]):
        temp = l[i]
        l[i] = l[j]
        l[j] = temp
     
print("The sorted element of l are:",l)    
     
        






