from lifestore_file import (lifestore_products ,
lifestore_searches, lifestore_sales)

#/\/\/\/\/\/\Variables/\/\/\/\/\/\/\/\
usuarios="Emtech"
contraseña="lifestore2020"

intentos=0
bandera=0
Total_ventas=[]
Total_reseña=[]
Total_busqueda=[]
Total_mensual=[]
Producto_con_reseña=[]
Venta_anual=[]
contador=0
promedio=0
contador_enero=0
contador_febrero=0
contador_marzo=0
contador_abril=0
contador_mayo=0
contador_junio=0
contador_julio=0
contador_agosto=0
contador_septiembre=0
contador_octubre=0
contador_noviembre=0
contador_diciembre=0
#/\/\/\/\/\/\Logica para extraer los productos y sus ventas /\/\/\/\/\/\/\/\
for product in lifestore_products:
  for venta in lifestore_sales:
    if product[0]==venta[1] and venta[4]==0:
     contador +=1
  formato_ideal=[product[0],product[1],contador,product[2],product[4]]
  Total_ventas.append(formato_ideal)
  contador=0
  #print(Total_ventas)
#/\/\/\/\/\/\Logica para extraer los productos y sus busquedas /\/\/\/\/\/\/\/\
for product in lifestore_products:
  for busqueda in lifestore_searches:
    if product[0]==busqueda[1]:
     contador +=1
  formato_ideal=[product[1],product[3],contador]
  Total_busqueda.append(formato_ideal)

  contador=0
#/\/\/\/\/\/\Logica para traer los productos con sus reseñas /\/\/\/\/\/\/\/\
contador=0
calif=0
promedio=0

for product in lifestore_products:  # Cuenta cuantas reseñas tiene sin contar las devoluciones
  for reseña in lifestore_sales:
    if product[0]==reseña[1]and reseña[4]==0:
      contador+=1
      calif+=reseña[2]
    if contador != 0 and calif !=0: 
      promedio=calif/contador
  formato_ideal=[product[1],promedio]
  Total_reseña.append(formato_ideal)
  #formato_ideal=[product[1],promedio]
  #Total_reseña.append(formato_ideal)
  contador=0
  calif=0
  promedio=0
#print(Total_reseña)

#promedio=calif/contador
#print(calif)
suma=0
#print(Total_ventas)
#/\/\/\/\/\/\Logica financiera /\/\/\/\/\/\/\/\
 # ventas totales
#print(veces_vendido)
for ventas in Total_ventas:     
  vvendidos=ventas[2]
  precio=ventas[3]
  multipla=vvendidos*precio

  suma+=multipla
  promedio_mensual=suma/12
  #contador=contador+1
#print(promedio_mensual)


for meses in lifestore_sales:
  venta_mensual=[meses[3]]
  Venta_por_mes=[meses[0],venta_mensual[0][3:5]]
  if Venta_por_mes[1]=="01":
    contador_enero+=1
    enero=[contador_enero]
  elif Venta_por_mes[1]=="02":
    contador_febrero+=1
    febrero=[contador_febrero]
  elif Venta_por_mes[1]=="03":
    contador_marzo+=1
    marzo=[contador_marzo]
  elif Venta_por_mes[1]=="04":
    contador_abril+=1
    abril=contador_abril
  elif Venta_por_mes[1]=="05":
    contador_mayo+=1
    mayo=[contador_mayo]
  elif Venta_por_mes[1]=="06":
    contador_junio+=1
    junio=[contador_junio]
  elif Venta_por_mes[1]=="07":
    contador_julio+=1
    julio=contador_julio
  elif Venta_por_mes[1]=="08":
    contador_agosto=0
    contador_agosto+=1
    agosto=[contador_agosto]
  elif Venta_por_mes[1]=="09":
    contador_septiembre+=1
    septiembre=[contador_septiembre]
  elif Venta_por_mes[1]=="10":
    contador_octubre+=1
    octubre=contador_octubre
  elif Venta_por_mes[1]=="11":
    contador_noviembre+=1
    diciembre=[contador_diciembre]
  elif Venta_por_mes[1]== "12":
    contador_diciembre+=1
    diciembre=contador_diciembre    
    #print(contador_enero)
  #print(x)





#/\/\/\/\/\/\Inicio de sesion/\/\/\/\/\/\/\/\
ID_usuario=input("Ingresa un usuario: ")
ID_contraseña=input("Ingresa una contraseña: ")

while intentos <= 3 and (ID_usuario != usuarios or ID_contraseña != contraseña):
  print("Datos de inicio de sesión incorrectos, favor de intentar de nuevo")
  intentos+= 1
  print("Intentos: " + str(intentos))
  ID_usuario=input("Ingresa un usuario: ")
  ID_contraseña=input("Ingresa una contraseña: ")
  if intentos >=2 and (ID_usuario != usuarios or ID_contraseña != contraseña):
    intentos += 1
    print("Intentos excedidos: "+ str(intentos))
    break

if intentos <=3 and (ID_usuario == usuarios and ID_contraseña == contraseña):
  print("Bienvenido a lifestore")
  menu=input("Seleccione el numero que desea visualizar:  \n 1 Productos mas vendidos. \n 2 Productos menos vendidos. \n 3 Productos con mejores reseñas. \n 4 Productos con peores reseñas. \n 5 Resumen financiero. \n 6 Mas buscados. \n 7 Menos buscados. \n opción: ")
  if menu=="1":
    bandera+=1
  elif menu=="2":
    bandera+=2
  elif menu=="3":
    bandera+=3
  elif menu=="4":
    bandera+=4
  elif menu=="5":
    bandera+=5
  elif menu=="6":
    bandera+=6
  elif menu=="7":
    bandera+=7
  #/\/\/\/\/\/\Logica para traer los 50 mas vendidos /\/\/\/\/\/\/\/\
if bandera == 1:
  Total_ventas.sort(key=lambda x:x[2],reverse=True)
  for indice in range (1,51):
    print ("Producto: ", Total_ventas[indice][1], "ventas", Total_ventas[indice][2],"con stock", Total_ventas[indice][4])
#/\/\/\/\/\/\Logica para traer los 50 menos vendidos /\/\/\/\/\/\/\/\
if bandera == 2:
  Total_ventas.sort(key=lambda x:x[2])
  for indice in range (1,51):
    print ("Producto: ", Total_ventas[indice][1], "ventas", Total_ventas[indice][2], "con stock", Total_ventas[indice][4])

#/\/\/\/\/\/\Logica para traer los 20 productos con mejores reseñas /\/\/\/\/\/\/\/\
if bandera == 3:
  Total_reseña.sort(key=lambda x:x[1],reverse=True)
  for indice in range (1,21):
    print ("Producto: ", Total_reseña[indice][0], "tiene un promedio de calificación de: ", Total_reseña[indice][1])#Total_reseña[indice][2]


#/\/\/\/\/\/\Logica para traer los 20 productos con las peores reseñas /\/\/\/\/\/\/\/\
if bandera == 4:
  Total_reseña.sort(key=lambda x:x[1])
  for indice in range (1,21):
    print ("Producto: ", Total_reseña[indice][0], "tiene un promedio de calificación de: ", Total_reseña[indice][1])#Total_reseña[indice][2]


#/\/\/\/\/\/\Logica para visualizar el resumen financiero/\/\/\/\/\/\/\/\
if bandera == 5:
  print("Venta_anual: ", suma, )
  print("Promedio mensual: ", promedio_mensual)
  print ("Venta mensual \n Enero", contador_enero,"pzs", "\n febrero", contador_febrero,"pzs" ,"\n marzo", contador_marzo, "pzs","\n abril",contador_abril,"pzs","\n mayo", contador_mayo,"pzs", "\n junio", contador_junio, "pzs","\n julio",contador_julio,"pzs","\n agosto", contador_agosto, "pzs","\n septiembre", contador_septiembre, "pzs","\n octubre",contador_octubre,"pzs","\n noviembre", contador_noviembre, "pzs""\n diciembre", contador_diciembre,"pzs")


#/\/\/\/\/\/\Logica para traer los 100 mas buscados /\/\/\/\/\/\/\/\
if bandera == 6:
  Total_busqueda.sort(key=lambda x:x[2],reverse=True)
  for indice in range (1,101):
    print ("Producto: ", Total_busqueda[indice][0]," de la categoria: ", Total_busqueda[indice][1], "fue buscado", Total_busqueda[indice][2], "veces")
#/\/\/\/\/\/\Logica para traer los 100 menos buscados/\/\/\/\/\/\/\/\
if bandera == 7:
  Total_busqueda.sort(key=lambda x:x[2])
  for indice in range (1,101):
    print ("Producto: ", Total_busqueda[indice][0]," de la categoria: ", Total_busqueda[indice][1], "fue buscado", Total_busqueda[indice][2], "veces")
#metodo de la burbuja
#if bandera == 7:
  #busqueda_ordenada=[]
  #while Total_busqueda:
   # minimo=Total_busqueda[1][2]
    #lista=Total_busqueda[0][1]
    #for tbusqueda in Total_busqueda:
        #if tbusqueda [2] < minimo:
          #  minimo=tbusqueda[1]
            #lista=tbusqueda
    #busqueda_ordenada.append(lista)
    #Total_busqueda.remove(lista)