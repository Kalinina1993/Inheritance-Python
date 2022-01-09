class Animal:
    """Animal class is basic class for class Can fly for describe animal datas"""
    def __init__(self, name):
        print(name, "is an animal")


class Can_fly(Animal):
    """Can fly class derive Animal class"""
    def __init__(self, name):
        print(name, "can fly")
        super().__init__(name)


class Skin(Animal):
    """Skin class derive Can fly class"""
    def __init__(self, name):
        print(name, "body is covered with feathers")
        super().__init__(name)


class Beak(Animal):
    """Beak class derive Skin class"""
    def __init__(self, name):
        print(name, "have a beak")
        super().__init__(name)


class Eagle(Can_fly, Skin, Beak):
    """multiple derive"""
    def __init__(self):
        print("This is Eagle")
        super().__init__("Eagle")


bird = Eagle()
print(bird)
