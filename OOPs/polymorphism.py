# Method Overriding 
# Same name in all classes with different values/ print statements

class A:
    def fun(self):
        print("Class A")

class B(A):
    def fun(self):
        super().fun()
        print("Class B")

class C(B):
    def fun(self):
        super().fun() # To access parent class (Method Overloading)
        print("Class C\n")

obj = C()
obj.fun()