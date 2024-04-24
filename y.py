y=[]
n=int(input("enter the list size"))
for i in range (0,n):
    ele=int(input('enter the elements'))
    y.append(ele)
    print(y) 
    
s=[]
n=int(input("enter the list size"))
for i in range (0,n):
    ele=int(input('enter the elements'))
    s.append(ele)
    print(s)
    
    for i in y:
        for j in s:
            if i==j:
                print(i)