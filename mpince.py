class A:
    def me(self):
        print("this is super class")
class B(A):
    def meth(self):
        print("this is child class 1")
class C(A):
    def method(self):
        print("this is child class 2 ")     
obj=C()
obj1=B()
obj.me()
obj1.meth()
obj.method()
                          

