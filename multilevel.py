class Appliances:
    """Appliances class describe type of appliances"""
    def __init__(self, name):
        print(name, "large appliances")


class Kitchen_appliances(Appliances):
    """Kitchen appliance class derive Appliances class and describe main function of kitchen appliances"""

    def __init__(self, name):
        super().__init__(name)
        print(name, "kitchen appliances for food storage")


class Energy_consumption(Kitchen_appliances):
    """Energy consumption derive Kitchen appliances and inform about average electricity consumption of a
    refrigerator"""
    def __init__(self, name):
        super().__init__(name)
        print(name, "the average electricity consumption of a refrigerator ranges from 300 to 380 kilowatts per year")


class Fridge(Energy_consumption):
    """Fridge class derive Energy consumption and add parameters for information about fridge"""
    def __init__(self, label, maker, power, year):
        super().__init__(label)
        self.label = label
        self.maker = maker
        self.power = power
        self.year = year

    def show_Info(self):

        """This method output parameters with assignment of values"""
        print("Label: ", self.label)
        print("Maker: ", self.maker)
        print("Power: ", self.power)
        print("Year: ", self.year)


Info = Fridge("LG", "Russia", 277, 2019)
Info.show_Info()
