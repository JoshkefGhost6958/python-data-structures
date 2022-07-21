class Node:
    def __init__(self,data =None):
        self.data = data
        self.link = None
class SLinkedlist:
    def __init__(self):
        self.head = None
    def letsprint(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.link
list1 = SLinkedlist()
list1.head = Node("MON")
e2 = Node("TUE")
e3 =Node("WED")
list1.head.link = e2
e2.link = e3
list1.letsprint()