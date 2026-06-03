def exam(str1):
    new=""
    count=0
    for i in str1:   
        #  i=G,e,n  COUNT=0,1,2,3   new="","g","g0","g0n" ,"g0n2","g0n2Ge" str1="GenX"
        if count%2!=0:
            new=new+str(count-1) 
        else:
            new=new+i.lower()
        count+=1
    new=new+str1[:2]  
    print("the new string is:",new)
exam("GenX")
         
