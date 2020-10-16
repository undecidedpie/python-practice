class Employee:
    raise_amt = 1.04

    #Default constructor
    def __init__(self, first, last, pay):
        self.firstName = first
        self.lastName = last
        self.pay = pay
    
    #Alternative constructor defined using @classmethod
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return(cls(first, last, pay))
        
    #always define __repr__, more meant for the develps
    def __repr__(self):
        return (f'Full name: {self.firstName} {self.lastName}, Pay: {self.pay}')

    #always implement __str__, more meant for the end-user
    def __str__(self):
        return (f'Employee {self.firstName} ready for duty!')
    
    #implement len to return the string length of full name
    def __len__(self):
        return (len(self.firstName) + len(self.lastName))

    #getter for email attribute
    @property
    def email(self):
        return(f'{self.firstName}.{self.lastName}@domain.com')

    #setter and getter for fullname attribute

    @property
    def fullname(self):
        return(f'{self.firstName} {self.lastName}')
    
    @fullname.setter
    def fullname(self, name):
        self.firstName, self.lastName = name.split(" ")


#single inheritance class test
class Developer(Employee):
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(self, first, last, pay)
        self.prog_lang = prog_lang