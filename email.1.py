email="t"
pwd=1
otp=123
uemail=str(input("enter the email"))
upwd=int(input("enter the password"))
if(email == uemail):
    if(pwd ==upwd):
    print("login success")
    uotp=int(input("enter otp"))
    if(otp == uotp):
      print("ok")
    else:
      print("not ok")
    else:
     print("login failed due to incorrect pwd")
else:
  print("login failed due to incorrect email")
      