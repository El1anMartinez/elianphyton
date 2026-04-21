#Pedir 2 numeros al usuario y mostrar su suma y resta
# numero1=int(input("Ingrese un numero "))
# numero2=int(input("ingrese otro numero "))
# resultadosuma=numero1+numero2
# resultadoresta=numero1-numero2
# print("El resultado de la suma es ",resultadosuma)
# print("El resultado de la resta es ",resultadoresta)

# titulo="clima actual" #tipo 
# diadelmes=16 #int numero entero
# mes=4 #int numero entero
# temp=18.6 #float numero decimal
# llueve=False

# print(f"{titulo}")
# print(f"fecha hoy: {diadelmes} {mes}")
# print(f"temperatura hoy {temp} grados")

# if llueve :
#     print ("saco el paragua")
# else:      
#     print("no saco el paraguas")


# num=int(input("Ingrese un numero: "))
# for i in range(num):
#     print(f"{i+1} Hola bro")

# nombre=input("Ingrese su nombre: ")
# vocales=0
# consonantes=0
# for i in nombre:
#     if i in "aeiouAEIOU":
#         vocales=vocales+1
#     elif i==" ":
#         print()
#     else:
#         consonantes=consonantes+1
# print(f"La cantidad de consonantes son {consonantes}")
# print(f"La cantidad de vocales son {vocales}")

#Control+F Reemplazar

pin=int(input("ingrese un pin de 4 digitos "))


if int(pin)>1000 and int(pin)<9999:
    print ("pin creado")
else:
    print ("pin denegado")