
import requests
from datetime import datetime

#funcion para validar el nombre de la moneda ingresada
def es_moneda(cripto):
    if cripto in monedas:
        return True
#función para validar el código de usuario
def validar_codigo(codigo):
    if codigo == "12345":
        return True
    
headers = {'Accepts':'application/json','X-CMC_PRO_API_KEY':'d79cbc11-ce2e-4b4c-a268-83a751ed4352'}
  
#obtencion de los nombres de las monedas en Coinmarketcap, guardandolas en la tupla monedas  
monedas_lista=[]    
data = requests.get("https://api.coinmarketcap.com/v2/listings/", headers=headers).json()
for cripto in data["data"]:
        monedas_lista.append(cripto["symbol"])        
monedas = tuple(monedas_lista)

#url para la cotizacion en dolares de las criptomonedas
url = "https://api.binance.com/api/v3/ticker/price?symbol="

#funcion para cotizar la moneda en dolares
def cotizacion(moneda):
    cotiz = requests.get(url+moneda+"USDT").json()
    return cotiz["price"]

#Diccionario con el saldo de cada una de las monedas
saldo_monedas = {}
for i in monedas:
    saldo_monedas[i] = 0
    
#archivo para guardar el historial de transacciones
historial = open("Historial.txt","a")
historial.close()

#variables para la seleccion de opciones por parte del usuario
opcion = 1
opciones = "123456"
    
#Menu de opciones para el usuario
print("**************************")       
print("* Bienvenido a su Wallet *")
print("**************************")
print("***** Usuario: 12345 *****")

while opcion == 1:
    print("\n")
    print("1- Recibir cantidad")
    print("2- Transferir monto")
    print("3- Balance de moneda")
    print("4- Balance general")
    print("5- Histórico de transacciones")
    print("6- Salir de Wallet\n")
    eleccion = input("elija una opción: ")
    
    while eleccion not in opciones:
        print("opción no válida.")
        eleccion = input("Elija una opción: ")
        
    if eleccion == "1":
        moneda = input("ingrese la moneda: ")
        while not es_moneda(moneda):
            print("La moneda ingresada no es válida.")
            moneda = input("ingrese la moneda: ")
        cantidad = float(input("ingrese cantidad que recibe: "))
        usuario = input("ingrese el código del enviador: ")
        while validar_codigo(usuario):
            print("Usted no puede enviarse a si mismo.")
            usuario = input("ingrese el código del enviador: ")
        saldo_monedas[moneda] += cantidad 
        datetime = datetime.now()
        dia_hora = datetime.strftime("%A %d/%m/%Y"+" a las "+"%H:%M:%S")
        data = "El día " + dia_hora + " Recibió del usuario " + usuario + " la cantidad de " + str(cantidad) + " " + moneda + " equivalente a USD " +cotizacion(moneda)+"\n"
        historial = open("historial.txt", "a")
        historial.write(data)
        historial.close()
        print("*operación realizada con exito*")
         
    if eleccion == "2":
        moneda = input("ingrese la moneda: ")
        while not es_moneda(moneda):
            print("La moneda ingresada no es válida.")
            moneda = input("ingrese la moneda: ")
        cantidad = float(input("ingrese cantidad a transferir: "))
        usuario = input("ingrese el código del usuario al que transfiere: ")
        while validar_codigo(usuario):
            print("Usted no puede transferirse a si mismo.")
            usuario = input("ingrese el código del usuario al que transfiere: ")
        saldo_monedas[moneda] -= cantidad 
        datetime = datetime.now()
        dia_hora = datetime.strftime("%A %d/%m/%Y"+" a las "+"%H:%M:%S")
        data ="El día " + dia_hora + " Transfirió al usuario " + usuario + " la cantidad de " + str(cantidad) + " " + moneda + " equivalente a USD " +cotizacion(moneda)+"\n"
        historial = open("historial.txt", "a")
        historial.write(data)
        historial.close()
        print("*operación realizada con exito*")
        
    if eleccion == "3":
        moneda = input("ingrese la moneda: ")
        while not es_moneda(moneda):
            print("La moneda ingresada no es válida.")
            moneda = input("ingrese la moneda: ")
        dolares = float(cotizacion(moneda))
        cant = saldo_monedas[moneda]
        print("Usted tiene ",moneda,": ",cant,"equivalente a USD ",dolares*cant)
            
    if eleccion == "4":
        total_dolares = 0
        print("\nBalance de sus monedas:\n")
        for i in saldo_monedas:
            if saldo_monedas[i] != 0:
                dolares = float(cotizacion(i))
                cant = saldo_monedas[i]
                print(i,":",cant,"=>","dolares:",dolares*cant)
                total_dolares += (dolares*cant) 
        print("\nUsted tiene un total de",total_dolares, "dolares")
        
    if eleccion == "5":
        historial = open("historial.txt","r")
        hist = historial.read()
        historial.close()
        lineas = hist.splitlines()
        print("Historial de transacciones:\n")
        for linea in lineas:
            print(linea)
                
    if eleccion == "6":
        opcion = 0
else:
    print('\n"Saliendo de su Wallet"')
    print('\n"Hasta luego"')

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




















