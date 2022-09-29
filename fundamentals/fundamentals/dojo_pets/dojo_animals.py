class Pet:
    animals = []

    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 50
        self.energy = 0
        Pet.animals.append(self)

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        pet_type = self.type
        if pet_type == "dog":
            print("Woof!")
            return self
        elif pet_type == "cat":
            print("Meeeeow")
            return self
        elif pet_type == "frog":
            print("riiiiiibbit")
            return self
        else:
            print("What do you want from me?!")
            return self


ted = Pet("Ted", "dog", "fetch")

trevor = Pet("Trevor", "frog", "hop")
