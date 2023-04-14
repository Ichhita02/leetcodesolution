# leetcodesolution
 r=[]
 for i in range(0,len(nums1)):
     for j in range(0,len(nums2)):
            flag=1
            info=0
            if nums1[i]==nums2[j]:
                info=nums2[j]
                for k in range(j+1,len(nums2)):
                      if nums2[k]>info:
                           r.append(nums2[k])
                           flag=0
                           break
                 if flag==1:
                     r.append(-1)
return r
