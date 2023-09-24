a = int (input('Enter the value of a :- '))
b = int (input('Enter the value of b :- '))
c = int (input('Enter the value of c :- '))

#use of and operator
if (a>b and a>c):
    largest_value = a
elif(b>c):
    largest_value = b

else:
    largest_value = c

print(largest_value)

#use of OR operator
if (a>b or a>c):
    print(a)
