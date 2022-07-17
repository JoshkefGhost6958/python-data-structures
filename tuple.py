#unlike lists tuples cannot be altered
chief_of_staff = ('john','vice','manuel');
importantYears =(1980,2000,2005);
print("This compaany was founded on: ",importantYears[1])

#one element tupple
#include comma even if its one element
Dob = (2002,);
print(Dob[0]);

#tuple traversal
#beginnning to end
print(importantYears[0:])

#creating tuple and adding values to it

allAbout = chief_of_staff + importantYears;
print(allAbout)
print(len(allAbout))
#using an if statement and len statement
if len(allAbout) > 2:
    print("The list has more than 2 elements")
    print("It contains: ",len(allAbout))
#using a for loop for traversal
print("important people && years: \n")
for x in allAbout:
    print(x)
