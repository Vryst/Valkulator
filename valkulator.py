num1 = float(input('Number:\n'))
comnd = str(input('Choose one +,-,x,÷:\n'))
num2 = float(input('2nd number:\n'))
h1 = float(num1 + num2)
h2 = float(num1 - num2)
h3 = float(num1 * num2)
h4 = float(num1 / num2)

if comnd == '+':
    print(f"The result of {float(num1)}, + ,{float(num2)} is = {float(h1)}")

if comnd == '-':
    print(f"The result of {float(num1)}, - ,{float(num2)} is = {h2}")

if comnd == 'x':
    print(f"The result of {float(num1)}, x ,{float(num2)} is = {h3}")
    
if comnd == '÷':
    print(f"The result of {float(num1)}, ÷ ,{float(num2)} is = {h4}")
    
print("\n\nProgram Finished")
