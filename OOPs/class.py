# Creating a class


class Sample:
    greet = "Welcome to Sample class"
    def func(self):
        print(self.greet)


# Creating a object
obj = Sample()
obj.func()  # func(obj)


class Demo:
    def func1(self):
        print("func1")

    def func2(self):
        print("func2")

    def func3(self):
        print("Welcome to Demo\n func3")
        self.func1()    # Accessing others functions inside the function within same class
        self.func2()

obj1 = Demo()
obj1.func3()



class A:
    def __init__(self):
        print("Constructor called")
    def fun(self):
        print("Function called")
    def __del__(self):
        print("Destructor called")

obj2 = A()
obj2.fun()
del obj2