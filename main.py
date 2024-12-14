class Animal:
    def __init__ (self , type, NumofLegs , avgLife):
        self.type = type
        self.NumofLegs = NumofLegs
        self.avgLife = avgLife
        print("Hello i am constructor")

    def PrintInfo(self):
        print(self.type)
        print(self.NumofLegs)
        print(self.avgLife)

    def __del__(self):
        print("Hello i am destructor")

cat = Animal("cat" , 4 , 9)
cat.PrintInfo()