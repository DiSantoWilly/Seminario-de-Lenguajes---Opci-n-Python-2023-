nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 'David',
'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 'Francsica', 
'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 'Joaquina', 'Jorge',
'JOSE', 'Javier', 'Joaquín'  , 'Julian', 'Julieta', 'Luciana','LAUTARO', 'Leonel', 'Luisa', 
'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 'Nicolás',  'Nancy', 'Noelia', 'Pablo', 
'Priscila', 'Sabrina', 'Tomás', 'Ulises', 'Yanina' '''
notas_1 = [81,  60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 12, 77, 
           13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 85, 73, 37, 42, 95, 18, 7, 
           74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37, 64, 13, 8,
           87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73, 95, 19, 47, 15, 31,
           39, 15, 74, 33, 57, 10]



#====================================
#---------------Inciso A

print ("\n \n")
print ("="*50)

notas_generales = notas_1.copy() + notas_2.copy()


print (f"Cantidad de notas generales: {len(set(notas_generales))} \n \n Notas generales: {set(notas_generales)}")



#====================================
#---------------Inciso B

print ("\n \n")
print ("="*50)

baja = 9999 #/////////////////////////////////ESTA VARIABLE CORRESPONDE AL INCISO E
nom_baja = "" #/////////////////////////////////ESTA VARIABLE CORRESPONDE AL INCISO E

promedios = {}

nom = nombres.split(",")

for i in range(len(nom)):
    nom[i] = nom[i].replace(' ', '')
    nom[i] = nom[i].replace("'", '')
    nom[i] = nom[i].replace("\n", '')

    promedios[nom[i]] = (notas_1[i] + notas_2[i]) / 2

    print(f"El promedio de notas de {nom[i]} es {promedios[nom[i]]}")

#/////////////////////////////////ESTA PARTE CORRESPONDE AL INCISO E

    if notas_1[i] < baja or notas_2[i] < baja:
        if notas_1[i] < notas_2[i]:
            baja = notas_1[i]
        else:
            baja = notas_2[i]
        nom_baja = nom[i]
    




#====================================
#---------------Inciso C

print ("\n \n")
print ("="*50)

p_notas_totales = 0

for notas in notas_generales:
    p_notas_totales += notas


print (f"El promedio general del curso es {p_notas_totales / len(notas_generales)}")





#====================================
#---------------Inciso D

print ("\n \n")
print ("="*50)

alta = -1
nom_alta = ""

for elem in promedios:
    if promedios[elem] > alta:
        alta = promedios[elem]
        nom_alta = elem


print (f"El estudiante con nota promedio más alta es: {nom_alta}")




#====================================
#---------------Inciso E

print ("\n \n")
print ("="*50)

print (f"El estudiante con la nota más baja es: {nom_baja}")
