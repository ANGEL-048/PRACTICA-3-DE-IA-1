import pandas as pd
from tabulate import tabulate
print ("""************
            LUIS ANGEL SANCHEZ
            ISC-181
            ************
            Menu
            SELECCIONA EL PROGRAMA
            1) Ingresar alumnos
            2) Leer archivo y salir""")

def Menu():
    """PRACTICA 3"""
    print ("""************
            LUIS ANGEL SANCHEZ
            ISC-181
            ************
            Menu
            SELECCIONA EL PROGRAMA
            1) Ingresar alumnos
            2) Leer archivo y salir""")



def KOFMETODOSS(opc):
    """PRACTICA 3"""
    
    Menu()

    Nombre=[]
    Apellidos=[]
    Edad=[]
    Grado=[]
    Grupo=[]
    Correo=[]
    Alumnos= {'NOMBRE_DEL_ALUMNO':Nombre , 'APELLIDOS':Apellidos, 'EDAD':Edad, 'GRADO':Grado, 'GRUPO':Grupo, 'CORREO':Correo }
    while (opc >0 and opc <7):
        if (opc==1):
            x = (int(input("Ingrese el numero de alumnos a registrar: \n")))
            rangoo = range(0,x)
            for i in rangoo:

                nombre = (str(input("Ingrese el nombre del alumno: \n")))
                Nombre.append(nombre)
                apellidos = (str(input("Ingrese los apellidos del alumno: \n")))
                Apellidos.append(apellidos)
                edad = (str(input("Ingrese la edad del alumno: \n")))
                Edad.append(edad)
                grado = (str(input("Ingrese el grado del alumno: \n")))
                Grado.append(grado)
                grupo = (str(input("Ingrese el grupo del alumno: \n")))
                Grupo.append(grupo)
                correo = (str(input("Ingrese el correo del alumno: \n")))
                Correo.append(correo)

                print(Alumnos)

                df=pd.DataFrame(Alumnos)
                df.to_csv('C:/Users/Luis/Desktop/INTELIGENCIA ARTIFICIAL I/Parcial 2/alumnosumb.csv')
                Menu()
                opc = int(input("SELECCIONE LA OPCION\n"))

                
        elif(opc == 2):
            datos = pd.read_csv('C:/Users/Luis/Desktop/INTELIGENCIA ARTIFICIAL I/Parcial 2/alumnosumb.csv')
            print (tabulate(datos))
            break

opc1 = int(input("SELECCIONE LA OPCION\n"))
KOFMETODOSS(opc1)
