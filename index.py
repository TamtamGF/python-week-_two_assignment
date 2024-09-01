my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list[1]=15
list_B=[]
list_B.append(50)
list_B.append(60)
list_B.append(70)
my_list.extend (list_B)
del my_list[3]
my_list.sort()
index_value = my_list.index(30)
print(index_value)