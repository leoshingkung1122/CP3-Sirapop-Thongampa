'''
This is GPA calculation Program for student
'''
x = input("Student First name   :")
y = input("Student Last  name   :")
print("----------------------------")
print("For example, Student XXX Grade : A,B,C,D,F")
englishGrade    = input("Student English    Grade :")
gBusinessGrade  = input("Student Business   Grade :")
comSystemGrade  = input("Student ComSystem  Grade :")
comProgramGrade = input("Student ComProgram Grade :")

print("----------------------------")
print("---Your score---")
print("Foundation English               :",englishGrade)
print("General Business                 :",gBusinessGrade)
print("Introduction to Computer Systems :",comSystemGrade)
print("Computer Programming             :",comProgramGrade)
print("----------------")

''' Here is a sum total of your grades and divide by the number of subjects 
which have enrolled in this semester'''
if englishGrade == "A":
    englishGrade = 4.00
if englishGrade == "B":
    englishGrade = 3.00
if englishGrade =="C":
    englishGrade = 2.00
if englishGrade == "D":
    englishGrade = 1.00
if englishGrade == "F":
    englishGrade = 0.00
if gBusinessGrade == "A":
    gBusinessGrade = 4.00
if gBusinessGrade =="B":
    gBusinessGrade = 3.00
if gBusinessGrade == "C":
    gBusinessGrade = 2.00
if gBusinessGrade == "D":
    gBusinessGrade = 1.00
if gBusinessGrade == "F":
    gBusinessGrade = 0.00
if comSystemGrade == "A":
    comSystemGrade = 4.00
if comSystemGrade =="B":
    comSystemGrade = 3.00
if comSystemGrade == "C":
    comSystemGrade = 2.00
if comSystemGrade == "D":
    comSystemGrade = 1.00
if comSystemGrade == "F":
    comSystemGrade = 0.00
if comProgramGrade == "A":
    comProgramGrade = 4.00
if comProgramGrade =="B":
    comProgramGrade = 3.00
if comProgramGrade == "C":
    comProgramGrade = 2.00
if comProgramGrade == "D":
    comProgramGrade = 1.00
if comProgramGrade == "F":
    comProgramGrade = 0.00

numberSubject       = 4
result = (englishGrade + gBusinessGrade+ comSystemGrade + comProgramGrade)/numberSubject
summary = (englishGrade + gBusinessGrade+ comSystemGrade + comProgramGrade)/numberSubject >= 2.00

print("Average GPA of (Mr/Mrs)",x,y,"is :",result)
print("----------------")
print("If your GPA is lower than 2.00 you will be dismissed")
print("Your student condition still is normal :",summary)





