class Animal:

    def __init__(self, type, name):
        self.name = name
        self.type = type
        if type == "cat":
            self.sound = "meow"
            self.size = "small"
        elif type == "dog":
            self.sound = "woof"
            self.size = "medium"
        elif type == "hippo":
            self.sound = "loud"
            self.size = "enormous"
        else:
            self.sound = "unknown"
            self.size = "unknown"

rumi = Animal("dog", "Rumi")
aly = Animal("hippo", "Aly")

