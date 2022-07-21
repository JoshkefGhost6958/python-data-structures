#printing our employee list
#defining a node to store our values
class Node:
    def __init__(self,name = None):
        self.name = name
        self.nextEmployee = None
#creating the linked list
class employees:
    def __init__(self):
        #setting the head node
        self.chief = None

        #a function to print out employees
    def checkEmps(self):
        empval = self.chief
        while empval is not None:
            print(empval.name)
            empval = empval.nextEmployee

emps = employees()#pointer to head
emps.chief = Node("Joshua")
e2 = Node("Travis")
e3 =Node("Trap")
emps.chief.nextEmployee = e2
e2.nextEmployee = e3
emps.checkEmps()
