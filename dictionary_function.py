def balaji():
    return "my bank balance is"

test_dct={"fname":balaji,"age":50,"address":"salem"}     #balaji is a function 
print("the original dictionary is:",test_dct)
print("the original dictionary is:",str(test_dct))
print(type((test_dct)))
print(type(str(test_dct)))

res=test_dct['fname']() #fname is key ,balaji  calls the function and returns value is stored in res
print("the required call result:",str(res)) 