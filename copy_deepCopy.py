import copy
li = [1,2,3,4,5,6,[7,8,9]]
li2 = copy.copy(li)
li3 = li
li.append(10)
print(li)
print(li2)
print("li3:",li3)