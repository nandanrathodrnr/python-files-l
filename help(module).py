p=["hai"]                #address is same for  both p and a
a={"hai":1}
print(type(a))             
print("ud of p=",id(p))   #id represents address of variable
print("ud of a=",id(a))                             
print(p is a)
print(p==a)  


'''
p=[10,20,30]
a=[10,20,30]
print("ud of p=",id(p))
print("ud of a=",id(a))
print(p is a)  it compares both value and datatype
print(p==a)
 we get true
        true
        because p and a are having a differnt address
'''