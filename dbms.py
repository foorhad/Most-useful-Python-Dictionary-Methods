def student_info(a):
    swither = {
        10 :"Name:Forhad, Department:Computer, Shift:1st, Sem:6th",
        12 :"Name:Forhad, Departmet: Electrical shif:2n, sem:7th",     
        55 :"Name:Forhad, Department:Computer, Shift:1st, Sem:6th",
        13 :"Name:Forhad, Department:Computer, Shift:1st, Sem:6th",
        14 :"Name:Forhad, Department:Computer, Shift:1st, Sem:6th",
        15 :"Name:Forhad, Department:Computer, Shift:1st, Sem:6th",
        16 :"Name:Forhad, Department:Computer, Shift:1st, Sem:6th"
    }

    return swither.get(a, 'nothing')
a=int(input("Enter the Student id:- "))
print(student_info(a))