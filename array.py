from array import *
tax_array = array('i',[22,45,66,77,98])
double_array = array('d',[55.77,90.89,88.88,77,56])

#array traversal
for x in tax_array:
    if x == 22:
        continue
    print(x)
    count = 0;
print("the 3rd element is:",tax_array[3])
print("our double list:")
#insertion in arrays
double_array.insert(2,678.88)
double_array.remove(55.77)
for i in double_array:
    if i == 56.0:
        break
    print(i)
else:
    print("loop conditions not met")
print(double_array.index(4))
print("--end--")

