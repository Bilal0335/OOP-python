# LABORATORY MANUAL CONTENTS
# Example:-1 Create a class with name Parrot and some object
class Parrot:
# class attribute
               speciec = "parrot"
# instance attribute
               def __init__(self,name,age):
                       self.name=name
                       self.age=age         

# instantiate the Parrot class (Objects of the class)
blu = Parrot("blu",10)
woo = Parrot("woo",20)

# access the class attributes
print("blu is {}".format(blu.__class__.speciec))
print("woo is {}".format(woo.__class__.speciec))


# access the instance attributes
print("{} is {} year old".format(blu.name,blu.age))
print("{} is {} year old".format(woo.name,woo.age))



class Parrot:
# class attribute
      species = "bird"
      Age=10;
      Name="Blu";
# instantiate the Parrot class
blu = Parrot()
woo = Parrot()
# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))
print("Blu age is {}".format(blu.__class__.Age))
print("Its name is {}".format(woo.__class__.Name))
