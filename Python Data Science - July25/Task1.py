list=[1,2,3,4,5]
emp={"name":"matt","age":"19","place":"bangalore"}
myset={1,2,3,4,5}

list.append(6)
list.remove(2)
list[0]=8

emp["sex"]="male"
del emp["place"]
emp["age"]='24'

myset.add(9)
myset.remove(3)
myset.discard(4)
myset.add(10)

print('The updated list is :',list)
print('The updated dict is :',emp)
print('The updated set is :',myset)