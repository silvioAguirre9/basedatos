import json
import os

#BLOQUE APERTURA ARCHIVO JSON
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER + '/DB/' 'base_de_datos.json') 
# --> Función Leer archivo JSON   
def leer_json():
    with open (my_file, "r") as f:
        datos = json.load(f)
        f.close()
        return datos
datos = leer_json()
# --> Función modificar JSON
def modificar_json():
    with open (my_file, "w") as modid:
            json.dump(datos, modid, indent=4)
            modid.close()



class Persona(object):
    contador_id = datos["Configuraciones"][0]["contador_id_db"]
    def __init__(self, nombre, apellido, apodo, telefono, direccion):
        print("El contador está en: ", Persona.contador_id)
        self.id = Persona.contador_id #Atriuto id es igual a la variable
        self.nombre = nombre
        self.apellido = apellido
        self.apodo = apodo
        self.telefono = telefono
        self.direccion = direccion



    def crear_contacto(self):    
            datos["Configuraciones"][0]["contador_id_db"]+=1 #Cambiamos el valor de "contador_id_db" (en la base de datos)
            modificar_json()
            print("El contador está ahora en: ", datos["Configuraciones"][0]["contador_id_db"])
            Persona.contador_id +=1 #Sumamos uno a la variable contador_id de la clase
        #Creamos nueva instancia
            nueva_persona = Persona(
                self.nombre,
                self.apellido,
                self.apodo,
                self.telefono, 
                self.direccion).__dict__ 
            datos['Personas'].append(nueva_persona) 
            modificar_json()


    def leer_contacto(atr, valor):
        encontradas = {} 
        for persona in datos["Personas"]: 
            if persona[atr] == valor or valor == 'all': 

                indice = datos["Personas"].index(persona) 

                encontradas[indice] = persona 
        return (encontradas) 
    
    
    def actualizar_contacto(id, atr, nuevo_valor):
        for persona in datos["Personas"]:
            if persona["id"] == id: 
                print (persona) 
                
                #Obtenemos el indice de esa persona
                indice = datos["Personas"].index(persona) 
                datos["Personas"][indice][atr] = nuevo_valor 
                modificar_json()
            

    def eliminar_contacto(id):
        for persona in datos["Personas"]: 
            if persona["id"] == id: 
                print ("Se va a borrar: ", persona) 
                
                
                indice = datos["Personas"].index(persona) 
                datos["Personas"].pop(indice) 
                modificar_json()



# persona_test1 = Persona("Mariano", "Laca", "Pyromaniac", "34343434", "pythones.net")
# persona_test1.crear_contacto()
# persona_test2 = Persona("Mar", "Paredes", "el loco", 343455555, "los buitres 123")
# persona_test2.crear_contacto()
# persona_test3= Persona("Marcos", "Talo", "El pepo", 343455555, "sin nombre 123")
# persona_test3.crear_contacto()

# Persona.actualizar_contacto(1, "Apellido", "Waldowf")

# persona_test1 = Persona("Silvio", "Aguirre", "Negro", "3765050605", "tumamá")

# persona_test1.crear_contacto()


# print(Persona.leer_contacto("Nombre", "Mariano"))

# Persona.eliminar_contacto(5)