def nextSmallerElementToLeft(arr,n):
    l=[]
    s=[]
    for i in range(n):
        if (len(s)==0):
            l.append(-1)
        elif (len(s)>0 and s[-1]<arr[i]):
            l.append(s[-1])
        elif (len(s)>0 and s[-1]>=arr[i]):
            while (len(s)!=0 and s[-1]>=arr[i]):
                s.pop(-1)
                l.append(-1)
            else:
                l.append(s[-1])
        s.append(arr[i])
    return l
