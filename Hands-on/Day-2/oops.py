'''
Truck Scenario 

---------------------- 

You are given two incomplete classes Car and Truck. 

A Truck is a Car but with the additional behaviors. 

Inherit the Car Class into Truck class and build the additional features. 

Go through the comments in the prefilled code to implement the Car and Truck classes with the described attributes and methods. 

 

Points to Note: 

--------------------- 

The output of the testcase Checking Default Tests is given by the "default_test" function in the prefilled code. 

This coding question does not have the usual input/output testcases. The class defined by you will be tested internally whether the attributes are present or not. So in testcases results you will be shown the rough description of the tests that will be verified. 

You can copy the implementation of Car class from the previous set and add new features on top of that code 

Prefilled Code 

------------------ 
'''
# Truck class should have the following attributes & methods 

# 

# Old Attributes: 

#   color, max_speed, acceleration, tyre_friction, is_engine_started, current_speed 

# New Attributes: 

#     max_cargo_weight, load 

# 

# Old Methods: 

#   start_engine, stop_engine, accelerate, apply_brakes, sound_horn 

#  

# Override Methods: 

#   sound_horn: 

#       - Print "Honk Honk" if truck engine is on 

#       - Print "Car has not started yet" if truck engine is off 

# 

# New Methods: 

#   load_cargo: 

#       - This method will have an argument cargo_weight, denoting the weight to be loaded in the truck. 

#       - Truck can load some cargo within max_cargo_weight 

#       - When this method is called when the car engine is off, the  current_load of the truck 

#         should increase according to the  cargo_weight  passed as an argument to this method. 

#       - When this method is called when the car engine is on, print the message  "Cannot load cargo during motion" 

#       - When the cargo_weight is more than max_cargo_weight, 

#           print the message  "Cannot load cargo more than max limit: {max_cargo_weight}" 

#   unload_cargo: 

#       - This method will have an argument cargo_weight, denoting the weight to be unloaded from the truck. 

#       - Truck can unload amount of cargo_weight passed as an argument, only when the truck engine is off. 

#       - If the truck engine is on, print the message "Cannot unload cargo during motion" 

#       - Truck load can never go behind 0 

# 

# When a new Truck is created, the engine should be off by default and current_speed, load should be 0 

 

 

# Implement the Car and Truck class appropriately 

# Inherit the Car class into Truck class and override the methods which have extra features 

 
class Car:
    def __init__(self,color, max_speed, acceleration, tyre_friction, is_engine_started, current_speed):
        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self.is_engine_started = is_engine_started
        self.current_speed = current_speed
        #print(color, max_speed, acceleration, tyre_friction, is_engine_started, current_speed)
    
    def start_engine(self):
        self.is_engine_started = True

    def stop_engine(self):
        self.is_engine_started = False
        self.current_speed = 0

    def accelerate(self):
        if self.is_engine_started:
            self.current_speed += self.acceleration
            if self.current_speed > self.max_speed:
                self.current_speed = self.max_speed

    def apply_brakes(self):
        self.current_speed -= self.tyre_friction
        if self.current_speed < 0:
            self.current_speed = 0

    def sound_horn(self):
        if is_engine_started == 'True':
            return "Honk Honk"
        else:
            return "Car has not started yet"

'''
color = input("Enter color of the car: ")
max_speed = int(input("Enter max_speed of the car: "))
acceleration = input("Enter acceleration: ")
tyre_friction = input("Enter tyre_friction: ")
is_engine_started = bool(input("Enter is_engine_started: "))
current_speed  = int(input("Enter current_speed: "))
'''

color = "red"
max_speed = 160
acceleration = 20
tyre_friction = 10
is_engine_started = True
current_speed  = 50


obj = Car(color, max_speed, acceleration, tyre_friction, is_engine_started, current_speed)


class Truck(Car):
    def __init__(self, is_engine_started,current_speed,current_load,max_cargo_weight):
        # super().__init__(color,max_speed, acceleration,tyre_friction)
        self.is_engine_started = is_engine_started
        self.current_speed = current_speed
        self.current_load = current_load
        self.max_cargo_weight = max_cargo_weight
    
    def sound_horn(self):
        if is_engine_started == 'True':
            return "Honk Honk"
        else:
            return "Truck has not started yet"
    def load_cargo(self,cargo_weight):
        if not is_engine_started:
            if cargo_weight <= max_cargo_weight:
                self.current_load += cargo_weight
                return self.current_load
            else:
                return f"Cannot load cargo more than max limit: {max_cargo_weight}"
        else:
            return "Cannot load cargo during motion"
    def unload_cargo(self,cargo_weight,current_load):
        if is_engine_started == 'False':
            if (current_load - cargo_weight) >= 0:
                current_load -= cargo_weight
            else:
                return f"Cannot load cargo more than max limit: {max_cargo_weight}"
        else:
            return "Cannot load cargo during motion"
        

'''
print("Creating a Truck")
is_engine_started = bool(input("Enter is_engine_started: "))
current_speed  = int(input("Enter current_speed: "))
current_load = int(input("Enter current load: "))
max_cargo_weight = int(input("Enter max cargo weight: "))


is_engine_started = False
current_speed  = 0 
current_load = 0
max_cargo_weight = 1000

obj = Truck(
    is_engine_started, current_speed, current_load, max_cargo_weight 
)

print(obj.stop_engine())
print(obj.is_engine_started, obj.current_load, obj.current_speed, obj.max_cargo_weight)

print("Horn of the truck: ",obj.sound_horn())

cargo_wgt = int(input("Enter cargo weight to load into truck: "))
obj.load_cargo(cargo_wgt)
print("Cargo Weight loaded: ",cargo_wgt)
print("Current cargo weight: ",obj.current_load)


cargo_wgt = int(input("Enter cargo weight to load into truck: "))
obj.load_cargo(cargo_wgt)
print("Cargo Weight loaded: ",cargo_wgt)
print("Current cargo weight: ",obj.current_load)
'''




def default_test():
    # Create a Truck object
    truck = Truck("Red", 80, 10, 3, 100)

    # Test initial conditions
    assert truck.color == "Red"
    assert truck.max_speed == 80
    assert truck.acceleration == 10
    assert truck.tyre_friction == 3
    assert truck.is_engine_started == False
    assert truck.current_speed == 0
    assert truck.max_cargo_weight == 100
    assert truck.load == 0

    # Test starting engine and sounding horn
    truck.sound_horn()  # Expected: "Car has not started yet"
    truck.start_engine()
    truck.sound_horn()  # Expected: "Honk Honk"

    # Test loading cargo
    truck.load_cargo(50)
    assert truck.load == 50
    truck.load_cargo(60)  # Expected: "Cannot load cargo more than max limit: 100"

    # Test accelerating and loading cargo while engine is on
    truck.accelerate()
    assert truck.current_speed == 10
    truck.load_cargo(30)  # Expected: "Cannot load cargo during motion"

    # Test stopping engine and unloading cargo
    truck.stop_engine()
    truck.unload_cargo(30)
    assert truck.load == 20
    truck.unload_cargo(30)
    assert truck.load == 0  # load should not go below 0

    print("All tests passed!")

default_test()