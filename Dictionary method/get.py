employe_info = {'name':'Kader', 'Dist':"Dhaka", 'Salary':18500, 'position':'2nd'}

get = employe_info.get('name')
print("Emloye name : ", get)

get =employe_info.get('Age', 21)
print("Emloye age is: ", get)