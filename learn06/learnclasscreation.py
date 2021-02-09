
class customer:
    name = "neil armstrang"
class house:
      material ="boards"
'''
class - keyword
class user defined classname
class name an method or function names talk about your experience
instantiation -creating an object
instance_name = classname()

'''

countingmaterials = house()
print(countingmaterials.material)
counting = customer()
print(counting.name)



class Robot:
     def introduce(my):
        print("myname is " + my.name)
r1 = Robot()
r1.name = "tom"
r1.color = "green"
r1.weight = 30
r1.introduce()

r2 = Robot()
r2.name ="sam"
r2.color = "red"
r2.weight = 40
r2.introduce()

def validate_customer(self):
    if self.age >18:
        print("provide alcohol")
    else:
        print("cannot provide alcohol")


