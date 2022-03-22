# sett=[[["N Mehta","Th"],["A Gondal", "Th"],["C Godse", "Lab"],["A Gondal", "Th"],["N Mehta","Th"]],[["N Mehta","Th"],["A Gondal", "Th"],["C Godse", "Lab"],["A Gondal", "Th"],["N Mehta","Th"]]]

# print(sett[1][4][0])

# for i in sett :
#     print(i)
#     print("\n")
classroom = []
noofclass = input("Enter number of classrooms : ")
for i in range(0,int(noofclass)):
    classroom.append(input("Enter classroom number : "))
print("classroom :")
print(classroom)

lab = []
nooflabs = input("Enter number of classrooms : ")
for i in range(0,int(nooflabs)):
    lab.append(input("Enter classroom number : "))
print("lab :")
print(lab)


noofteachers = input("Enter number of classrooms : ")
teachers=[[] for _ in range(0,int(noofteachers))]
for i in range(0,int(noofteachers)):
    print("Enter info : ")
    teachers[i].append(input("Name : "))
    teachers[i].append(input("Time Slot : "))
    teachers[i].append(input("subject : "))
    teachers[i].append(input("Th : "))
    teachers[i].append(input("PT : "))
    teachers[i].append(input("Tut : "))

print(teachers[0][1])
print("lab :")
print(lab)

Ateachers = []
Bteachers = []
for i in range(0,int(noofteachers)):
    print(i)
    if(teachers[i][1]=="A"):
        Ateachers.append(teachers[i][0])
    else:
        Bteachers.append(teachers[i][0])

