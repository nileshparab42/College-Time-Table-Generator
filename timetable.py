import random

# FINAL OP
# sett=[[["N Mehta","MP","Th","402"],["A Gondal", "Th"],["C Godse", "Lab"],["A Gondal", "Th"],["N Mehta","Th"]],[["N Mehta","Th"],["A Gondal", "Th"],["C Godse", "Lab"],["A Gondal", "Th"],["N Mehta","Th"]]]

# TAKING CLASSROOM INPUTS
# for i in sett :
#     print(i)
#     print("\n")
# classroom = []
# noofclass = input("Enter number of classrooms : ")
# for i in range(0,int(noofclass)):
#     classroom.append(input("Enter classroom number : "))
classroom=[402,404,502]

# lab = []
# nooflabs = input("Enter number of classrooms : ")
# for i in range(0,int(nooflabs)):
#     lab.append(input("Enter classroom number : "))
# print("lab :")
# print(lab)


# noofteachers = input("Enter number of classrooms : ")
# teachers=[[] for _ in range(0,int(noofteachers))]
# for i in range(0,int(noofteachers)):
#     print("Enter info : ")
#     teachers[i].append(input("Name : "))
#     teachers[i].append(input("Time Slot : "))
#     teachers[i].append(input("subject(SE) : "))
#     teachers[i].append(input("Th(SE) : "))
#     teachers[i].append(input("PT(SE) : "))
#     teachers[i].append(input("Enter lab room no(SE) : "))
#     teachers[i].append(input("subject(TE) : "))
#     teachers[i].append(input("Th(TE) : "))
#     teachers[i].append(input("PT(TE) : "))
#     teachers[i].append(input("Enter lab room no(TE) : "))
#     teachers[i].append(input("subject(BE) : "))
#     teachers[i].append(input("Th(BE) : "))
#     teachers[i].append(input("PT(BE) : "))
#     teachers[i].append(input("Enter lab room no(BE) : "))

noofteachers=6
teachers=[["CG","OS",3,2,"704"],["NM","MP",3,2,"701"],["AG","DBMS",3,2,"LL"],["DR","AOA",3,2,"702"],["AS","PYTHON",2,2,"704"],["AJ","EM3",5,0,""]]

# STRUCTURE OF TT
se_tt=[[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]]]

te_tt=[[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]]]

be_tt=[[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]]]

# SHUFFLE TEACHER LIST
random.shuffle(teachers)
print(teachers)

for i in range(0,6):
    if teachers[i][3] == 2:
        id1=i
        teachers[i][3]=0
        break

for i in range(0,6):
    if teachers[i][3] == 2:
        id2=i
        teachers[i][3]=0
        break

print(id1)
print(id2)
print(teachers)
