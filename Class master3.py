class master:
    org="Aeonx"
    Address="Bhuj"

    def __init__(self,name,ID):
        self.name=name
        self.ID=ID

class emp(master):
    pass
class details(emp):
    def display(self):
        print(f"Name Of Employee={self.name}")
        print(f"ID Of Employee={self.ID}")

master1=details("abc",101)
master1.display()
