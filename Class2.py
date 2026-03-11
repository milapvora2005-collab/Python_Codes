#Object Oriented Programming Of Python

class student:
    def __init__(self,name,rollnumber):
        self.name=name
        self.rollnumber=rollnumber

    def info(self):
        print(self.name)
        print(self.rollnumber)

student1=student("Milap",28)
student1.info()
