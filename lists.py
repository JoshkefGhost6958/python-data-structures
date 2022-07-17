#lists
Employees = ['josh','vic','kefa']
numbers = [1,2,3,4,5]
characters =["F","m"]
#prints the first element in the list
print ("list[0]: ",Employees[0])
#prints from the first character but omits the last one i.e 5
print ("list[1:4]: ",numbers[1:4])

#Deletion

del numbers[2];
print(numbers)

#list concentration
numbers2 = [1,2,3,4] + [7,8,9,0]
print(numbers2)

#repetition 
fav_employee=Employees[0]*2
print(fav_employee)
