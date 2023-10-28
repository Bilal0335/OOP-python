# Exercise-3: Create a class with name Human and with some characteristics 

class Human:
               print("\n-------------------------------------")
               species = "Animal"
               def __init__(self,name,age,profession):
                       self.name = name
                       self.age = age
                       self.profession = profession

Amir = Human("Amir",25,"Doctor")
Aisha = Human("Aisha",25,"Teacher")

print("Amir is a {} ".format(Amir.__class__.species))
print("Aisha is a {} ".format(Aisha.__class__.species))

print("{} is {} years old and {}".format(Amir.name,Amir.age,Amir.profession))
print("{} is {} years old and {}".format(Aisha.name,Aisha.age,Aisha.profession))
print("-------------------------------------\n")


