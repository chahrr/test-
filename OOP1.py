# position, name, age, level, salary


se1 = ["softwareEngineer", "Max", 20, "Jenior", 5000]
se2 = ["SoftwareEngineer", "Lisa", 25, "Senior", 7000]

# calss
class SoftwareEngineer:
      # class attribute
      alias = "Keyboard Magacian"

      def __init__(self, name, age, level, salary):
          #instance attributes 
          self.name = name
          self.age = age 
          self.level = level
          self.salary = salary 
# instance 
se1 = SoftwareEngineer("Max", 20, "Jenior", 5000)   
print(se1.name, se1.age)
print(se1.alias)
se2 = SoftwareEngineer("Lisa", 25, "Senior", 7000)
print(SoftwareEngineer.alias)