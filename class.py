class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class JackRussellTerrier(Dog):
    def speak(self, sound="Wow"):
        return super().speak(sound)


class Dachshund(Dog):
    def speak(self, sound="Ffaf"):
        return super().speak(sound)


class Bulldog(Dog):
    def speak(self, sound="Wfghf"):
        return super().speak(sound)


dog1 = Dog('Bob', 23)
dog2 = Dog('Fgoe', 44)
jac = JackRussellTerrier("Miles", 7)
dac = Dachshund("Agdf", 6)
bul = Bulldog("Sggr", 35)
print(dog1)
print(dog2)
print(jac)
print(dac)
print(bul)
print(bul.speak())
print(dac.speak())
print(jac.speak())
