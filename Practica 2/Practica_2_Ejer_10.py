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
#---------------Inciso A: Crear una lista a partir de las notas NO REPETIDAS de todos los estudiantes
def inciso_a(notas):

    print ("\n \n")
    print ("="*50)

    notas= set(notas)

    print (f"Cantidad de notas generales: {len(notas)} \n \n Notas generales: {notas}")



#====================================
#---------------Inciso B: Informar el promedio de notas de cada estudiante
def inciso_b(nombre):

    print ("\n \n")
    print ("="*50)

    promedios = {}

    for i in range(len(nombre)):

        promedios[nombre[i]] = (notas_1[i] + notas_2[i]) / 2

        print(f"El promedio de notas de {nombre[i]} es {promedios[nombre[i]]}")

    return promedios

    


#====================================
#---------------Inciso C: Informar el promedio general de los estudiantes

def inciso_c(notas_generales):

    print ("\n \n")
    print ("="*50)

    p_notas_totales = 0

    for notas in notas_generales:
        p_notas_totales += notas


    print (f"El promedio general del curso es {p_notas_totales / len(notas_generales)}")





#====================================
#---------------Inciso D: Buscar la nota promedio más alta e informar a que estudiante le corresponde
def inciso_d(promedios):

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
#---------------Inciso E: Buscar la nota promedio más baja e informar a que estudiante le corresponde
def inciso_e(promedios):

    print ("\n \n")
    print ("="*50)

    baja = 9999 
    nom_baja = "" 
        
    for elem in promedios:

        if promedios[elem] < baja:
            baja = promedios[elem]
            nom_baja = elem
        
    print (f"El estudiante con la nota más baja es: {nom_baja}")

    



#===================================================================
#******************************     Programa principal


notas_generales = notas_1.copy() + notas_2.copy()

            #// Aplico filtros para guardar en "nom" únicamente elementos que contengan el nombre de cada alumno, sin contar comillas ni comas u espacios.
nom = nombres.split(",")
nom = list(map(lambda x: x.replace(' ', '').replace("'", '').replace('\n', ''), nom))




inciso_a(notas_generales.copy())
x = inciso_b(nom)
inciso_c(notas_generales)
inciso_d(x)
inciso_e(x)
