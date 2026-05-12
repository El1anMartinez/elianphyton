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

while True:
    try:
        pas=int(input("Cuantos pasajes desea llevar: "))
        break
    except ValueError as e:
        print("Error", e)
        print("Solo numeros enteros")
total=0
for i in range(pas):
    while True:
        try:
            precio=int(input(f"Cuanto vale el pasaje {i+1}: "))
            break
        except ValueError as a:
            print("Error", a)
            print("Solo numeros enteros")
    total=total+precio
print(f"El precio total a pagar es de {total}")