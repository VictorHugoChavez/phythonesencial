from __future__ import division


x=10
y=50

resultado=x+y
resta=x-y
multiplicacion=x*y
divisionx=x//y #redonde los valores
division2=x/y # da valores exactos
print(resultado)
print(resta)
print(multiplicacion)
print(divisionx)
print(division2)
pago=False;

#Operacione logicas
# == igual
# != diferente
# <= mayor igual
# => menor igual
# and  
# or
# not
#
#
#



edad=21
if  not(edad>18 and edad<20): 
    print("Edad es 19");
    #if pago==True:
     #   print("Entonces eres mayor y pagaste");
    #else:
     #   print("Eres mayor de edad y no pagaste");
else:
    print("Edad es otro valor a 19 ")

#while  o  mientras
numerowhile=0

while(numerowhile<100):
    print("El valor de numero es ", numerowhile )
    numerowhile+=1


#funciones

def saludos():
    print("Hola desde una funcion")

def despedida():
    print("adios")

saludos()
despedida()

def saludos2(nombre):
    print("Hola mi nombre es " + nombre)

saludos2("Victor 2014110239") 

#def sumar(numero1,numero2=0) asi evitamos errores

def sumar(numero1,numero2):
    resultado=numero1+numero2
    return resultado


valor=sumar(10,18)
print(valor)

#tupla

tupla=(21,1.75,"Victor")

print(tupla[0])

indice=0
while(indice<len(tupla)):
    print(tupla[indice])
    indice+=1

#for
print("#####################################")
tupla=(1,891,3454,6142,"Victor","Neto","SAO")
indice=0
for numeros in tupla:
    print(numeros)


#listas len=javascript es el lenght

print("#####################################")
lsita2=['Corre','Platicar',546,156]
lista=['Slatar','caminar',9746,552432]

print(len(lista))

for elemento in lista:
    print(elemento)

#esto es para sumar las listas que tenemos 
#lsitaf=lista+lsita2
#print(lsitaf)


#esto  indica que si anda un numero en uan lista, busca los valores
if 9746 in lista:
    print('Si')
else:
    print('No')

#para imprimir u obtner solo unos valores de una lista es nesesario que 
# indicarle los rangos de valores que se requieren

print(lista[1:3]) # es importante recordar que solo obtiene dos valores el 1 la psicion del 2
#si le indicamos [1:] toma des de la posicion 1 en adelante
#viseversa [:3] toma todos los valores hasta la posicion 3

print("#####################################")
print("Valores negativos")
print(lista[-1])#accede al ultimo valor 

#se puede decir que se rocorre de atras 

print("#####################################")
print("DICCCIONARIO")

diccionario={'Victor':25,'Hugo':29,'Ernesto':28,'Ana Karen':26}

print(diccionario['Victor'])

print(len(diccionario))


print("#####################################")
print("funciones proporcionadas")
tupla3=(2,5,6)
#help(tupla3)

print("#####################################")
print("funciones type")
x=2565
y=True
print(type(x))
print(type(y))


print("#####################################")
print("funcion str")#trasnforma un valor en una cadena y viceversa
numeroenterio=10
numero2d=15
print(str(numeroenterio)+str(numero2d))

print("#####################################")
print("funcion dir")
tuplaxs=(1,2,3,4,6,8,4)
print(dir(tuplaxs))


print("#####################################")
print("POO")

class Persona:
    nBrazos=0
    npriernas=0
    cabello=True
    cCabello="Defecto"
    hambre=0
    def __init__(self):
        self.nBrazos=2
        self.npriernas=2

    def dormir():
        pass
    def comer(self):
        self.hambre=0

class Hombre(Persona):
    nombre="Defecto"
    sexo="M"

    def cambiarNombre (self,nombre):
        self.nombre=nombre

class Mujer (Persona):
    nombre="Defecto"
    sexo="F"

jose=Hombre()
jose.comer()
print(jose.hambre)


