a = int(input("Līdz kuram skaitlim: "))
for i in range(8, a):
 print(i+1)
s = 0
for i in range(9, a+1):
 s = i + s
print("Summa ir",s)