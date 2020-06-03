'''
This is GPA result for student
'''
A = 4.00
B = 3.00
C = 2.00
D = 1.00
F = 0.00
'''Input Grade results after the the comma sign to accumulate and analyze the GPA'''
englishGrade        = A
gBusinessGrade      = B
comSystemGrade      = C
comProgramGrade     = F
numberSubject       = 4
result = (englishGrade + gBusinessGrade+ comSystemGrade + comProgramGrade)/numberSubject
print("---Your score---")
print("Foundation English               :",englishGrade)
print("General Business                 :",gBusinessGrade)
print("Introduction to Computer Systems :",comSystemGrade)
print("Computer Programming             :",comProgramGrade)
print("----------------")
''' Here is a sum total of your grades and divide by the number of subjects 
which have enrolled in this semester'''
print("Average GPA                      :",result)


