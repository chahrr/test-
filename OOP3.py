#inherits, extend, override



class Employee:
    
    def __int__(self, name, age, salary):
        self.name = name
        self.age = age 
        self.salary = salary 
    def work(self):
        print(f"{self.name} is working...")


class SoftwareEnginner(Employee): 
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level 

    def work(self):
        print(f"{self.name} is codinging...")

    def debug(self):
        print(f"{self.name} is debugging..")

class Designer(Employee):

    def work(self):
        print(f"{self.name} is designing...")

    def draw(self):
        print(f"{self.name} is drawing...")
 
se = SoftwareEnginner("Max", 25, 6000, "Junior")
#print(se.name, se.age, se.salary)
#se.work()
#se.debug()
#print(se.level) 

d = Designer("Phillip", 27, 7000)
#print(d.name, d.age, d.salary) 
#d.work()
#d.draw()


#polymorphism
employees = [SoftwareEnginner("Max", 25, 6000, "Junior"),
             SoftwareEnginner("Lisa", 30, 9000, "Senior"),
             Designer("Phillip", 27, 7000)]



def motivate_employees(employees):
    for employee in employees:
        employee.work()

motivate_employees(employees)     


# Recap
# inheritance : CHildclass(BaseClass)
#inherit, extend, override
#super().__int__()
# polymorphism