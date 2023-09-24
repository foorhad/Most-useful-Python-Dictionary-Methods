employe_info = {'name':'Kader', 'Dist':"Dhaka", 'Salary':18500, 'position':'2nd'}
employe_info1 = {'name':'Abdullah', 'Dist':"Manikgonj"}

print("befor update information: ",employe_info)
employe_info.update(employe_info1)
print("After update information: ", employe_info)

#copy() mehod
employe_info.copy()
employe_info['Salary']=20000
print('copy: ', employe_info)