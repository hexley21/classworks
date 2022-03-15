class Person():
    def __init__(self, fname, lname, phone) -> None:
        self.fname = fname
        self.lname = lname
        self.phone = phone
        
    def info(self):
        print(f"First name: {self.fname}\nLast name: {self.lname}")

class CallMixin(Person):
    def call(self):
        print(f"Pending a call to {self.fname} {self.lname} on a number +{self.phone}")


fbi_agent = CallMixin("Konstantine", "Mgeladze", 995541034141)
fbi_agent.info()
fbi_agent.call()