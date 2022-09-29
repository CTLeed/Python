from dojo_animals import Pet
from dojo_ninjas import Ninja


ted = Pet("Ted", "dog", "fetch")

for animal in Pet.animals:
    print(animal.name)

ted.play()

print(ted.health)

colby = Ninja("Colby", "Leed", "milk bones", "salmon kibble", ted)

colby.walk()

colby.feed()

print(ted.health)

trevor = Pet("Trevor", "frog", "hop")

neville = Ninja("Neville", "Longbottom", "flies", "frog food", trevor)

neville.bathe()
