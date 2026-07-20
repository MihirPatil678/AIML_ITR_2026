class Person:
    def __init__(self, name, age):   # Fix 1: Added 'self'
        self.name = name             # Fix 2: self.name Stores The Attribute
        self.age  = age              # Fix 2: elf.age  Stores The Attribute
 
    def introduce(self):             # Fix 3: Added 'self'
        # Fix 4: f-string For Proper String Formatting
        print(f"My name is {self.name} and I am {self.age} years old.")
 
p1 = Person("Mihir", 18)
p1.introduce()