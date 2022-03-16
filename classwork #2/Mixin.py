class CallMixin():
    def call(self):
        print(f"Pending a call to  +{self.phone}")
        
class Person(CallMixin):
    def __init__(self, fname, lname, phone):
        self.fname = fname
        self.lname = lname
        self.phone = phone
        
    def info(self):
        print(f"First name: {self.fname}\nLast name: {self.lname}")

    def call(self):
        print(f"Pending a call to {self.fname} {self.lname} on a number +{self.phone}")




fbi_agent = Person("Konstantine", "Mgeladze", 995541034141)
fbi_agent.info()
fbi_agent.call()