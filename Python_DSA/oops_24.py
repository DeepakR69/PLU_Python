class Parent:
    def __init__(self, name):
        self.name = name
        
class childOne(Parent):
    def __init__(self, name):
        super().__init__(name)
        print("Child One")

class childTwo(childOne):
    def __init__(self, name):
        super().__init__(name)
        print("Child Two")