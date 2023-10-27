# Example:-2 Create a class with name Human and their objects Amir and Aisha
class Human:
# class attribute
      species = "Animal"
# instance attribute
def __init__(self, name, age):
      self.name = name
      self.age = age
# instantiate the Parrot class
Amir = Human("Amir", 25)
Aisha = Human("Aisha", 20)
# access the class attributes
print("Amir is a {}".format(Amir.__class__.species))
print("Aisha is also a {}".format(Aisha.__class__.species))
# access the instance attributes
print("{} is {} years old".format( Amir.name, Amir.age))
print("{} is {} years old".format( Aisha.name, Aisha.age))
