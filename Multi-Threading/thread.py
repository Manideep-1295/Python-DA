from threading import *
from time import *

class Sample(Thread):
    def func(self):
        print("Function called from run method")
    def run(self):
        self.func()
        for i in range(1,11):
            print(i,",")
            sleep(1)


class Demo(Thread):
    def run(self):
        for i in range(11,21):
            print(i,",")
            sleep(1)

obj1 = Sample()
obj2 = Demo()
'''
obj1.run() # This alone does not initializes the thread
obj2.run() # It runs like normal function, not like a thread
'''
obj1.start() #This intializes the thread and executes the statements in the run method
obj2.start()

obj1.join() # To wait until the thread is terminated
obj2.join()
print("End of program")