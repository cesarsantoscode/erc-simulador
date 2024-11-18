#Hola Reportes DataFrame

from ctypes import POINTER
import numpy as np #no se ha usado todavia
import pandas as pd
import seaborn as sns #no se ha usado todavia
import matplotlib.pyplot as plt #no se ha usado todavia
from datetime import datetime, timedelta
import os


#Cargar los datos desde archivo csv

#Primer DataFrame archivo_prestamos
data = {
    "codigo": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
    "dni": [12345678, 12345679, 40658571, 39620177, 47142638, 24392730, 38538059, 20946837, 43214578, 36456745,
            10234578, 45234589, 43568923, 10347348, 75741349, 10751690, 65713897, 72456485, 96454224, 18564527,
            47142638, 10234578, 39620177],
    "nombre": ["Juan Carlos", "Rosa Esther", "Fernanda Marisol", "Daniela Isabel", "Jesus Mateo", "Ezequiel Marcelo", 
               "Samir Alonso", "Almendra Mercedes", "Luis Carlos", "Ana Carolina", "Carlos Alberto", "Epifania", 
               "María Elena", "Elvis Roman", "Mercedes Maria", "Byron David", "Gonzalo Luis", "Fernanda Noemi", 
               "Jaime Eduardo", "Marlene Estefania", "Jesus Mateo", "Carlos Alberto", "Daniela Isabel"],
    "apellido": ["Perez Sandoval", "Diaz Lopez", "Chaves Paredes", "Torres Alvarez", "Portal Valdivia", "Mendez Cardenas", 
                 "Contreras Montalvan", "Araujo Cardozo", "García Perez", "Rojas Sanchez", "Sanchez Perez", "Ruiz Macedo", 
                 "Herrera Galindo", "Novillo Jara", "López González", "Cevallos Trujillo", "Balcazar Campoverde", 
                 "Campos Mendiata", "Cárdenas Molina", "Perez Cabrera", "Portal Valdivia", "Sanchez Perez", "Torres Alvarez"],
    "fecha_nacim": ["1/01/1990", "6/09/1992", "27/04/2000", "6/02/1992", "16/02/1968", "12/05/1970", "23/06/1994", 
                    "21/09/1979", "30/09/2000", "3/03/1988", "20/04/1994", "1/10/2003", "25/08/1988", "1/09/1995", 
                    "15/07/2000", "8/07/2002", "2/07/1988", "3/02/1976", "11/11/1960", "14/10/1959", "16/02/1968", 
                    "20/04/1994", "6/02/1992"],
    "edad": [34, 32, 24, 32, 56, 54, 30, 45, 24, 36, 30, 21, 36, 29, 24, 22, 36, 48, 64, 65, 56, 30, 32],
    "sexo": ["M", "F", "F", "F", "M", "M", "M", "F", "M", "F", "M", "F", "F", "M", "F", "M", "M", "F", "M", "F", "M", "M", "F"],
    "cod_prod": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
    "nom_prod": ["Personal", "Personal", "Hipotecario", "Personal", "Vehicular", "Hipotecario", "Personal", "Vehicular", 
                 "Personal", "Vehicular", "Hipotecario", "Personal", "Vehicular", "Vehicular", "Hipotecario", "Personal", 
                 "Vehicular", "Hipotecario", "Vehicular", "Personal", "Hipotecario", "Personal", "Vehicular"],
    "moneda": ["soles", "soles", "dolares", "dolares", "soles", "soles", "dolares", "soles", "soles", "dolares", 
               "soles", "soles", "soles", "dolares", "dolares", "soles", "soles", "dolares", "dolares", "soles", 
               "soles", "soles", "dolares"],
    "monto": [10000, 20000, 5080, 9000, 40000, 35820, 399400, 30000, 8000, 20000, 100000, 15000, 25000, 75000, 5000, 
              8400, 10000, 65000, 150000, 48000, 3050, 1950, 2050],
    "num_cuotas": [12, 16, 24, 32, 56, 54, 80, 45, 24, 36, 120, 18, 36, 180, 24, 12, 36, 48, 72, 65, 32, 12, 12],
    "tea": [0.2, 0.2, 0.097, 0.153, 0.205, 0.138, 0.164, 0.105, 0.155, 0.182, 0.103, 0.125, 0.148, 0.087, 0.082, 0.063, 
            0.044, 0.025, 0.076, 0.113, 0.132, 0.151, 0.179],
    "fecha_desem": ["1/12/2023", "1/12/2023", "16/02/2024", "27/09/2024", "29/04/2024", "4/11/2024", "23/08/2024", 
                    "9/03/2024", "10/11/2024", "20/10/2024", "15/08/2024", "5/09/2024", "25/07/2024", "25/07/2024", 
                    "18/06/2024", "23/10/2024", "18/02/2024", "8/03/2024", "13/06/2024", "31/08/2024", "12/09/2024", 
                    "13/10/2024", "4/10/2024"],
    "tipo_cuota": [1, 2, 1, 2, 1, 1, 2, 2, 1, 2, 1, 2, 2, 1, 1, 2, 2, 1, 2, 1, 2, 2, 1],
    "tasa_desgrav": [1.14, 1.14, 3, 2.7, 1.32, 1.24, 2.5, 2.27, 2, 1.5, 2.5, 1.7, 1.6, 3, 3.4, 1.05, 2.7, 2.35, 1.6, 
                     1.65, 2.3, 1.95, 2.6],
    "tasa_derecho": [2.5, 2.5, 2, 2.73, 2.43, 2.56, 3, 2.75, 2.3, 2, 2.8, 2.2, 2.1, 2.9, 2.13, 2.45, 2.8, 2.15, 2.5, 
                     2.85, 2.2, 2.55, 2.9],
    "dia_fijo": [28, 28, 24, 18, 20, 28, 13, 18, 4, 19, 21, 14, 20, 14, 10, 8, 20, 12, 10, 27, 28, 14, 2]
}

df = pd.DataFrame(data)
df.to_csv('archivo_prestamos.csv',sep=';' ,index=False)

#Segundo Dataframe archivo_productos
data = {
    "cod_prod": [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
    "nom_prod": [
        "Personal", "Personal", "Hipotecario", "Personal", "Vehicular",
        "Hipotecario", "Personal", "Vehicular", "Personal", "Vehicular",
        "Hipotecario", "Personal", "Vehicular", "Vehicular", "Hipotecario",
        "Personal", "Vehicular", "Hipotecario", "Vehicular", "Personal",
        "Hipotecario", "Personal", "Vehicular"
    ]
}
df = pd.DataFrame(data)
df.to_csv('archivo_productos.csv',sep=';', index=False)

# Tercer Dataframe archivo_clientes
data = {
    "dni": [
        12345678, 12345679, 40658571, 39620177, 47142638, 24392730, 38538059, 
        20946837, 43214578, 36456745, 10234578, 45234589, 43568923, 10347348, 
        75741349, 10751690, 65713897, 72456485, 96454224, 18564527],
    "nombre": [
        "Juan Carlos", "Rosa Esther", "Fernanda Marisol", "Daniela Isabel", 
        "Jesus Mateo", "Ezequiel Marcelo", "Samir Alonso", "Almendra Mercedes",
        "Luis Carlos", "Ana Carolina", "Carlos Alberto", "Epifania", 
        "María Elena", "Elvis Roman", "Mercedes Maria", "Byron David", 
        "Gonzalo Luis", "Fernanda Noemi", "Jaime Eduardo", "Marlene Estefania"],
    "apellido": [
        "Perez Sandoval", "Diaz Lopez", "Chaves Paredes", "Torres Alvarez",
        "Portal Valdivia", "Mendez Cardenas", "Contreras Montalvan", 
        "Araujo Cardozo", "García Perez", "Rojas Sanchez", "Sanchez Perez", 
        "Ruiz Macedo", "Herrera Galindo", "Novillo Jara", "López González", 
        "Cevallos Trujillo", "Balcazar Campoverde", "Campos Mendiata", 
        "Cárdenas Molina", "Perez Cabrera"],
    "fecha_nacim": [
        "1/01/1990", "6/09/1992", "27/04/2000", "6/02/1992", "16/02/1968", 
        "12/05/1970", "23/06/1994", "21/09/1979", "30/09/2000", "3/03/1988", 
        "20/04/1994", "1/10/2003", "25/08/1988", "1/09/1995", "15/07/2000", 
        "8/07/2002", "2/07/1988", "3/02/1976", "11/11/1960", "14/10/1959"],
    "sexo": [
        "M", "F", "F", "F", "M", "M", "M", "F", "M", "F", "M", "F", "F", 
        "M", "F", "M", "M", "F", "M", "F"]
}

df = pd.DataFrame(data)
df.to_csv('archivo_clientes.csv',sep=';', index=False)


prestamos=pd.read_csv('archivo_prestamos.csv',sep=';')
productos=pd.read_csv('archivo_productos.csv',sep=';')
clientes=pd.read_csv('archivo_clientes.csv',sep=';')
#Nuestro logo de proyecto ERC  TuBanca - “Financia tus sueños”
def logo():
        frase='"Financia tus sueños..."'
        print(r"__________________________________________________________________________________________________")
        print(r"                              ____________     ___  ___  ___                                     ")
        print(r"                             | 0000000000 |   |__  |__/ |                                        ")
        print(r"                             | 00      00 |   |___ |  \ |___                                     ")
        print(r"                             | 0000  0000 |                                                       ")
        print(r"                             | 0000000000 |   PROJECT MANAGEMENT SOLUTIONS                        ")
        print(r"                             |____________|                                                       ")
        print(f"                                 {frase}                                       ")
        print(r"\nPresentado por: Estefany Amaya - Rosa Diaz - Rosmery Villar                                      ")
        print(r"__________________________________________________________________________________________________")

def leer_datos():
    try:
        df=pd.read_csv('archivo_prestamose.csv')
        return df
    except FileNotFoundError:
        print('No se encontró el archivo, se procederá a crear uno nuevo')
        return pd.DataFrame()

#Funcion para reporte de prestamos por rango de edad y sexo
def generar_reporte(df,sexo=None,rango_edad=None):
    if sexo:
        df=df[df['Sexo']==sexo]
    if rango_edad:
        df=df[(df['Edad']>=rango_edad[0])&(df['Edad']<=rango_edad[1])]
    return df

class Cliente:
    def __init__(self, dni, nombre, apellido, fecha_nacimiento, sexo):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_nacimiento = fecha_nacimiento
        self.__sexo = sexo
    
    @property
    def dni(self):
        return self.__dni
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento
    
    @property
    def sexo(self):
        return self.__sexo
    
    @dni.setter
    def dni(self, dni):
        self.__dni = dni
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido
    
    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento
    
    @sexo.setter
    def sexo(self, sexo):
        self.__sexo = sexo

    def Edad(self):
        Edad = datetime.now().year - datetime.strptime(self.__fecha_nacimiento, '%d/%m/%Y').year
        return Edad
    
    def __str__(self):
        return f'{self.__dni} {self.__nombre} {self.__apellido} {self.__fecha_nacimiento} {self.Edad()} {self.__sexo}'

class Producto:
    def __init__(self, codigo_producto, nombre_producto):
        self.__codigo_producto = codigo_producto
        self.__nombre_producto = nombre_producto
    
    @property
    def codigo_producto(self):
        return self.__codigo_producto
    
    @property
    def nombre_producto(self):
        return self.__nombre_producto
    
    @codigo_producto.setter
    def codigo_producto(self, codigo_producto):
        self.__codigo_producto = codigo_producto
    
    @nombre_producto.setter
    def nombre_producto(self, nombre_producto):
        self.__nombre_producto = nombre_producto
    @staticmethod
    def generar_codigo_unico_producto(productos_df):
        if productos_df.empty:
            return 1
        else:
            return productos_df['cod_prod'].max()+1
    def __str__(self):
        return f'{self.__codigo_producto} {self.__nombre_producto}'

class Prestamo:
    def __init__(self, codigo_prestamo, cliente, producto, moneda, monto, num_cuotas, tea, fecha_desembolso, tipo_cuota, tasa_desgravamen, tasa_derecho, dia_fijo):
        self.__codigo_prestamo = codigo_prestamo
        self.__cliente = cliente
        self.__producto = producto
        self.__moneda = moneda
        self.__monto = monto
        self.__num_cuotas = num_cuotas
        self.__tea = tea
        self.__fecha_desembolso=datetime.strptime(fecha_desembolso, '%d/%m/%Y')
        self.__tipo_cuota = tipo_cuota
        self.__tasa_desgravamen = tasa_desgravamen
        self.__tasa_derecho = tasa_derecho
        self.__dia_fijo = dia_fijo

    @property
    def codigo_prestamo(self):
        return self.__codigo_prestamo
    
    @property
    def cliente(self):
        return self.__cliente
    
    @property
    def producto(self):
        return self.__producto
    
    @property
    def moneda(self):
        return self.__moneda
    
    @property
    def monto(self):
        return self.__monto
    
    @property
    def num_cuotas(self):
        return self.__num_cuotas
    
    @property
    def tea(self):
        return self.__tea
    
    @property
    def fecha_desembolso(self):
        return self.__fecha_desembolso
    
    @property
    def tipo_cuota(self):
        return self.__tipo_cuota
    
    @property
    def tasa_desgravamen(self):
        return self.__tasa_desgravamen
    
    @property
    def tasa_derecho(self):
        return self.__tasa_derecho
    @property
    def dia_fijo(self):
        return self.__dia_fijo

    @codigo_prestamo.setter
    def codigo_prestamo(self, codigo_prestamo):
        self.__codigo_prestamo = codigo_prestamo
    
    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente
    
    @producto.setter
    def producto(self, producto):
        self.__producto = producto
    
    @moneda.setter
    def moneda(self, moneda):
        self.__moneda = moneda
    
    @monto.setter
    def monto(self, monto):
        self.__monto = monto
    
    @num_cuotas.setter
    def num_cuotas(self, num_cuotas):
        self.__num_cuotas = num_cuotas
    
    @tea.setter
    def tea(self, tea):
        self.__tea = tea
    
    @fecha_desembolso.setter
    def fecha_desembolso(self, fecha_desembolso):
        if isinstance(fecha_desembolso, str):
            self.__fecha_desembolso = datetime.strptime(fecha_desembolso, '%d/%m/%Y')
        elif isinstance(fecha_desembolso, datetime):
            self.__fecha_desembolso = fecha_desembolso
        else:
            raise ValueError("El formato de fecha_desembolso no es válido")
    
    @tipo_cuota.setter
    def tipo_cuota(self, tipo_cuota):
        self.__tipo_cuota = tipo_cuota
    
    @tasa_desgravamen.setter
    def tasa_desgravamen(self, tasa_desgravamen):
        self.__tasa_desgravamen = tasa_desgravamen
    
    @tasa_derecho.setter
    def tasa_derecho(self, tasa_derecho):
        self.__tasa_derecho = tasa_derecho
    def tea_mensual(self):
      # Calcular la tasa de interés mensual
      tea_mensual = (((1 + (self.__tea / 100)) ** (1 / 12)) - 1)
      return float(tea_mensual)
    @dia_fijo.setter
    def dia_fijo(self, dia_fijo):
        self.__dia_fijo = dia_fijo

    def Cuota(self):
      """
      Calcular la cuota fija dependiendo del tipo de cuota.
      Tipo de cuota 1 -> Cuota con día fijo
      Tipo de cuota 2 -> Cuota con período fijo de 30 días
      """
      
      if self.__tipo_cuota == 1:
          # Tipo de cuota 1 (día fijo): se calcula con la fórmula de cuota fija tradicional
          cuota_fija = self.__monto * (self.tea_mensual() * (1 + self.tea_mensual()) ** self.__num_cuotas) / ((1 + self.tea_mensual()) ** self.__num_cuotas - 1)
      elif self.__tipo_cuota == 2:
          # Tipo de cuota 2 (periodo fijo de 30 días): calculamos cuota fija estándar sin ajuste de fechas
          cuota_fija = self.__monto * (self.tea_mensual() * (1 + self.tea_mensual()) ** self.__num_cuotas) / ((1 + self.tea_mensual()) ** self.__num_cuotas - 1)
      
      return cuota_fija

    def generar_cronograma(self):
      saldo_pendiente = self.__monto
      fecha_vencimiento = self.__fecha_desembolso
      cronograma = []
      for cuota_num in range(1, self.__num_cuotas + 1):
          # Calcular intereses y amortización
          cuota_fija = self.Cuota()
          interes = saldo_pendiente * self.tea_mensual()
          amortizacion = cuota_fija - interes
          saldo_pendiente -= amortizacion

          # Asignar valores fijos de Desgravamen y Emisión
          desgravamen = self.__tasa_desgravamen  # Valor fijo para desgravamen
          derecho_emision = self.__tasa_derecho  # Valor fijo para emisión
          total_pagar = cuota_fija + desgravamen + derecho_emision

          # Calcular la fecha de vencimiento dependiendo del tipo de cuota
          if self.__tipo_cuota == 1:  # Día fijo de vencimiento
              # Para cuotas con día fijo, el vencimiento se mantiene en el mismo día cada mes
              if fecha_vencimiento.day != self.__dia_fijo:
                  fecha_vencimiento = fecha_vencimiento.replace(day=self.__dia_fijo)
              # Avanzamos al siguiente mes, manteniendo el día fijo
              if fecha_vencimiento.month==12:
                  fecha_vencimiento=fecha_vencimiento.replace(year=fecha_vencimiento.year + 1, month=1)
              else:
                  fecha_vencimiento = fecha_vencimiento.replace(month=fecha_vencimiento.month + 1)
          elif self.__tipo_cuota == 2:  # Periodo fijo de 30 días
              # Para cuotas con periodo fijo de 30 días, sumamos 30 días cada vez
              fecha_vencimiento = self.__fecha_desembolso + timedelta(days=30 * cuota_num)

          # Agregar información del cronograma
          cronograma.append({
              "Nro Cuota": cuota_num,
              "Fecha Desembolso": self.__fecha_desembolso.strftime('%d/%m/%Y'),
              "Fecha de Vcto. Cuota": fecha_vencimiento.strftime('%d/%m/%Y'),
              "Capital": round(saldo_pendiente+amortizacion, 2),  # El capital restante
              "Amortizacion": round(amortizacion, 2),
              "Interes": round(interes, 2),
              "Cuota": round(cuota_fija, 2),
              "Desgravamen": round(desgravamen, 2),
              "Emision": round(derecho_emision, 2),
              "Total a Pagar": round(total_pagar, 2)
          })
      return pd.DataFrame(cronograma)
      #return pd.DataFrame(cronograma)
    def mostrar_cronograma(cronograma_df):
      print(f"{'Nro Cuota':<10}{'Fecha Desembolso':<20}{'Fecha de Vcto. Cuota':<20}{'Capital':<10}{'Amortizacion':<12}{'Interes':<8}{'Cuota':<8}{'Desgravamen':<12}{'Emision':<8}{'Total a Pagar':<12}")
      for _, row in cronograma_df.iterrows():
        print(f"{row['Nro Cuota']:<10}{row['Fecha Desembolso']:<20}{row['Fecha de Vcto. Cuota']:<20}{row['Capital']:<10}{row['Amortizacion']:<12}{round(row['Interes']*100,2):<8}{row['Cuota']:<8}{row['Desgravamen']:<12}{row['Emision']:<8}{row['Total a Pagar']:<12}")
    @staticmethod
    def generar_codigo_unico(prestamos_df):
        if prestamos_df.empty:
            return 1
        else:
            return prestamos_df['codigo'].max()+1

def simulador():
  logo()
  os.system("pause")
  #Copias locales
  prestamos_df=prestamos.copy()
  productos_df=productos.copy()
  clientes_df=clientes.copy()
  print('Bienvenido al simulador de préstamos')
  print('--------------------------------------')
  
  while True:
    print('\n          SIMULADOR DE PRÉSTAMOS            ')
    print('1. Ver datos actuales')
    print('2. Agregar nuevo cliente')
    print('3. Agregar nuevo préstamo')
    print('4. Generar cronograma')
    print('5. Generar gráficos')
    print('6. Exportar a archivo csv')
    print('7. Salir')
    opcion = input('Ingrese una opción: ')
    while opcion not in ['1', '2','3','4','5','6','7']:   
      opcion = input('Ingrese una opción válida: ')
    if opcion=='1':
       print('\nDatos actuales')
       print('---------------------------')
       print('\nClientes: ')
       print(clientes_df)
       print('\nPréstamos:')
       print(prestamos_df)
       print('\nProductos:')
       print(productos_df)
    elif opcion=='2':
      print("\n     Agregar nuevo cliente     ")
      dni = input('DNI del cliente: ')
      while len(dni) != 8 or not dni.isdigit():
        dni = input('Ingrese un DNI válido: ')
      if dni in clientes_df['dni'].values:
          print(f'El cliente con dni {dni} ya existe en la base de datos')
          os.system('pause')
          continue
      else:
        nombre = input('Nombre del cliente: ').capitalize()
        apellido = input('Apellido del cliente: ').capitalize()
        while True:
            fecha_nacimiento = input('Fecha de nacimiento del cliente (dd/mm/aaaa): ')
            try:
                datetime.strptime(fecha_nacimiento, '%d/%m/%Y')
                break
            except ValueError:
                print(f'{fecha_nacimiento} no es válida.')
                print('Ingrese una fecha de nacimiento válida')        
        sexo = input('Sexo del cliente (M/F): ').upper().strip()
        while sexo not in ['M', 'F']:
            sexo = input('Ingrese un sexo válido (M/F): ').upper().strip()
        cliente_obj=Cliente(dni=dni,nombre=nombre,apellido=apellido,fecha_nacimiento=fecha_nacimiento,sexo=sexo)
        edad_cliente=cliente_obj.Edad()
        if edad_cliente<18:
            print(f'El cliente {nombre} {apellido} no es mayor de edad (edad: {edad_cliente}. No se puede continuar con la simulación.)')
            continue
        elif edad_cliente>70:
            print(f'El cliente {nombre} {apellido} tiene más de 70 años (edad: {edad_cliente}. No se puede continuar con la simulación.)')
            continue
        
        nuevo_cliente={
            'dni':dni,
            'nombre':nombre,
            'apellido':apellido,
            'fecha_nacim':fecha_nacimiento,
            'sexo':sexo
            }
        clientes_df=pd.concat([clientes_df,pd.DataFrame([nuevo_cliente])],ignore_index=True)
        print('Cliente agregado con éxito.')
      
    elif opcion=='3':
      print('\tAgregar prestamo')
      dni_cliente = input('Ingrese DNI del Cliente: ')         
      while len(dni_cliente)!=8 or not dni_cliente.isdigit():     
         dni_cliente=input('Ingrese DNI del Cliente: ')
      cliente=clientes_df[clientes_df['dni'].astype(str)==dni_cliente]#se corrigio

      if not cliente.empty:
        cliente_obj=Cliente(
            dni=cliente.iloc[0]['dni'],
            nombre=cliente.iloc[0]['nombre'],
            apellido=cliente.iloc[0]['apellido'],
            fecha_nacimiento=cliente.iloc[0]['fecha_nacim'],
            sexo=cliente.iloc[0]['sexo']
        )      
        edad_cliente=cliente_obj.Edad()
        print(f'Cliente encontrado: {cliente_obj.nombre} {cliente_obj.apellido}')

        #Verificar que tiene la edad para que se le otorge el credito 
        # (puede que desde la fecha se registro ya no cumpla con la condicion de la edad)
        if edad_cliente<18 or edad_cliente>70:
            print(f'El cliente {cliente_obj.nombre} {cliente_obj.apellido} no puede acceder a crédito debido a su edad ({edad_cliente})')
            continue
        #Generar código único
        nuevo_codigo_prestamo=Prestamo.generar_codigo_unico(prestamos_df)
        #Pedimos los demas datos de prestamo
        producto_registrar=int(input('Nombre producto (1-Personal/2-Vehicular/3-Hipotecario): '))
        while producto_registrar not in [1,2,3]:
            producto_registrar=int(input('Nombre producto (1-Personal/2-Vehicular/3-Hipotecario): '))
        if producto_registrar==1:
            producto_registrar='Personal'
        elif producto_registrar==2:
            producto_registrar='Vehicular'
        else:
            producto_registrar='Hipotecario'
        nuevo_codigo_producto=Producto.generar_codigo_unico_producto(productos_df)
        producto=Producto(codigo_producto=nuevo_codigo_producto,nombre_producto=producto_registrar )

        productos_df=pd.concat([productos_df,pd.DataFrame([{
            'cod_prod':producto.codigo_producto,
            'nom_prod':producto.nombre_producto,
        }],columns=productos_df.columns)],ignore_index=True)

        moneda=input('Moneda del préstamo (soles/dolares): ').lower()
        while moneda not in ['soles', 'dolares']:
            moneda=input('Ingrese una moneda válida (soles/dolares): ').lower()
        while True:
            try:
                monto=float(input('Monto del préstamo: '))
                if monto<=0:
                    continue
                else:
                    break 
            except ValueError:
                print('Ingrese un monto válido')
        while True:
            try:
                num_cuotas=int(input('Número de cuotas: '))
                if num_cuotas<=0:
                    continue
                else:
                    break 
            except ValueError:
                print('Ingrese un número de cuotas válido')
        while True:
            try:
                tea=float(input('TEA (Ejm: 20%=0.2): '))
                if tea<=0:
                    continue
                else:
                    break 
            except ValueError:
                print('Ingrese una tasa de interés válida')
        while True:
            fecha_desembolso = input('Fecha de desembolso del préstamo (dd/mm/aaaa): ')
            try:
                fecha_desembolso = datetime.strptime(fecha_desembolso, '%d/%m/%Y').date()
                fecha_hoy=datetime.now().date()
                if fecha_desembolso>=fecha_hoy:
                    break
                else:
                    print(f'La fecha de desembolso debe ser hoy {fecha_hoy.strftime('%d/%m/%Y')} o posterior')
            except ValueError:
                print(f'{fecha_desembolso} no es válida.')
                print('Ingrese una fecha de desembolso válida')
        while True:
            try:
                tipo_cuota=int(input('Tipo de cuota (1.Día fijo/2.Periodo fijo de 30 días): '))
                if tipo_cuota not in [1,2]:
                    continue
                else:
                    break 
            except ValueError:
                print('Ingrese un tipo de cuota válido')
        while True:
            try:
                tasa_desgravamen=float(input('Tasa de desgravamen (Entre 1.0 y 3.0): '))
                if tasa_desgravamen<1 or tasa_desgravamen>3:
                    continue
                else:
                    break
            except ValueError:
                print('Ingrese una valor válido')
        while True:
            try:
                tasa_derecho=float(input('Tasa de derecho de emisión (Entre 2.0 y 3.0): '))
                if tasa_derecho<2 or tasa_derecho>3:
                    continue
                else:
                    break
            except ValueError:
                print('Ingrese una tasa de derecho de emisión válida')
        if tipo_cuota==1:
            while True:
                try:
                    dia_fijo=int(input('Ingrese el día fijo de vencimiento (no mas de 28): '))
                    if dia_fijo not in range(1,29):
                        continue
                    else:
                        break
                except ValueError:
                    print('Ingrese un día fijo válido')
        else:
            dia_fijo=0
        
        prestamo=Prestamo(
            codigo_prestamo=nuevo_codigo_prestamo,
            cliente=cliente_obj,
            producto=producto,
            moneda=moneda,
            monto=monto,
            num_cuotas=num_cuotas,
            tea=tea,
            fecha_desembolso=fecha_desembolso.strftime('%d/%m/%Y'),
            tipo_cuota=tipo_cuota,
            tasa_desgravamen=tasa_desgravamen,
            tasa_derecho=tasa_derecho,
            dia_fijo=dia_fijo
        )
        prestamos_df=pd.concat([prestamos_df,pd.DataFrame([{
            'codigo':prestamo.codigo_prestamo,
            'dni':cliente_obj.dni,
            'nombre':cliente_obj.nombre,
            'apellido':cliente_obj.apellido,
            'fecha_nacim':cliente_obj.fecha_nacimiento,
            'edad':cliente_obj.Edad(),
            'sexo':cliente_obj.sexo,
            'cod_prod':producto.codigo_producto,
            'nom_prod':producto.nombre_producto,
            'moneda':prestamo.moneda,
            'monto':prestamo.monto,
            'num_cuotas':prestamo.num_cuotas,
            'tea':prestamo.tea,
            'fecha_desem':prestamo.fecha_desembolso.strftime('%d/%m/%Y'),
            'tipo_cuota':prestamo.tipo_cuota,
            'tasa_desgrav':prestamo.tasa_desgravamen,
            'tasa_derecho':prestamo.tasa_derecho,
            'dia_fijo':prestamo.dia_fijo
        }],columns=prestamos_df.columns)],ignore_index=True)
        print(f'Préstamos con código {nuevo_codigo_prestamo} agregado exitosamente.')
    elif opcion=='4':
        print('\tGenerando cronograma')
        dni_cliente=input('DNI de cliente, para ver con que prestamos cuenta: ')
        while len(dni_cliente)!=8 or not dni_cliente.isdigit():
            dni_cliente=input('Ingrese DNI válido (8 dígitos): ')
        prestamos_cliente=prestamos_df[prestamos_df['dni'].astype(str)==dni_cliente]
        if prestamos_cliente.empty:
            print(f'No se encontraron prestamos asociados al DNI {dni_cliente}')
            continue
        print(f'\nPréstamos asociados a DNI {dni_cliente}: ')
        print(prestamos_cliente[['codigo', 'nom_prod', 'monto', 'num_cuotas', 'fecha_desem']])
        codigo_prestamo=input('\nIngrese el Código de préstamo a generar cronograma: ')
        while codigo_prestamo not in prestamos_cliente['codigo'].astype(str).values:
            codigo_prestamo=input('Ingrese un código válido: ')
        #Obtenemos info del prestamo seleccionado  
        prestamo_seleccionado=prestamos_df[prestamos_df['codigo']==int(codigo_prestamo)].iloc[0] 
        cliente_objetivo=Cliente(
            dni=prestamo_seleccionado['dni'],
            nombre=prestamo_seleccionado['nombre'],
            apellido=prestamo_seleccionado['apellido'],
            fecha_nacimiento=prestamo_seleccionado['fecha_nacim'],
            sexo=prestamo_seleccionado['sexo']
        )
        producto_objetivo=Producto(
            codigo_producto=prestamo_seleccionado['cod_prod'],
            nombre_producto=prestamo_seleccionado['nom_prod']
        )
        prestamo_objetivo = Prestamo(
            codigo_prestamo=prestamo_seleccionado['codigo'],
            cliente=cliente_objetivo,
            producto=producto_objetivo,
            moneda=prestamo_seleccionado['moneda'],
            monto=prestamo_seleccionado['monto'],
            num_cuotas=prestamo_seleccionado['num_cuotas'],
            tea=prestamo_seleccionado['tea'],
            fecha_desembolso=prestamo_seleccionado['fecha_desem'],
            tipo_cuota=prestamo_seleccionado['tipo_cuota'],
            tasa_desgravamen=prestamo_seleccionado['tasa_desgrav'],
            tasa_derecho=prestamo_seleccionado['tasa_derecho'],
            dia_fijo=prestamo_seleccionado['dia_fijo']
        )
        #Generamos el cronograma
        cronograma_df=prestamo_objetivo.generar_cronograma()

        #Mostramos el cronograma
        print(f'\n\tCronograma de pago para el préstamo con codigo {prestamo_objetivo.codigo_prestamo}:')
        Prestamo.mostrar_cronograma(cronograma_df)

    elif opcion=='5':
        while True:
            os.system('cls')
            print('Reporte de clientes')
            print('1. Reporte de prestamos por sexo y rango de edad. ')
            print('2. Reporte de prestamos por tipo de crédito. ')
            print('3. Reporte de prestamos por moneda. ')
            print('4. Prestamos por Edad y tipo de prestamo.')
            print('5. Salir')

            
            opcion=input('Ingrese una opción: ')

            while opcion not in ['1','2','3','4','5']:
                opcion=input('Ingrese una opción: ')
            if opcion=='1':
                os.system('cls')
                print('Reporte de prestamos por sexo y rango de edad')
                # Gráfico de barras para edad
                edad_counts = prestamos_df['edad'].value_counts().reset_index()
                edad_counts.columns = ['edad', 'conteo']
                
                plt.figure(figsize=(10, 7))
                ax = sns.barplot(x='edad', y='conteo', data=edad_counts, palette='coolwarm')

                ax.bar_label(ax.containers[0], fmt='%.0f', label_type='edge', padding=5,fontsize=10,color='black' )
                for p in ax.patches:
                    ax.annotate(
                        f'{p.get_height():.0f}',
                        (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='center', 
                        xytext=(0, 9), textcoords='offset points',
                        fontsize=12,color='black')
                    
                plt.title("Distribución por Rango de Edad",fontsize=16)
                plt.xlabel("Rango de Edad",fontsize=12)
                plt.ylabel("Número de Registros", fontsize=12)
                plt.xticks(rotation=45) #rotamos etiquetas
                plt.tight_layout() #Para que no se corte ningun texto
                plt.show()

                # Gráfico de barras para sexo
                sexo_counts = prestamos_df['sexo'].value_counts().reset_index()
                sexo_counts.columns = ['sexo', 'conteo']

                plt.figure(figsize=(8, 6))
                ax = sns.barplot(x='sexo', y='conteo', data=sexo_counts, palette='Set2')
                for p in ax.patches:
                    ax.annotate(
                        f'{p.get_height():.0f}',
                        (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='center', 
                        xytext=(0, 8), textcoords='offset points',
                        fontsize=12,color='black')

                # Añadir etiquetas directamente a las barras
                ax.bar_label(ax.containers[0], fmt='%.0f', label_type='edge', padding=5, fontsize=10,color='black')

                plt.title("Distribución por Sexo",fontsize=16)
                plt.xlabel("Sexo",fontsize=12)
                plt.ylabel("Número de Registros",fontsize=12)
                plt.tight_layout()
                plt.show()
                os.system("pause")
            elif opcion=='2':
                os.system('cls')
                print('Reporte de prestamos por tipo de crédito')
                reporte_credito= prestamos_df['nom_prod'].value_counts().reset_index()
                reporte_credito.columns = ['Tipo de Crédito', 'Cantidad de Préstamos']
                
                sns.set(style="whitegrid",palette="muted")

                colores=sns.color_palette("coolwarm",len(reporte_credito))

                plt.figure(figsize=(10,6))
                bars=plt.bar(reporte_credito['Tipo de Crédito'],reporte_credito['Cantidad de Préstamos'],color=colores)
                for bar in bars:
                    height=bar.get_height()
                    plt.text(bar.get_x()+bar.get_width()/2.,height+1,f'{height}',
                            ha='center',va='bottom',fontsize=11,color='black')
                    
                plt.title('Prestamos por tipo de Crédito',fontsize=16,fontweight='bold',color='darkblue')
        
                plt.xlabel('Tipo de crédito', fontsize=12,fontweight='bold')
        
                plt.ylabel('Cantidad de Préstamos',fontsize=12,fontweight='bold')
                plt.xticks(rotation=45,ha='right',fontsize=10)
                plt.tight_layout()
                plt.show()
                
            elif opcion=='3':
                os.system('cls')
                print('Reporte de prestamos por moneda')
                prestamos_por_moneda=prestamos_df.groupby('moneda')['monto'].sum().reset_index()
                print(prestamos_por_moneda)

                plt.figure(figsize=(8,6))
                plt.bar(prestamos_por_moneda['moneda'],prestamos_por_moneda['monto'],color='skyblue')
                plt.xlabel('Moneda')
                plt.ylabel('Monto Total de Prestamos')
                plt.title('Total de Préstamos por Moneda')
                plt.xticks(rotation=45) 
                plt.tight_layout()   
                plt.show() 
                os.system("pause")   
            elif opcion=='4':
                plt.figure(figsize=(10,6))
                sns.scatterplot(x='edad', y='monto', data=prestamos_df, hue='sexo', palette='coolwarm')
                plt.title('Relación entre Edad y Monto Solicitado', fontsize=16)
                plt.xlabel('Edad', fontsize=12)
                plt.ylabel('Monto Solicitado', fontsize=12)
                plt.tight_layout()
                plt.show()
            else:
                break

    elif opcion=='6':
        try:
            prestamos_df.to_csv('prestamos_nuevo.csv', sep=';', index=False)
            clientes_df.to_csv('clientes.csv', sep=';', index=False)
            productos_df.to_csv('productos.csv', sep=';', index=False)
            print("Archivos CSV creados exitosamente:")
            print("- 'prestamos.csv'")
            print("- 'productos.csv'")
            print("- 'clientes.csv'")

        except Exception as e:
            print(f"Error al guardar los archivos: {e}")
    else:
        break

simulador()

