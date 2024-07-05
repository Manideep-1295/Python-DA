print("Single-Level Inheritance:")
# Single Inheritance
class Parent:
    def f1(self):
        print("This is Funciton 1 in Parent")


class Child(Parent):
    def f2(self):
        print("This is Funciton 2 in Child\n")

obj = Child()
obj.f1()
obj.f2()


print("Multi-Level Inheritance:")
# Multi Level Inheritance
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


print("Multiple Inheritance")
# Multiple Inheritance
class A:
    def fun(self):
        print("Class A")

class B():
    def fun(self):
        print("Class B")

class C(A,B):
    def fun(self):
        super().fun() # To access parent class (Method Overloading)
        print("Class C\n")

obj = C()
obj.fun()


print("Hierarchical Inheritance")
# Hierarchical Inheritance
class A:
    def fun(self):
        print("Class A")

class B(A):
    def fun(self):
        super().fun()
        print("Class B")

class C(A):
    def fun(self):
        super().fun() # To access parent class (Method Overloading)
        print("Class C\n")

objc = C()
objc.fun()

objb = B()
objb.fun()