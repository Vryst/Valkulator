num1 = float(input('Input number:\n'))
comnd = str(input('choose one : +,-,x,÷'))
num2 = float(input('Input second number:\n'))

r1 = float(num1 + num2)
r2 = float(num1 - num2)
r3 = float(num1 * num2)
r4 = float(num1 / num2)

if comnd == '+':
    print(f"The result of {float(num1)} + {float(num2)} is = {r1}")
    
if comnd == '-':
    print(f"The result of {float(num1)} - {float(num2)} is = {r2}")
   
if comnd == 'x':
    print(f"The result of {float(num1)} x {float(num2)} is = {r3}")
   
if comnd == '÷':
    print(f"The result of {float(num1)} ÷ {float(num2)} is = {r4}")
    
print("\nValkulator Finished")
