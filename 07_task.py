# Create a class Phone with a method call(). 
# Then create a subclass SmartPhone with an additional method browse().

class Phone:
    def call(self):
        print("Making a call...")

class SmartPhone(Phone):
    def browse(self):
        print("Browsing the internet...")

sp = SmartPhone()
sp.call()
sp.browse()
