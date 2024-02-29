'''Elaborar un programa en Python el cual tiene los siguientes productos: 1.
Computador de escritorio 2. Computador de escritorio 3. Tabletas 4. Videobeam 5.
Televisores y determinar cuantos de cada uno se han comprado, tener en cuenta
que el precio de los artículos debe estar establecidos de manera constante, el
sistema debe recibir todos los productos de manera infinita y al momento de
seleccionar la opción de “FACTURAR” debe mostrar el total de la suma de los
artículos, cuantos de cada uno se agregaron, el total a pagar'''

computadorEscritorio = 3100000
computadorPortatil = 2200000
tableta = 1500000
videobeam = 600000
televisor = 2800000

import os
#inicializar valores
control = True
total = 0
cComputador = 0
cPortatil = 0
cTableta = 0
cVideobeam = 0
cTelevisor = 0
 
 # ENTRADA 
while (control == True) :
    os.system ('cls')
    #MENU
    print('\t.: Tienda alexbbelectro:.\n\n[0] Facturacion\n[1] Computador escritorio (3.1M)\n[2]Computador Portatil (2.2M) [3]Tabletas(1.5M)\n[4]VideoBeam(600K)\n[4]Televisor(2.8M)')
    opcion = int(input('[] -->'))
    if opcion == 0:
             control = False
    elif opcion == 1:
             control = computadorEscritorio
             cComputador += 1
    elif opcion == 2:
            total += computadorPortatil
            cPortatil += 1
    elif opcion == 3:
            total += tableta
            cTableta += 1
    elif opcion == 4:
             total += videobeam
             cVideobeam += 1
    elif opcion == 5:
            total += televisor
            cTelevisor += 1
            
    if opcion != 0:
                input('compra realizada con exito (Enter para continuar)')
                
                
if total != 0:
    print(f'\t << menu de facturacion')