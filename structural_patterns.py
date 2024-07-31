""" 
Facade

According to Oxford Languages, a Facade is

an outward appearance that is maintained to conceal a less pleasant or creditable reality.
In the programming world, the "outward appearance" is the class or interface we interact with as programmers. And the "less pleasant reality" is the complexity that is hidden from us.
So a Facade, is simply a wrapper class that can be used to abstract lower-level details that we don't want to worry about.

 """


# Python arrays are dynamic by default, but this is an example of resizing.
class Array:
    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.arr = [0] * 2 # Array of capacity = 2

    # Insert n in the last position of the array
    def pushback(self, n):
        if self.length == self.capacity:
            self.resize()
            
        # insert at next empty position
        self.arr[self.length] = n
        self.length += 1

    def resize(self):
        # Create new array of double capacity
        self.capacity = 2 * self.capacity
        newArr = [0] * self.capacity 
        
        # Copy elements to newArr
        for i in range(self.length):
            newArr[i] = self.arr[i]
        self.arr = newArr
        
    # Remove the last element in the array
    def popback(self):
        if self.length > 0:
            self.length -= 1 




""" 
Adapter
Adapters allow incompatible objects to be used together. Following the Open-Closed principle, we can extend class behaviour without modifying the class itself.
If a MicroUsbCable class is initially incompatible with UsbPort, we can create a wrapper class (i.e. an Adapter), which makes them compatible. In this case, a MicroToUsbAdapter makes them compatible, similar to how we use adapters in the real-world.
 """

class UsbCable:
    def __init__(self):
        self.isPlugged = False
    
    def plugUsb(self):
        self.isPlugged = True

class UsbPort:
    def __init__(self):
        self.portAvailable = True
    
    def plug(self, usb):
        usb.plugUsb()
        self.portAvailable = False

# UsbCables can plug directly into Usb ports
usbCable = UsbCable()
usbPort1 = UsbPort()
usbPort1.plug(usbCable)

class MicroUsbCable:
    def __init__(self):
        self.isPlugged = False

    def plugMicroUsb(self):
        self.isPlugged = True

class MicroToUsbAdapter(UsbCable):
    def __init__(self, microUsbCable):
        self.microUsbCable = microUsbCable
        self.microUsbCable.plugMicroUsb()


         # can override UsbCable.plugUsb() if needed

# MicroUsbCables can plug into Usb ports via an adapter
microToUsbAdapter = MicroToUsbAdapter(MicroUsbCable())
usbPort2 = UsbPort()
usbPort2.plug(microToUsbAdapter)

""" Composite

The Composite pattern is a structural pattern because it deals with the composition of objects and how they are structured to form a whole.

The Composite design pattern is a structural pattern that allows clients to treat individual objects and compositions of objects uniformly. It enables you to create a tree-like structure of objects, where each node can be either a leaf node (a single object) or a composite node (a collection of objects). """

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_salary(self):
        return sum(employee.get_salary() for employee in self.employees)

# Usage:
ceo = Employee("CEO", 100000)
cto = Employee("CTO", 80000)
dev1 = Employee("Dev1", 60000)
dev2 = Employee("Dev2", 60000)

it_dept = Department("IT")
it_dept.add_employee(cto)
it_dept.add_employee(dev1)
it_dept.add_employee(dev2)

company = Department("Company")
company.add_employee(ceo)
company.add_employee(it_dept)

print(company.get_salary())  # Output: 260000