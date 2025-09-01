#Autor: Antonio Betancourt

# 
print("Hello World")

# definicion a problemas

# solucion a problemas

#Algoritmos

# encuentre el valor de x en la siguiente ecuacion

# AX = B - Z

mensaje = "El valor de la variable es"
#IMPLEMENTAR LA FUNCION INPUT, Y EXPLICAR CADA PARAMETRO EFECTUADO
#A = input("Escriba un numero para la variable A ")
A = int(4)

print(type(A), A)

result = A + A 

print(type(result), result)



#1 Str a Int

B = str(5)

print("B inicial:", B, type(B))

B = int(B)

print("B convertido:", B, type(B))



#2 Float a Int

C = 3.1

print("C inicial:", B, type(B))

C = int(C)

print("C convertido:", B, type(B))


D = 55


print()

# Estructuras de control, operaciones logicas
#Booleano, 1,0,

if(A>5):
    print("Este es el resultado del if verdadero")
    print(f"La variable A es igual a: {A}")
else:
    print("La condicion no se cumplio")

print()


if(B<11):
    print("Este es el resultado del if verdadero")
    print(f"La variable B es igual a: {B}")
else:
    print("La condicion no se cumplio")

print()


if(C<=4):
    print("Este es el resultado del if verdadero")
    print(f"La variable C es igual a: {C}")
else:
    print("La condicion no se cumplio")    

print()


if(D>=55):
    print("Este es el resultado del if verdadero")
    print(f"La variable D es igual a: {D}")
else:
    print("La condicion no se cumplio")

print()
