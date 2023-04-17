class Cat(Animal):
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} meows."

class Cat_refactored(Animal):
    # I doesn't have to define the init since the Animal class already has proper initialization and self.name storing.
    def speak(self):
        return f"{self.name} meows."
    
