departamentos=[["A10","B10","C10","D10"],
               ["A9","B9","C9","D9"],
               ["A8","B8","C8","D8"],
               ["A7","B7","C7","D7"],
               ["A6","B6","C6","D6"],
               ["A5","B5","C5","D5"],
               ["A4","B4","C4","D4"],
               ["A3","B3","C3","D3"],
               ["A2","B2","C2","D2"],
               ["A1","B1","C1","D1",]]

d=0
rut_comprador=[]
def menu():
  print('''Bienvenido a Casa Feliz
  
  Seleccione una opción:
  1. Comprar departamento
  2. Mostrar departamentos disponibles
  3. Ver listado de compradores
  4. Mostrar ganancias totales
  5. Salir''')


def edificio ():
  e=0
  print("DEPARTAMENTOS DISPONIBLES\n")
  for piso in range (len(departamentos)):
    for dpto in range (len(departamentos[piso])):
      print(" ",departamentos[piso][dpto], end=" ")
    print("\n")

def comprar_depto():

  print("Ingrese el número y letra del departamento a comprar")
  depto=(input()) .upper
  edificio()
  print("Ingrese el rut del comprador")
  rut_cliente()
  edificio()

  while depto==edificio:
    print("ERROR!! Ingrese el número y letra correctamente")
    depto=(input()) .upper
    rut_cliente()
  
  edificio()
  menu()
  

def seleccionar_depto(depto):
  for i in range (len(departamentos)):
    if departamentos[i]==depto:
      departamentos[i]="X"

def rut_cliente():
  rut=int(input())
  rut_comprador.append(rut)

def ganancias_totales(depto):
  a=3800
  b=3000
  c=2800
  d=3500
  
  total=total+a+b+c+d
  print(f"Las ganancias totales son {total} UF ")
  


menu()

op=int(input())

if op==1:
  comprar_depto()

if op==2:
  edificio()


menu()


if op==3:
    print(rut_comprador)
    
menu()

if op==4:

  ganancias_totales()

menu()

if op==5:
  while d==0:
    print("chau")
    break

