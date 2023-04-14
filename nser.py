l=[]
s=[]
for i in range(n-1,-1,-1):
      if len(s)==0:
       if (len(s)==0):
           l.append(-1)
        elif len(s)>0 and s[-1]<arr[i]:
        elif (len(s)>0 and s[-1]<arr[i]):
            l.append(s[-1])
        elif len(s)>0 and s[-1]>=arr[i]:
            while len(s)!=0 and s[-1]>=arr[i]:
        elif (len(s)>0 and s[-1]>=arr[i]):
            while (len(s)!=0 and s[-1]>=arr[i]):
                s.pop(-1)
            if len(s)==0:
            if (len(s)==0):
                l.append(-1)
            else:
                l.append(s[-1])
