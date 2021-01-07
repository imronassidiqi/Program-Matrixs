import numpy as np
print("Penjumlahan Matrik Ordo 2x2")
print()
print("matriks 1")
a = int(input("baris 1, kolom 1 : "))
b = int(input("baris 1, kolom 2 : "))
c = int(input("baris 2, kolom 1 : "))
d = int(input("baris 2, kolom 2 : "))
x = np.array([(a,b),(c,d)])

print()
print("matriks 2")
e = int(input("baris 1, kolom 1 : "))
f = int(input("baris 1, kolom 2 : "))
g = int(input("baris 2, kolom 1 : "))
h = int(input("baris 2, kolom 2 : "))
y = np.array([(e,f),(g,h)])

print()
print("matriks 1 :\n",x)
print()
print("matriks 2 :\n",y)
print()

for n in range(0, len(x)):
  for m in range(0, len(x[0])):
    hasil=print((x[m][n] + y[m][n]),end=' '),
  print
