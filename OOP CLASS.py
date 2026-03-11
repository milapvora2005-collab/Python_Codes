#Object Oriented Programming Of Python

class student:
    def __init__(self,name):
        self.name=name

    def info(self):
        print(self.name)

student1=student("Milap")
student1.info()
