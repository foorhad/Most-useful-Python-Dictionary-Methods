# #list_compurehensions
list1 = [34,44,55,'name','roll','registration', 'number',66,3,12]
list = [1,2,4,5,6,7,8]

# newList = [2*x for x in list]
# print(newList)

# even_number 
# for i in list:
#     if i % 2 ==0:
#         even_number.append(i)

#1number_method
print([i for i in list if i%2==0])

#2number_method
list = [1,2,3,4]
print('list= ',list)
squareList = [i**2 for i in list ]
print(squareList)
