#EXPLICACION Y EJEMPLOS DE WHILE
# cont=1
# while cont<3:
#     print(f"El contador es {cont} ")
#     cont=cont+1

# pin=5656
# num=int(input("Ingrese su PIN "))
# while num!=pin:
#     print("Error, Intente denuevo")
#     num=int(input("Ingrese su PIN "))
# print("A ingresado correctamente")

# num=int(input("ingrese un numero: "))

# print(f"{num} X 1 = ", num*1)
# print(f"{num} X 2 = ", num*2)
# print(f"{num} X 3 = ", num*3)
# print(f"{num} X 4 = ", num*4)
# print(f"{num} X 5 = ", num*5)
# print(f"{num} X 6 = ", num*6)
# print(f"{num} X 7 = ", num*7)
# print(f"{num} X 8 = ", num*8)
# print(f"{num} X 9 = ", num*9)
# print(f"{num} X 10 = ", num*10)

# num=int(input("ingrese un numero: "))
# c=1
# while c<=10:
#     print(f"{num}x{c}= {num*c}")
#     c=c+1





def tabla():
    num=int(input("ingrese un numero: "))
    print(f"{num} X 1 = ", num*1)
    print(f"{num} X 2 = ", num*2)
    print(f"{num} X 3 = ", num*3)
    print(f"{num} X 4 = ", num*4)
    print(f"{num} X 5 = ", num*5)
    print(f"{num} X 6 = ", num*6)
    print(f"{num} X 7 = ", num*7)
    print(f"{num} X 8 = ", num*8)
    print(f"{num} X 9 = ", num*9)
    print(f"{num} X 10 = ", num*10)
def vocales():
    nombre=input("Ingrese su nombre: ")
    vocales=0
    consonantes=0
    for i in nombre:
      if i in "aeiouAEIOU":
        vocales=vocales+1
      elif i==" ":
        print()
    else:
        consonantes=consonantes+1
    print(f"La cantidad de consonantes son {consonantes}")
    print(f"La cantidad de vocales son {vocales}")
def pin():
   pin=5656
   num=int(input("Ingrese su PIN "))
   while num!=pin:
     print("Error, Intente denuevo")
     num=int(input("Ingrese su PIN "))
   print("A ingresado correctamente")


while op!=4:
    op=int(input("ingrese una opcion"))
    print("1.- Tabla de multiplicar")
    print("2.- Identificar vocales de nombre")
    print("3.-PIN")
    print("4.-Salir")

match op:
    case 1:
       tabla()
    case 2:
       vocales()
    case 3: 
       pin()
    case _:
       print("opcion invalida")