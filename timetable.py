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

noofteachers=16
teachers=[["CG","C","OS",3,2,"704","",0,0,"","",0,0,""],["NM","A","MP",3,2,"701","",0,0,"","",0,0,""],["AG","C","DBMS",3,2,"LL","",0,0,"","",0,0,""],["DR","B","AOA",3,2,"702","",0,0,"","",0,0,""],["AS","C","PYTHON",2,2,"501","",0,0,"","",0,0,""],["AJ","D","EM4",3,0,"","",0,0,"","",0,0,""],["RJ","A","",0,0,"","SPCC",3,2,"704","",0,0,""],["NV","C","",0,0,"","AI",3,2,"501","",0,0,""],["UA","C","",0,0,"","CNSS",3,2,"108","",0,0,""],["RS","C","",0,0,"","MC",3,2,"704","",0,0,""],["DNR","A","",0,0,"","IOT",3,0,"","",0,0,""],["MNR","C","",0,0,"","CC",0,2,"","",0,0,""],["SS","A","",0,0,"","",0,0,"","HMI",4,2,"702"],["VJ","C","",0,0,"","",0,0,"","EM",3,0,""],["TRP","A","",0,0,"","",0,0,"","AWN",4,2,"501"],["SS","B","",0,0,"","",0,0,"","DC",4,2,""]]

# STRUCTURE OF TT
se_tt=[[["LAB"],["LAB"],[],[],[],[]],[[],[],["LAB"],["LAB"],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[["LAB"],["LAB"],[],[],[],[]],[["LAB"],["LAB"],["LAB"],["LAB"],[],[]]]

te_tt=[[[],[],[],[],["LAB"],["LAB"]],[[],[],[],[],["LAB"],["LAB"]],[[],[],["LAB"],["LAB"],["LAB"],["LAB"]],[[],[],[],[],["LAB"],["LAB"]],[[],[],["LAB"],["LAB"],["LAB"],["LAB"]],[[],[],[],[],[],[]]]

be_tt=[[[],[],["LAB"],["LAB"],[],[]],[["LAB"],["LAB"],[],[],[],[]],[["LAB"],["LAB"],[],[],["LAB"],["LAB"]],[[],[],["LAB"],["LAB"],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]]]

# ARRANGING SE TIMETABLE
for i in range(0,6):
    for j in range(0,6):
        if len(se_tt[j][i])==0:
            if i==0:
                random.shuffle(teachers)
                for z in range(0,noofteachers):
                    if teachers[z][1]=="A" :
                        if teachers[z][3]!=0:
                            teachers[z][3]=teachers[z][3]-1
                            se_tt[j][i].append(teachers[z][2])
                            se_tt[j][i].append(teachers[z][0])
                            break
            elif i==5:
                random.shuffle(teachers)
                for z in range(0,noofteachers):
                    if teachers[z][1]=="B" :
                        if teachers[z][3]!=0:
                            teachers[z][3]=teachers[z][3]-1
                            se_tt[j][i].append(teachers[z][2])
                            se_tt[j][i].append(teachers[z][0])
                            break
            else:
                random.shuffle(teachers)
                for z in range(0,noofteachers):
                    if teachers[z][3]!=0:
                        teachers[z][3]=teachers[z][3]-1
                        se_tt[j][i].append(teachers[z][2])
                        se_tt[j][i].append(teachers[z][0])
                        break

# ARRANGING TE TIMETABLE
for i in range(0,6):
    for j in range(0,5):
        if len(te_tt[j][i])==0:
            if i==0:
                random.shuffle(teachers)
                for z in range(0,noofteachers):
                    if teachers[z][1]=="A" :
                        if teachers[z][7]!=0:
                            teachers[z][7]=teachers[z][7]-1
                            te_tt[j][i].append(teachers[z][6])
                            te_tt[j][i].append(teachers[z][0])
                            break
            elif i==5:
                random.shuffle(teachers)
                for z in range(0,noofteachers):
                    if teachers[z][1]=="B" :
                        if teachers[z][7]!=0:
                            teachers[z][7]=teachers[z][7]-1
                            te_tt[j][i].append(teachers[z][6])
                            te_tt[j][i].append(teachers[z][0])
                            break
            else:
                random.shuffle(teachers)
                for z in range(0,noofteachers):
                    if teachers[z][7]!=0:
                        teachers[z][7]=teachers[z][7]-1
                        te_tt[j][i].append(teachers[z][6])
                        te_tt[j][i].append(teachers[z][0])
                        break
                            

# ARRANGING BE TIMETABLE
for i in range(0,6):
    for j in range(0,5):
        if len(be_tt[j][i])==0:
            if i==0:
                random.shuffle(teachers)
                for z in range(0,noofteachers):
                    if teachers[z][1]=="A" :
                        if teachers[z][11]!=0:
                            teachers[z][11]=teachers[z][11]-1
                            be_tt[j][i].append(teachers[z][10])
                            be_tt[j][i].append(teachers[z][0])
                            break
            elif i==5:
                random.shuffle(teachers)
                for z in range(0,noofteachers):
                    if teachers[z][1]=="B" :
                        if teachers[z][11]!=0:
                            teachers[z][11]=teachers[z][11]-1
                            be_tt[j][i].append(teachers[z][10])
                            be_tt[j][i].append(teachers[z][0])
                            break
            else:
                random.shuffle(teachers)
                for z in range(0,noofteachers):
                    if teachers[z][11]!=0:
                        teachers[z][11]=teachers[z][11]-1
                        be_tt[j][i].append(teachers[z][10])
                        be_tt[j][i].append(teachers[z][0])
                        break
           

# SHUFFLE TEACHER LIST
random.shuffle(teachers)
#print(teachers)

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


print(be_tt)
print("\n\n")
print(se_tt)
print("\n\n")
print(te_tt)


