class Sample:
    def fun(self,a,b):
        try:
            a1 = [1,2,3]
            print(a1[2])
            print(a/b)
        except IndexError as ie:
            print(ie)
        except ZeroDivisionError as zde:
            print(zde)
        except Exception as e:
            print(e)
        except:
            print("Error occured")
        finally:
            print("End of the Try & Except")

obj = Sample()
obj.fun(10,2)



# User-defined Exception
class UnderAgeError(Exception):
    def __init__(self,error):
        pass

class Demo:
    def eligible(self,age):
        if age < 18:
            raise UnderAgeError("Age is under 18")
        else:
            print("Eligible to vote")

objdemo = Demo()
try:
    objdemo.eligible(17)
except UnderAgeError as uae:
    print(uae)    
finally:
    print("End of User-Defined Exception")


