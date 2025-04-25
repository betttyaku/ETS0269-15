set_1= {1,2,3,4,5,6,7,8,}
set_1.remove(8)
print(set_1)

set_1= {1,2,3,4,5,6,7,8,}
set_1.add(9)
print(set_1)

set_1= {1,2,3,4,5,6,7,8,}
set_1.clear()
print(set_1)

set_1= {1,2,3,4,5,6,7,8,}
set_1.copy()
print(set_1)

set_1= {1,2,3,4,5,6,7,8,}
set_2 ={1,9,0,8,6,4}
difference = set_1.difference(set_2)
print(difference)

set_1= {1,2,3,4,5,6,7,8,}
set_2 ={1,6,7,0,9,5}
intersection = set_1.intersection(set_2)
print(intersection)