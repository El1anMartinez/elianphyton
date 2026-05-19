# while True:
#     try:
#         num=int(input("ingrese un numero: "))
#     except ValueError as er:
#         print(f"Error {er}")
#         print ("Solo debe ingresar numeros enteros")


# op=0
# total=0
# while op!=4:
#     try:
#         print ("1.- PC $500.000")
#         print ("2.- LGTV 55 pulgadas $450.000")
#         print ("3.- Microondas Mademsa $100.000")
#         print ("4.- Salir ")
#         print ("Seleccione una opción")
#         op=int(input())
#     except ValueError as e:
#         print(f"Error {e}")
#         print ("Solo se aceptan numeros enteros")
#     match op:
#         case 1: 
#             print ("Total a pagar es ",500000*1.19)
#             total=total+500000*1.19
#         case 2:
#             print ("El total a pagar es ", 450000*1.19)
#             total=total+450000*1.19
#         case 3:
#             print ("El total a pagar es ",100000*1.19)
#             total=total+100000*1.19
#         case 4:
#             print ("Saliendo Del Programa")
#             print (f"El total a pagar es de {total}")
# while True:
#     try:
#         notas=int(input ("Ingrese la cantidad de notas: "))
#         break
#     except:
#         print ("Solo numeros enteros")
# suma=0
# for i in range(notas):
#     while True:
#         try:
#             n=float(input(f"ingrese la nota {i+1}: "))
#             break
#         except ValueError as e:
#             print("solo numeros decimales")
#         suma=suma+n
#         prom=suma/notas
# print("El Promedio es" , round(prom,1))
# if prom>=4:
#     print ("Alumno Aprobado")
# else:
#     print ("Alumno Reprobado")
# while True:
#     try:
#         pas=int(input("Cuantos pasajes desea llevar?: "))
#         break
#     except ValueError as e:
#         print(f"Error {e}")
#         print("Solo numeros enteros")

# while True:
#     try:
#         pas=int(input("Cuantos pasajes desea llevar: "))
#         break
#     except ValueError as e:
#         print("Error", e)
#         print("Solo numeros enteros")
# total=0
# for i in range(pas):
#     while True:
#         try:
#             precio=int(input(f"Cuanto vale el pasaje {i+1}: "))
#             break
#         except ValueError as a:
#             print("Error", a)
#             print("Solo numeros enteros")
#     total=total+precio
# print(f"El precio total a pagar es de {total}")


# Registro de juegos
# indie=0
# estudio=0
# ce=0
# c12=0
# cm=0
# try:
#     nj=int(input("Cuantos juegos son?: "))
# except ValueError as a:
#     print("Solo numeros")
#     print(f"Error {a}")
# for i in range(nj):
#     nombre=input("Ingrese nombre del Juego: ")
#     if len(nombre) < 5:
#         print("Nombre muy corto")
#         break
#     elif " " in nombre:
#         print("No debe tener espacios")
#         break
#     elif nombre.isupper()==False:
#         print ("Debe estar en mayusculas")
#         break
#     try:
#         precio=int(input("Ingrese el Precio: "))
#         if precio <=0:
#             print("Precio invalido")
#     except ValueError as b:
#         print ("Debe ingresar numeros")
#         print(f"Error {b}")
#     if precio >20000 and precio<40000:
#         indie=indie+1
#     elif precio >=40000:
#         estudio=estudio+1
#     try:
#         edad=int(input("Ingrese edad recomendada:"))
#     except ValueError as c:
#         print("Solo numeros")
#         print(f"Error {c}")
#         break
#     if edad < 12:
#         ce=ce+1
#     elif edad >=12 and edad <=17:
#         c12=c12+1
#     else:
#         cm=cm+1
# print(f"indies {indie}")
# print (f"estudio {estudio}")
# print(f"clasificacion E {ce}")
# print(f"clasificacion 12 {c12}")
# print(f"clasificacion M {cm}")




credito=100000
compras=3
op=0
print("1.-Pago de Tarjeta")
print("2.-Simulacion de compras")
print("3.-Salir")
op=int(input())
while op!=3:
    match op:
        case 1:
            print("Pagar Credito")
            try:
                pagar=int(input("Ingrese monto a pagar: "))
            except ValueError as a:
                    print("Solo numeros")
                    print(f"Error {a}")
            if pagar>=0 and abs(credito):
                credito=credito-pagar
                break
            else:
                print("Monto invalido")
            print (f"Su Credito Queda En {credito}")
                
            if pagar>credito:
                print ("Exceso De Saldo")
        case 2:
                print("Simulacion de compras")
                for i in range (compras):
                 while True:
                    try:
                        c1=int(input("ingrese el monto de la compra"))
                        c2=int(input("ingrese el monto de la compra"))
                        c3=int(input("ingrese el monto de la compra"))
                    except ValueError as b:
                        print("Solo numeros")
                        print(f"Error {b}")

