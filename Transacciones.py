import library #Importamos el módulo que tendrá nuestras principales librerías y funciones

@library.click.group # Nos permite definir un grupo de comandos que estarán en esta misma estructura de CLI
def trans(): #Definimos como trans a nuestro grupo de comandos bajo el que desarrollaremos nuestro CLI para este proyecto
    pass

@trans.command() # Nos permite definir comandos con instrucciones específicas
def imprimir_reporte_transacciones():
    #Asignamos valores a las variables para nuestro reporte de acuerdo a nuestra función reporte1_transacciones
    id_transaccion, balance_total, monto_max, quant_trans_credito, quant_trans_debito = library.reporte1_transacciones('data.csv')
    #Definimos la estructura del reporte y que nos ayudarà para el impresión tabular
    reporte=[
        ["Balance Final: ",f"S/. {balance_total:.2f}"],
        ["Transacción de Mayor Monto: ",f"ID: {id_transaccion} - S/. {monto_max:.2f}"],
        ["Reconteo de Transacciones: ",f"Crédito: {quant_trans_credito}, Débito: {quant_trans_debito}"]
    ]

    print("Reporte de Transacciones")
    print(library.tabulate(reporte,headers=["Detalle","Resultado"],tablefmt="pretty"))


@trans.command()
def mostrar_transacciones():
    data=library.leer_csv('data.csv')
    if data: #Definimos este condicional para que solo imprima el csv si es que hay contenido
        print(library.tabulate(data,headers='keys',tablefmt='pretty'))#La función tabulate nos ayuda a imprimir los datos en forma tabular
    else:
        print("No hay datos de transacción para mostrar.")

if __name__ == '__main__': #Definimos que solo proceda a ejecutarse el CLI que venga desde nuestro archivo principal
    trans()
