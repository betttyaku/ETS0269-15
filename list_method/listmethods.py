my_list = ["1","2","4","3"]
my_list.append("14")
print(my_list)

my_list = ["2","4","5","6"]
my_list.clear()
print(my_list)

my_list = ["2","3","4","5"]
my_list.copy()
print(my_list)

my_list = ["1","2","3","4","5"]
my_list.count("3")
print(my_list)
#output : ['1', '2', '3', '4', '5']

my_list = ["a","d","f","j","k"]
my_list.extend("n")
print(my_list)
#output : ['a', 'd', 'f', 'j', 'k', 'n']

my_list =  ["1","2","3","4","5"]
my_list.index("1")
print(my_list)
#output :['1', '2', '3', '4', '5'] 


my_list =  ["1","2","3","4","5"]
my_list.insert(5,"8")
print(my_list)
#output :['1', '2', '3', '4', '5', '8']

my_list =  ["1","2","3","4","5"]
my_list.pop()
print(my_list)
#output :['1', '2', '3', '4']

my_list =  ["1","2","3","4","5"]
my_list.remove("1")
print(my_list)
#output : ['2', '3', '4', '5']

my_list = ["1","2","3","4","5"]
my_list.reverse()
print(my_list)
#output : ['5', '4', '3', '2', '1']

my_list =  ["5","2","4","3","1"]
my_list.sort()
print(my_list)
#output : ['1', '2', '3', '4', '5']
