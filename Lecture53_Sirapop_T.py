def vatCalculate(dataInput):
    result = dataInput+(dataInput*7/100)
    return result

dataInput = float(input("Input your value : "))
print(vatCalculate(dataInput))


































