#Uso Y Ejemplos De Random

# import random 
# num=random.randint(1,10)
# print(num)

# for i in range(num):
#     print ("hola elian")
# num=random.randint(1,10)

# dado1=random.randint(1,6)
# dado2=random.randint(1,6)

# print(f"El dado 1 dió {dado1}")
# print(f"El dado 2 dió {dado2}")

# if dado1==dado2:
#     print ("Se Va A La Carcel")
# else:
#     print ("Avance Por Favor")


# numrandom=random.randint(1,100)
# for i in range (5):
#  adivinar=int(input("Adivine el numero: "))
#  if adivinar>numrandom:
#     print ("Menos")
#  else:
#    print("Más")
#  if adivinar==numrandom:
#    print (f"Usted a adivinado el numero era {numrandom}")
#    break
# else:
#     print (f"Usted no a adivinado el numero era {numrandom}")
import time
import random 
c1=0
c2=0
peleador1=input("Ingrese el nombre de su peleador ")
peleador2=input("Ingrese el nombre del otro peleador ")
while c1<=100 or c2<=100:
 golpe1=random.randint(7,18)
 golpe2=random.randint(7,18)
 time.sleep(1)
 print (f"{peleador1} da un golpe de {golpe1} de daño ")
 c2=c2+golpe1
 time.sleep(1)
 print (f"{peleador2} da un golpe de {golpe2} de daño ")
 c1=c1+golpe2
if c1>c2:
    print (f"{peleador2} es el ganador ")
else:
    print (f"{peleador1} es el ganador ")
 

  


