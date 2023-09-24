# list = [22,33,44,55,33,'forhad', 'Apollo', 'Akter']
# print(list)
# list.append(55)
# print(list)
# list.remove(22)
# print(list)
# list.pop()
# print(list)

list = ['mango','guava','banan','orange']
# list.insert(2, 'grape')
# print(list)
list2= [1,2,'one','two','three']
list.extend(list2)
for i in list:
    print(i)
list.remove('mango')
list.pop()
print(list)


del(list[1]) #delete_method
print(list)

list.clear()#clear_method
print(list)