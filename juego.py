# #hijo prodigo
# nombre = input("Ingrese su nombre: ")
# #variables
# dinero = 100
# dignidad = 50
# hambre = 0
# #mensaje
# print(f"{nombre} ha recibido su Herencia")
# print("Que desea hacer con su herencia?")
# print("1 Gastarlo todo en Fiestas")
# print("2 Invertir")
# print("2 Ahorrar")

# opcion = int(input("Elige una opcion: "))
# if opcion == 1:
#     dinero = 0
#     dignidad -=20
#     hambre = 50
# elif opcion == 2:
#     dinero +=20
# elif opcion == 3:
#     print("Ahorraste tu dinero Felicidades!!!...")
# else:
#     print("Esta opcion es invalida")
    
# #gastar(dinero, dignidad)
# #trabajar(dinero, hambre)

# def gastar(dinero, dignidad):
#     dinero -=30
#     dignidad -=10
#     return dinero, dignidad

# def trabajar(dinero, hambre):
#     dinero +=15
#     hambre +=5
#     return dinero, hambre

# #Bucle
# while dinero > 0:
#     print ("Sigues viviendo lejos de casa...")
#     dinero -=10
    
#Creando la Clase
class HijoProdigo :
    def __init__(self, nombre):
        self.nombre = nombre
        self.dinero = 100
        self.dignidad = 50
        self.hambre = 0
        self.arrepentimiento = 0
        
#Creando los metodos para la clase
    def gastar_todo(self):
        self.dinero = 0
        self.dignidad -= 20
        self.hambre += 50
    
    def invertir(self):
        self.dinero += 20
        print("Has invertido sabiamente tu dinero: " , self.dinero)
        
    def ahorrar(self):
        self.dinero += 20
        
    def trabajar(self):
        self.dinero += 15
        
    def reflexionar(self):
        if self.hambre > 40:
            self.arrepentimiento += 10
        
        
jugador = HijoProdigo(input("Ingrese su nombre: "))

print(f"{jugador.nombre} ha recibido su Herencia")
print(f"Dispone de este monto {jugador.dinero}")
print(f"Inicia con una dignidad de {jugador.dignidad}")
print(f"Inicia con una hambre de {jugador.hambre}")

#usando los metodos de la funcion
while jugador.dinero > 0:
    print ("Sigues viviendo lejos de casa...")
    jugador.gastar_todo()
    # jugador.dinero -=10
    jugador.reflexionar()
    
print("El dinero se acabo")
print("Su nivel de arrepentimiento esta en: " , jugador.arrepentimiento)


#usando la funcion en las opciones
opcion = int(input("Elige una opcion: "))
if opcion == 1:
    jugador.gastar_todo()
elif opcion == 2:
    jugador.invertir()
elif opcion == 3:
    jugador.ahorrar()
else:
    print("Esta opcion es invalida")