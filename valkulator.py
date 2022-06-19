num1 = float(input('nomor:\n'))
comnd = str(input('pilih salah satu +,-,x,÷:\n'))
num2 = float(input('nomor ke-2:\n'))
h1 = float(num1 + num2)
h2 = float(num1 - num2)
h3 = float(num1 * num2)
h4 = float(num1 / num2)

if comnd == '+':
    print(f"Hasil dari {float(num1)}, + ,{float(num2)} adalah = {float(h1)}")

if comnd == '-':
    print(f"Hasil dari {float(num1)}, - ,{float(num2)} adalah = {h2}")

if comnd == 'x':
    print(f"Hasil dari {float(num1)}, x ,{float(num2)} adalah = {h3}")
    
if comnd == '÷':
    print(f"Hasil dari {float(num1)}, ÷ ,{float(num2)} adalah = {h4}")
    
print("\n\nProgram selesai\nRate bang\n\nProgram Finished\nRate it bro")