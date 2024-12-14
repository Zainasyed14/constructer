class Employee : 
    def __init__ (self, id , name):
        self.id = id
        self.name = name
        print("Hi, i am an emplpoyee")

    def PrintInfo(self):
        print(self.id)
        print(self.name)
    
    def __del__(self):
        print("Goodbye")

Sarah = Employee("05123" , "Sarah")
Sarah.PrintInfo()