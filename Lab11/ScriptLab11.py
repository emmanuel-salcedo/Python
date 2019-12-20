class Dogs:
    bonesperdog = 1
    numOfDogs = 0
    bellyrubs = 5
    balls = 1

    def __init__(self, Name, Age, Sex, Breed, Size):
        self.Name = Name
        self.Age = Age
        self.Sex = Sex
        self.Breed = Breed
        self.Size = Size

        Dogs.numOfDogs += 1

    def getBreed(self):
        return "Breed:" + self.Breed

    def dogYear(self):
        return self.Age * 7

    def changeBreed(self, Breed):
        self.Breed = Breed

    def showDog(self):
        return "This ia a " + self.Size + " " + str(
            self.Age) + " Year Old " + self.Sex + " " + self.Breed + ", Named " + self.Name

    @classmethod
    def morebones(cls, bones):
        cls.bonesperdog = bones

    @classmethod
    def morebellyrubs(cls, rubs):
        cls.bellyrubs = rubs

    @classmethod
    def moreballs(cls, balls):
        cls.balls = balls


print("Print # of Dogs")
print(Dogs.numOfDogs)
lance = Dogs('Lance', 5, "Male", 'Goldy', 'Large')
print(Dogs.numOfDogs)
randy = Dogs('Randy', 1, "Male", 'Pitbul', 'Medium')
print(Dogs.numOfDogs)
avery = Dogs('Avery', 2, 'Male', 'Corgi', 'Medium')
print(Dogs.numOfDogs)

print("\nPrint Dog Info")
print(lance.showDog())
print(randy.showDog())
print(avery.showDog())

print("\nPrint Dog Values")
print(lance.__dict__)
print(randy.__dict__)
print(avery.__dict__)
print("Bones: " + str(Dogs.bonesperdog))
print("Balls: " + str(Dogs.balls))

Dogs.morebones(3)
Dogs.moreballs(7)

print("\nChangeBones and Balls")
print(lance.__dict__)
print(randy.__dict__)
print(avery.__dict__)
print("Bones: " + str(Dogs.bonesperdog))
print("Balls: " + str(Dogs.balls))
