'''
This is GPA calculation Program for student
'''
x = input("Student First name   :")
y = input("Student Last  name   :")
print("----------------------------")
print("For example, Student XXX Grade : 4.00, 3.50, 3.00, 1.50, 0.00")
print("Note!!! you have to input float values don't input the integer")
englishGrade    = float(input("Student English    Grade :"))
gBusinessGrade  = float(input("Student Business   Grade :"))
comSystemGrade  = float(input("Student ComSystem  Grade :"))
comProgramGrade = float(input("Student ComProgram Grade :"))

print("----------------------------")
print("---Your score---")
print("Foundation English               :",englishGrade)
print("General Business                 :",gBusinessGrade)
print("Introduction to Computer Systems :",comSystemGrade)
print("Computer Programming             :",comProgramGrade)
print("----------------")

''' Here is a sum total of your grades and divide by the number of subjects 
which have enrolled in this semester'''
numberSubject       = 4
result = (englishGrade + gBusinessGrade+ comSystemGrade + comProgramGrade)/numberSubject
summary = (englishGrade + gBusinessGrade+ comSystemGrade + comProgramGrade)/numberSubject >= 2.00

print("Average GPA of (Mr/Mrs)",x,y,"is :",result)
print("----------------")
print("If your GPA is lower than 2.00 you will be dismissed")
print("Your student condition still is normal :",summary)





