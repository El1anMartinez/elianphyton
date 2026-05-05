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
# import time
# import random 
# c1=0
# c2=0
# peleador1=input("Ingrese el nombre de su peleador ")
# peleador2=input("Ingrese el nombre del otro peleador ")
# while c1<=100 or c2<=100:
#  golpe1=random.randint(7,18)
#  golpe2=random.randint(7,18)
#  time.sleep(1)
#  print (f"{peleador1} da un golpe de {golpe1} de daño ")
#  c2=c2+golpe1
#  time.sleep(1)
#  print (f"{peleador2} da un golpe de {golpe2} de daño ")
#  c1=c1+golpe2
# if c1>c2:
#     print (f"{peleador2} es el ganador ")
# else:
#     print (f"{peleador1} es el ganador ")
 
# import random 
# codigo=random.randint(7000,21000) 
# print(f"tu codigo es {codigo}")
# print("1.- VIP ")
# print("2.- General ")
# print("3.- Tribuna ")
# op=int(input())

# if op==1:
#  print (f"el precio solo de la entrada es de {40000*1.8}")
#  pf=40000*1.8
# elif op==2:
#  print (f"el precio solo de la entrada es de {40000*1.4}")
#  pf=40000*1.4
# elif op==3:
#  print (f"el precio solo de la entrada es de {40000*1.2}")
#  pf=40000*1.2
# else:
#   print ("entrada no valida")

# if codigo>6999 or codigo<21001:
#  pf=pf*0.90
# print(f"el precio a pagar con el descuento será de {pf}")

import time
import random 
# num1=random.randint(1,9)
# num2=random.randint(1,9)
# num3=random.randint(1,9)
# nums=0
# print (f"Los numeros generados son {num1} {num2} {num3} ")
# t1=False
# t2=False
# t3=False
# while not t1 or not t2 or not t3:
    
#     numerito=random.randint(1,9)
#     print(f"El numero es {numerito} ")
#     time.sleep(1)
#     if numerito==num1:
#         t1=True
#     if numerito==num2:
#         t2=True
#     if numerito==num3:
#         t3=True
#     nums=nums+1
# print (f"GANASTE, en {nums} turnos ")

g=int(input("Cuanto pesa su producto? (En Gramos): "))
sodio=int(input("Cuanto sodio tiene su producto? (entre 1 y 100): "))
envio=int(input("Donde se enviará la lata? (1.-Nacional o 2.-Internacional): "))
lugar=(input("Hacia que sector se enviará la lata?: "))
laton=""


if g<=500:
    print ("Su lata es tamaño normal")
    tipo="Su lata es tamaño normal"

elif g>500 and g<1499:
    print ("Su lata es tamaño mediano")
    tipo="Su lata es tamaño mediana"

elif g>1500:
    print ("Su lata es tamaño grande ")
    tipo=("Su lata es Tamaño grande")




if sodio>=5 and sodio < 9 :
    print ("Su lata es especial")
    laton=("especial ")
elif sodio >= 9 :
    print ("Su lata es acorazada ")
    laton=("acorazada ")



if envio==2:
    print ("Lata con Sticker de Validación Sanitaria")
    sanitaria=("con validacion sanitaria")
else: 
    print ("Lata sin sticker de Validación Sanitaria")
    sanitaria=("sin validacion sanitaria")

print (f"{g}gr , {sodio}% de sodio , {tipo} , {sanitaria}, {laton}y su envio se dirige hacia {lugar}")

