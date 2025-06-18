class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def meow(self):
        print(f"{self.name} says Meow!")


my_cat = Cat("Leo", "White")


my_cat.meow()