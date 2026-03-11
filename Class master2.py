class master:
    org="Aeonx"
    address="Bhuj"
    
    def __init__(self,name,ID):
        self.name=name
        self.ID=ID

class emp(master):
    def display(self):
        print(self.name,self.ID)

master1=emp("abc",101)
master1.display()
master2=emp("xyz",102)
master2.display()
master1.org="Department"
print(master1.org)
print(master.org)
