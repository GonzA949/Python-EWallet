import requests #import del requests para utilizar get de las API's
import os #import del OS para limpiar la terminal
from datetime import datetime #import para obtener el dia y hora exacta.

nombre_archivo = "transacciones.txt"  #ARCHIVO DONDE SE ALOJARAN LAS TRANSACCIONES

class Usuario(object): # CLASE USUARIO PARA VALIDAR MOSTRAR CÓDIGO
    def __init__(self, codigo): #Init código Usuario
        self.codigo = codigo
    
    def mostrarCodigo(self): #Funcion que muestra el código del usuario
        return self.codigo

class Criptomoneda(object): #CLASE CRIPTOMONEDA PARA OPERACIONES CON CRIPTOS
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad
    
    def indicarCantidad(self, cantidad):  
        self.cantidad=cantidad

    def mostrarNombre(self):
        return self.nombre
    
    def mostrarCantidad(self):  
        return  self.cantidad
    
    def calcularSaldo(self, cotizacion):  
        return self.cantidad*cotizacion

def esmoneda(cripto):#funcion que verifica que la moneda ingresada se encuentre en las monedas soportadas
    criptos =["BTC","LTC","XRP","ETH"]
    if cripto in criptos:
        return True
    else:
        print ("Ingrese una moneda válida:(BTC,XRP,LTC,ETH)")
    return cripto in monedas

def nombre(cripto): #funcion que recibe el simbolo y retorna el nombre
    monedas_dict={}
    for coin in data["data"]:
        monedas_dict[coin["symbol"]]=coin["name"] 
    return monedas_dict.get(cripto) #devuelve el nombre

#inicializamos elemento
monedas=() #LISTA DE MONEDAS
diccionario={} #DICCIONARIO PARA ALOJAR LOS DATOS DE CRIPTO

COINMARKET_API_KEY = "2448e9c9-b938-4f0e-85f1-9878a7b41c87" # Esta es la llave de la API que nos permite hacer peticiones a la direccion URL de la API
headers = { #esto son los parametros que necesitamos pasar en la peticion para que la API nos pueda devolver la informacion
  'Accepts': 'application/json', # esto indica que el formato de la respuesta de la API sera JSON, que es un formato legible para Python, asi podra usar la informacion 
  'X-CMC_PRO_API_KEY': COINMARKET_API_KEY #aqui asignamos que usaremos la clave de la API que definimos arriba
}

data=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json() #aqui almacenamos  en data el resultado de la peticion a la direccion de la API usando requests.get y pasamos los parametros que definimos arriba

for cripto in data["data"]:# aqui creamos un for para recorrer todos los datos o cripto como se especifica en el for que estan en "data" que es el valor dentro de la variable data que tiene todas las criptomonedas de la API
    diccionario[cripto["symbol"]]=cripto["quote"]["USD"]["price"] #cada que recorremos la data almacenamos en el diccionario los datos de symbolo que es la abreviacion por ejemplo BTC junto con el precio de la moneda que consulta con quote.USD.price en el json
monedas = diccionario.keys() 

def esnumero(numero): #Valida que la cantidad ingresada sea mayor a 0
    if numero > 0.0:
        print ("")
    else:
        print ("")
    return numero
    
def validarCodigo(codigo):# Valida que el código de recepción o envío , sea diferente al del usuario
    if codigo == usuario.codigo:
        print("\n       ¡TRANSACCIÓN FALLÍDA!, el código indicado es inválido")
        return False
    else:
        return True
            
_ENDPOINT = "https://api.binance.com" #dirección de Binance donde toma la variable del precio.

def _url(api): #Funcion de retorno de API
    return _ENDPOINT+api

def get_price(cripto): #Funcion que obtiene el precio de Binance
    data = requests.get(_url("/api/v3/ticker/price?symbol="+cripto)).json()
    precio = float(data["price"])
    return precio

total = 0.0

def GuardarRegistro(moneda, operacion, codigo, cantidad, cantTotal): #Funcion que guarda los registros en el archivo de texto mencionado.
    archivo = open(nombre_archivo,"a")
    dt = datetime.now()
    precio =  get_price(moneda+"USDT")
    archivo.write("\n"+"Fecha"+ ":" + dt.strftime("%A %d/%m/%Y %I:%M:%S%p") +",Moneda" +":"+str(moneda)
        +",Transaccion" +":"+ operacion+",Código de usuario"+ ":"+ str(codigo) + ",Cantidad "+ ":"+ str(cantidad) 
            + ",Total de la operacion en $"+":"+ str(precio*cantidad) +", Total acumulado en cuenta en $" + ":"+ str(precio*cantTotal))
    archivo.close()
    return

usuario = Usuario("NXT2020") #Código proporcionado al usuario
bit = Criptomoneda("BTC",2.5) # Valores de las criptomonedas
ethe = Criptomoneda("ETH",0.6734)
xrp = Criptomoneda("XRP",8.5)
ltc = Criptomoneda("LTC",7.36)
monedas = [bit,ethe,xrp,ltc] #Lista de codigo criptos

def cantidadSuficiente(moneda, cantidad):#Valida que la cantidad de transferencia sea suficiente para que el usuario pueda enviar.
    aux = True
    if(moneda== "BTC"):
        if(bit.cantidad >= cantidad):
            return True
        else:
            aux = False
    if(moneda== "ETH"):
        if(ethe.cantidad >= cantidad):
            return True
        else:
            aux = False
    if(moneda== "XRP"):
        if(xrp.cantidad >= cantidad):
            return True
        else:
            aux = False
    if(moneda== "LTC"):
        if(ltc.cantidad >= cantidad):
            return True
        else:
            aux = False
    if(aux==False):
        print("     ¡TRANSACCION RECHAZADA!, Cantidad de "+ moneda+ " es insuficiente")
        return False

def menu(variable): #Funcion Menu, que retorna cada vez que el usuario indique de comenzar una nueva operación.
    os.system("cls") #Limpia la terminal cada vez que comienza.
    opcion = 0
    if variable == "S":
        #DATOS DE RELEVANCIA
        print ("BIENVENIDO A TU BILLETERA VIRTUAL")
        print ("*********************************")
        print ("Tú código de Usuario es: " + str(usuario.mostrarCodigo()))
        print ("Monedas soportadas: BTC,LTC,ETH,XRP")
        #Menu del Programa
        print ("1-Recibir Cantidad.")
        print ("2-Transferir Monto.")
        print ("3-Mostrar balance de una moneda.")
        print ("4-Mostrar balance general.")
        print ("5-Mostrar histórico de transacciones.")
        print ("6-Salir")
        #Entrada de opción del usuario
        opcion = int (input("Escriba el número de la opción deseada: "))#Input para asignar la opción elegida
        if opcion == 1:
            moneda= input ("Escriba el código de la moneda a recibir: ")
            while not esmoneda(moneda):  #Se inicializa el loop para ver si la moneda existe en coinmarketcap y es soportada por el programa.
                print("Moneda Invalida.")
                moneda=input("Ingrese el nombre de la moneda: ")
            else:
                print("La moneda,",moneda,"es valida porque existe en coinmarketcap.com")
                cantidad = float (input("Ingrese la cantidad a recibir de "+moneda+":"))
            while not esnumero(cantidad): # Inicializo el loop para ver si la cantidad ingresada es un número.
                print ("Cantidad inválida")
            else:
                print ("Cantidad válida")
                codigo = str (input("Ingrese el código: "))
            while not validarCodigo(codigo):
                codigo = int(input("        Ingrese el código del emisor: "))
            if(moneda=="BTC"): # Devuelve la suma de la cantidad preexistente y la cantidad ingresada "nueva"
                bit.indicarCantidad(bit.cantidad + cantidad)
                GuardarRegistro(moneda,"Recibido",codigo, cantidad, bit.mostrarCantidad()) #Se guarda cada registro
            elif(moneda=="ETH"):
                ethe.indicarCantidad(ethe.cantidad + cantidad)
                GuardarRegistro(moneda,"Recibido",codigo, cantidad,ethe.mostrarCantidad())
            elif(moneda=="XRP"):
                xrp.indicarCantidad(xrp.cantidad + cantidad)
                GuardarRegistro(moneda,"Recibido",codigo, cantidad,xrp.mostrarCantidad())
            elif(moneda=="LTC"):
                ltc.indicarCantidad(ltc.cantidad + cantidad)
                GuardarRegistro(moneda,"Recibido",codigo, cantidad,ltc.mostrarCantidad())
            print ("Transacción realizada!")
            regresar = input ("¿Desea volver al menú principal?, escriba S/N: ") #Input para volver al Menu principal
            regresar.upper()
            menu(regresar)
        elif opcion == 2 :
            moneda= input ("Escriba el código de la moneda a Transferir: ")
            while not esmoneda(moneda):  #Inicializo el loop para que se cumpla hasta que sea True 
                print("Moneda Invalida.")
                moneda=input("Ingrese el nombre de la moneda: ")
            else:
                print("La moneda,",moneda,"es valida porque existe en coimnmarketcap.com")
                cantidad = float (input("Ingrese la cantidad a transferir de "+moneda+":"))
            while not cantidadSuficiente(moneda,cantidad): #
                cantidad = float(input("        Ingrese la cantidad a transferir de " + moneda+ ":"))
                codigo = int(input("        Ingrese el código del receptor: "))
            else:
                print ("Cantidad válida")
                codigo = str (input("Ingrese el código de receptor: "))
            while not validarCodigo(codigo):
                codigo = int(input("        Ingrese el código de receptor: "))
            if(moneda=="BTC"):
                bit.indicarCantidad(bit.cantidad + cantidad)
                GuardarRegistro(moneda,"Enviado",codigo, cantidad, bit.mostrarCantidad())
            elif(moneda=="ETH"):
                ethe.indicarCantidad(ethe.cantidad + cantidad)
                GuardarRegistro(moneda,"Enviado",codigo, cantidad,ethe.mostrarCantidad())
            elif(moneda=="XRP"):
                xrp.indicarCantidad(xrp.cantidad + cantidad)
                GuardarRegistro(moneda,"Enviado",codigo, cantidad,xrp.mostrarCantidad())
            elif(moneda=="LTC"):
                ltc.indicarCantidad(ltc.cantidad + cantidad)
                GuardarRegistro(moneda,"Enviado",codigo, cantidad,ltc.mostrarCantidad())
            print ("Transacción realizada!")
            regresar = input ("¿Desea volver al menú principal?, escriba S/N: ")
            regresar.upper()
            menu(regresar)
        elif opcion ==3:
            moneda = input("    Ingrese la moneda a consultar: ") #Input para elegir el balance de la moneda que desea obtener
            while not esmoneda(moneda):
                moneda = input("    Ingrese la moneda a consultar: ")
            precio = get_price(moneda+"USDT")
            if(moneda=="BTC"):
                print("Moneda: " + moneda + " Cantidad: "+ str(bit.mostrarCantidad()) +" Saldo disponible: $."+ str(bit.calcularSaldo(precio)))
            elif(moneda=="ETH"):
                print("Moneda: " + moneda + " Cantidad: "+str(ethe.mostrarCantidad()) +" Saldo disponible: $."+str(ethe.calcularSaldo(precio)))
            elif(moneda=="XRP"):
                print("Moneda: " + moneda + " Cantidad: "+str(xrp.mostrarCantidad()) + " Saldo disponible: $."+str(xrp.calcularSaldo(precio)))
            elif(moneda=="LTC"):
                print("Moneda: " + moneda + " Cantidad: "+ str(ltc.mostrarCantidad()) +" Saldo disponible: $."+str(ltc.calcularSaldo(precio)))
            regresar = input ("¿Desea volver al menú principal?, escriba S/N: ")
            regresar.upper()
            menu(regresar)
        elif opcion ==4:
            moneda = ""
            totalUSD = 0
            for moneda in monedas:
                precio = get_price(moneda.mostrarNombre()+"USDT")
                totalUSD += moneda.calcularSaldo(precio)
                print("Moneda: " + moneda.mostrarNombre() + " Cantidad: "+ str(moneda.mostrarCantidad()) +" Saldo disponible: $."+ str(moneda.calcularSaldo(precio)) +"\n")
            print("El monto acumulado total de todas las criptomonedas es $." + str(totalUSD))
            regresar = input ("¿Desea volver al menú principal?, escriba S/N: ")
            regresar.upper()
            menu(regresar)
        elif opcion ==5: 
            archivo = open(nombre_archivo,"r") #Lectura de archivo de transacciones y print del historial
            texto = archivo.read()
            archivo.close()
            print(texto)
            regresar = input ("¿Desea volver al menú principal?, escriba S/N: ")
            regresar.upper()
            menu(regresar)
        elif opcion ==6:
            SystemExit # Salida del programa
        else:
            print ("Error, Opción Inexistente") # Por si el usuario ingresa una opción que no existe, devuelve error.
            opcion = int (input ("Ingrese la opción nuevamente: "))
    else:
        SystemExit
    return opcion

menu("S") # Inicializa el programa