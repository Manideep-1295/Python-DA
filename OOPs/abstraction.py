# Objects cannot be created for an abstract class
from abc import *

class A:
    def show(self):
        print("This is class A")

class B(ABC):       # If the class is not inherited from ABC, obj will be created and can access all the methods inside the class
    @abstractmethod
    def display(self):
        pass

class C(B):
    def display(self):
        print("This is class C extending class B")

# obj = B()
obj1 = C()
obj1.display()