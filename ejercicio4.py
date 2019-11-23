cantPersonas=int(input("Ingrese la cantidad de personas a registrar: "))

diccionario={}#Declaración diccionario

#ciclo para ingresar los datos segun la cantidad de personas
for i in range(cantPersonas):
    print("Ingrese los datos de la Persona: #",(i+1))
    documento=input("Ingrese el número de documento: ")
    nombre=input("Ingrese el nombre: ")
    edad=input("Ingrese la edad: ")
    estaura=input("Ingrese la estatura: ")
    diccionario[documento]={"id":documento,"nombre":nombre,"edad":edad,"estatura":estaura}#definir diccionario,
    #se asigna un identificador al diccionario y dentro de este se definen los par clave:valor
    print("\nRegistro exitoso!!!!!\n")

menu="¿Desea Consultar registro?\n\n"
menu+="1. Si\n"
menu+="2. No\n\n"
menu+="Ingrese según corresponda: "

consulta=int(input(menu))
print()

#validación para buscar el número de documento en el diccionario, si esta arroja toda la informacion del usuario
if consulta==1:
        id=input("Ingrese el documento de la persona que desea consultar: ")
        if id==documento:
            print("\nSus datos son :\n")
            print("Nombre: ",diccionario[id]["nombre"])#busca en el diccionario el identificador y arroja el par clave:valor
            print("Documento: ",diccionario[id]["id"])
            print("Edad: ",diccionario[id]["edad"])
            print("Estatura: ",diccionario[id]["estatura"])
        else:
            print("\nEl usuario no se encuentra registrado!!!!!!!")
            
else:
    print("Ha Salido del sistema!!!")    

