employe_info = {'name':'Kader', 'Dist':"Dhaka", 'Salary':18500, 'position':'2nd'}

print('The information of employe: \n', employe_info.items())



#extra_method_use_this_progam
employe_info['name']='Kader uddin'
print(employe_info)

a =employe_info.setdefault("shift",'morning')
print(employe_info)

print(employe_info['Dist'])

print(len(employe_info))

gets = employe_info.get('age',20)
print('Employe age is :-', gets)
