> .[!NOTE].
> Esta es una elaboración principalmente académica

# Reto Técnico: Procesamiento de Transacciones Bancarias (CLI)

## 1. INTRODUCCIÓN
Esta es una excelente **oportunidad** de desarrollo académico en colaboración entre **Interbank y Codeable** para la postulación a una beca de formación en **COBOL Engineers**.<br> <br>
El **objetivo** de esta iniciativa es demostrar nuestro conocimiento en **programación** y el proyecto consiste en que desarrollemos una aplicación de líneas de comandos (**CLI**) para un **proceso de transacciones bancarias** y brindar un **reporte** que podría ser requerido por una **entidad bancaría** ante un gran volumen de datos.

## 2. TECNOLOGÍAS UTILIZADAS
### 2.1. Lenguaje
- Python: Se requiere instalar [Python](https://www.python.org/downloads/)

### 2.2. Programas
- PyCharm: Encontramos un versión educativa y [trial profesional](https://www.jetbrains.com/es-es/pycharm/download/?section=windows)
- GitHub: Para instalar [Git](https://git-scm.com/) y [GitHub](https://desktop.github.com/download/)

## 3. MODELADO
### 3.0. INSTALACIÓN PREVIA
#### 3.0.1 En Terminal:
>.[!TIP].
> Si deseas realizar la manipulación de la aplicación sin afectar el resto de tus proyectos podrías inicializar un entorno virtual introduciendo en la terminal:<br><br>
> **python -m venv venv**<br><br> 
> Si deseas activarlo:<br><br>
> **venv\Scripts\active** <br><br>
> Podrás validar que se activo porque en tu terminal se añadió la sigla *(venv)*

- click:
>pip install click
- tabulate:
>pip install tabulate

#### 3.0.2 En Librerías:
- click: Para definir grupos de líneas de comando
> import click
- csv: Para la lectura de archivos csv
> import csv
- tabulate: Para el ordenamiento de la información al imprimir el reporte, al definirlo con **from** nos ayuda a solo importar una función específica *tabulate*, qué es la que principalmente usaremos en este proyecto.
> from tabulate import tabulate

### 3.1. ESTRUCTURA
#### 3.1.0 Archivos
Consiste de los siguientes archivos:
- data.csv: Archivo que contiene todas las transacciones y su información
- README.md: Readme del reto
- README - PROYECTO.md: Readme propio del desarrollo del proyecto
- library.py: Módulo para almacenar funciones recurrentes y librerias para el proyecto
- Transacciones.py: Módulo principal que tendrá definido las líneas de comando para el proyecto

#### 3.1.1 Lógica
- Entorno de librería y funciones principales:<br>
Al desconocer la data y la cantidad de funciones que requeriría el proyecto, se procede a elaborar un módulo adicional llamado **library.py** para almacenarlas. Este será llamado en nuestro módulo principal **Transacciones.py**.
- Definimos la primera situación en qué no se encuentre la data requerida y para evitar un error sobre ello, definimos la función **crear_csv(nombre_archivo)**, que creará el csv con el nombre que le definamos.
- Seguidamente, para entender la estructura de la data,procedemos a crear la función **leer_csv(nombre_archivo)**.
- Luego, procedemos a definir las primeras líneas de comando:
- A continuación, requerimos que podamos visualizar la data y para ello, creamos nuestras primeras líneas de comando, empezando por el nombre del grupo con el comando **@library.click.group**: **trans()**

> .[!IMPORTANT].
> Al utilizar un módulo para almacenar todas nuestras librerías y funciones, para hacer su llamado se tiene que iniciar con el apartado: **library.__NombreFuncion__**
- Dentro de este grupo, definimos la línea de comando: **mostrar_transacciones()** y para la estructura, se hará uso de la función **library.tabulate()**
  - Al terminar este detalle, si en la terminal se escribe: 
  > **python Transacciones.py** <br>
    Nos mostrará un bloque de **Commands**, a los que podremos llamar de la siguiente forma <br>
    **python Transacciones.py comando1**
- Después, al entender la estructura al visualizar las transacciones, procedemos a crear la función **reporte1_transacciones(nombre_archivo)**, que nos ayudará a obtener los valores de las variables que requeriremos para nuestro reporte:
  - v_balance_total: Para Balance Final (Tipo de dato: Float)
  - v_quant_trans_credito: Para la cantidad de transacciones de crédito (Tipo de dato: Entero)
  - v_quant_trans_debito: Para la cantidad de transacciones de débito (Tipo de dato: Entero)
  - v_monto_max: Para el mayor monto de las transacciones (Tipo de dato: Float)
  - v_id_trans: Para capturar el *ID* de la transacción con mayor monto (Tipo de dato: Entero)

> .[!WARNING].
> Es importante que antes de continuar, entiendas que toda la secuencia de códigos trabaja bajo una misma estructura de **data.csv**, que es el archivo que almacena todas las transacciones y su información.

- La lógica para obtener las variables requeridas, sería un **for** para recorrer cada una de las filas mientras se van sumando y restando los montos de crédito y restando los montos de débito. <br> Cabe mencionar, que la lógica puede modificarse como disgregar la función para cada variable para evitar que se recorra todas las filas del archivo en el cálculo de las 4 variables.
- Finalmente, definimos la línea de comando: **imprimir_reporte_transacciones()**, dónde almaceneramos las variables de la función **reporte1_transacciones(nombre_archivo)**
  - Al terminar este detalle, ejecutaremos en la terminal: 
  > **python Transacciones.py imprimir-reporte-transacciones** <br>
    Con ello, podremos ver el reporte que requerimos para el proyecto.

![Reporte Final](Reporte%20Final.png)

## 4. CONCLUSIÓN
Podemos concluir que el uso de CLI puede facilitar el acceso a instrucciones en altos volumenes de datos sin tanta necesidad de un diseño GUI.
Así mismo, el conjunto de instrucciones puede disgregarse en mayor medida para optimizar el consumo computacional que tiene las líneas de comando en sí.
Si están iniciando en programación, les recomiendo iniciar a explorar estos conceptos porque podrían acelerar ciertas actividades en los reportes o actividades diarios en su trabajo o en su día a día.