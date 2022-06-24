def tambah(a,b):
    a = a + b
    print (a)
    
def kurang(a,b):
    a = a - b
    print (a)
    
def kali(a,b):
    a = a * b
    print (a)
    
def bagi(a,b):
    a = a / b
    print (a)
    
def pangkat(a,b):
    a = a ** b
    print (a)
    
def akar(a,b):
    a = a // b
    print (a)
    
def sbagi(a,b):
    a = a % b
    print (a)

hz = 50*"↓"
hy = 50*"↑"
ak = 23*"="
ax = 8*"→"
az = 8*"←"
ay = 60*"↑"
at = 60*"↓"

red = '\033[91m'
green = '\033[92m'
blue = '\033[94m'
bold = '\033[1m'
italics = '\033[3m'
underline = '\033[4m'
end = '\033[0m'

a = int(input("First number : \n"))
o = str(input(f"{ak}\n\nOperator : Tambah ( + )\n\nKurang ( - )\n\nKali ( x )\n\nBagi ( ÷ )\n\nPangkat ( ^ )\n\nAkar ( √ )\n\nSisa Bagi ( % )\n\n{ak}\nPilih satu = "))
b = int(input("Second number : \n"))

if o == '+':
    print(green + hz + end)
    print(italics + 'Hasilnya adalah' + end)
    s = tambah(a,b)
    print(green + hy + end)
elif o == '-':
    print(hz)
    kurang(a,b)
    print(hy)
elif o == 'x':
     print(hz)
     kali(a,b)
     print(hy)
elif o == '÷':
    print(hz)
    bagi(a,b)
    print(hy)
elif o == '^':
    print(hz)
    pangkat(a,b)
    print(hy)
elif o == '√':
    print(hz)
    akar(a,b)
    print(hy)
elif o == '%':
    print(hz)
    sbagi(a,b)
    print(hy)

print(f"{red}\n\n\n\n\n{ay}\n\n{blue}              VALKULATOR v2 FINISHED{red}\n\n{at}{end}")