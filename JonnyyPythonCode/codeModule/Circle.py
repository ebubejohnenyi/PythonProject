import math
class Circle:
    def calculateRadius(Radius):
        area = Radius **2 * math.pi
    @property
    def set_radious(self):
        self.Radius

    def get_radious(self):
        return self.Radius

    Radius = float (input("Please enter the radius of a given circle: "))
    if Radius < 0:
        ValueError("The value you entered is incorrect. ")
    print("The area of a given circle is: ", calculateRadius(C))




