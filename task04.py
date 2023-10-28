# Lab#3 Methods in Object Oriented Programming Using Python.

# Instance Method

#Example 1
class Student:
               def __init__(self,a,b):
                       self.a =a 
                       self.b = b
               def avg(self):
                       return (self.a + self.b) /2

s1 = Student(10,20)
print(f"Average student is {s1.avg()}")


# Example 2

class Volume:
        def calculate(self,c,d):
                self.c = c
                self.d = d
                e = c * d
                print(f"volume is {c}")

z = Volume()
z.calculate(10,20)

# or

class volume:
        def calculate01(self):
                f = 9
                g = 7
                h = f * g 
                print("volume is ",h)

x = volume()
x.calculate01()



