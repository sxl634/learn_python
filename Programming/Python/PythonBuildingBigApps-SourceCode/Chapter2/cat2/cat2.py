# cat2.py provides an improved Cat Class

class Cat:
    # constructor
    def __init__(self, name):
        self.name = name

    # other methods
    def speak(self):
        print(self.name, "says meow.")

    def drink(self):
        print(self.name, "drinks some milk.")
        print(self.name, "takes a nap.")
