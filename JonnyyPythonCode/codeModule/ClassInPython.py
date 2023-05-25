class My_Class:
    # This is my function
    # def my_Method(self): # Creating a method
    #     print("Hello john")
    def __init__(self, name): # This is my constructor
        self.name = name

    def greet(self):
        print(f" {self.name} is walking")


My_Class1 = My_Class("Ebube")
My_Class2 = My_Class("John")
My_Class3 = My_Class("Enyi")
My_Class1.greet()
My_Class2.greet()
My_Class3.greet()
