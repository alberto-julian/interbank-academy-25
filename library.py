#Importamos las librerias:
import click
import csv
#import os
from tabulate import tabulate

#Definimos la función que leerá nuestro archivo csv
def leer_csv(nombre_archivo):
    try:
        with open(nombre_archivo,mode='r',newline='', encoding='utf-8') as data:
            lectura = csv.DictReader(data)
            return [item for item in lectura]
    except FileNotFoundError: #Definimos nuestra gestión de posibles errores al leer el archivo csv
        print(f"El archivo '{nombre_archivo}' no existe")
        crear_csv(nombre_archivo)#Llamamos a la función crear csv
        return [] #Devuelve una lista en caso no encuentre el archivo csv
    except Exception as error:
        print(f"Ocurrió el error al leer la data de: {error}")
        return [] #Devuelve una lista en caso no encuentre el archivo csv

#Definimos nuestra función que nos permitirá crear nuestro csv pero con encabezados ya predefinidos y en caso no lo encuentré en la función de leer csv, nos permitirá crearlo
def crear_csv(nombre_archivo):
    with open(nombre_archivo,mode='w',newline='', encoding='utf-8') as data:
        escritura = csv.DictWriter(data,fieldnames=['id','tipo','monto'])
        escritura.writeheader()
        print(f"El archivo '{nombre_archivo}' ha sido creado con éxito")

#Definimos nuestra función que obtendrá los datos de las variables para nuestro primer reporte
def reporte1_transacciones(nombre_archivo):
    v_balance_total = 0.0
    v_quant_trans_credito = 0
    v_quant_trans_debito = 0
    v_monto_max = 0.0
    v_id_trans = None

    with open(nombre_archivo,mode='r', encoding='utf-8') as data:
        lectura = csv.DictReader(data)
        for item in lectura:
            vt_monto = float(item['monto']) #Nos aseguramos que el tipo de dato extraído sea float (numérico)
            vt_tipo_trans=item['tipo'].strip() #Eliminamos posibles espacios en la información para evitar error en el procedimiento

            if vt_tipo_trans == "Crédito":
                v_balance_total += vt_monto
                v_quant_trans_credito += 1
            elif vt_tipo_trans == "Débito":
                v_balance_total -= vt_monto
                v_quant_trans_debito += 1

            if vt_monto>v_monto_max:
                v_monto_max=vt_monto
                v_id_trans=item['id']

    return v_id_trans, v_balance_total, v_monto_max,v_quant_trans_credito, v_quant_trans_debito