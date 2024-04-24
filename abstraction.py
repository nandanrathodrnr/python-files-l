from abc import ABC,abstractmethod
class A(ABC):
    def add(self):
        pass
    def sub(self):
        pass

class B(A):
    def add(self):
        print("added")
    def sub(self):
        print("subtracted")

class C(A):
    def add(self):
        print(" this is additon")
    def sub(self):
        print("this is subtraction")
        
class D:
    def reference(self,ref):
        ref.add()
        ref.sub()
    



obj1=B()
obj2=C()

obj3=D()
obj3.reference(obj1)
obj3.reference(obj2)
        
