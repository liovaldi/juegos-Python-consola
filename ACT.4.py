#TP integrador – Repetitivas- Condicionales y Secuenciales. // Iovaldi Ludmila // Comision 2
#Ejercicio 4  — “Escape Room: La Bóveda”

#Mensaje de bienvenida
print("*** Escape Room: La Bóveda ***")

print("Eres un agente con una misión critica: abrir las 3 cerraduras que protegen una bóveda impenetrable.")
print("Dispones de energía y tiempo limitados para lograrlo.")

print("CONDICIONES DE VICTORIA:")
print("- Abrir las 3 cerraduras antes de quedarte sin energía o sin tiempo.")

print("CONDICIONES DE DERROTA:")
print("- Si tu energía llega a 0.")
print("- Si tu tiempo llega a 0.")
print("- Si la alarma se activa y bloquea el sistema.")

print("Cada decisión que tomes será vital:")
print("- Forzar cerraduras te acerca rápido al éxito, pero consume mucha energía.")
print("- Hackear paneles requiere paciencia, pero puede darte acceso seguro.")
print("- Descansar recupera fuerzas, aunque el reloj sigue corriendo.")

print("¿Lograrás abrir la bóveda y cumplir tu misión?")
print("La suerte y tu estrategia decidirán el resultado.")
print("-------------------------------------------------------------------------------")

#Variables
energia = 100 
tiempo = 12 
cerraduras_abiertas = 0 
alarma = False 
codigo_parcial = "" 
case1= 0  
#nombre del agente
agente= input("Introduce el nombre del agente: ").strip().lower()
while not agente.isalpha():
    print("Error# el nombre solo puede contener letras")
    agente= input("Introduce el nombre del agente: ").strip().lower()

#Informacion de pantalla
print("Bienvendio agente ",agente)

#Menu de opciones
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
        print("ALARMA ENCENDIDA > La boveda se cerro por bloqueo")
        print("---DERROTA: el sistema se bloqueo---")
        break
    print(f"|ENERGIA: {energia} | TIEMPO: {tiempo} | CERRRADURAS ABIERTAS: {cerraduras_abiertas} | ALARMA: {alarma} |CODIGO PARCIAL: {codigo_parcial} |")
    
    print("1) Forzar cerradura" )
    print("2) Hackear panel")
    print("3) Descansar ")
    print("0) Salir del juego")
#Solicitud de numero para ingresar al menu y validacion
    estrategia=input("Elije tu mejor estrategia: ").strip()
    while not estrategia.isdigit(): 
        print("Error# ingrese un numero correcto")
        estrategia=input("Elije tu mejor estrategia: ").strip()
    estrategia=int(estrategia)
    while estrategia < 0 or estrategia > 3:
        print("Error# ingrese un numero correcto")
        estrategia=input("Elije tu mejor estrategia: ").strip()
        while not estrategia.isdigit():
            print("Error# ingrese un numero correcto")
            estrategia=input("Elije tu mejor estrategia: ").strip()
        estrategia=int(estrategia)
            
#Desarrollo del menu
    match estrategia:
#Forzar cerradura
#Ejecucion case 1 
        case 1:
            print("Forzando cerradura...")
            energia -= 20
            tiempo -= 2
#contador de ingresos a la opcion
            case1 += 1
            if case1 == 3:
                energia -= 20
                tiempo -= 2
                print("Anti-spam detectado ##Alarma activada##")
                alarma = True
            if alarma == False:
                cerraduras_abiertas +=1
#condicion case 1 
            if energia < 40:
                num= input("¡¡RIESGO DE ALARMA!! por favor, ingrese un numero del 1 al 3: ")
                while not num.isdigit(): 
                    print("Error# numero seleccionado incorrecto")
                    num= input("¡¡RIESGO DE ALARMA!! por favor, ingrese un numero del 1 al 3: ")
                num=int(num)
                if num == 3:
                    alarma=True
                    print("<<<<<ALARMA ENCENDIDA>>>>>")
                else:
                    cerraduras_abiertas += 1 
                    print("Abriste una cerradura")
        case 2:
#ejecucion case 2
            print("Hakeando panel...")
            case1 = 0
            energia -=10
            tiempo -=3
            for codi in range(4):
                codigo_parcial += "O"
                print(f"|CODIGO PARCIAL: {codigo_parcial} |")
            if len(codigo_parcial)>= 8:
                cerraduras_abiertas +=1
                print("Abriste una cerradura")
                

        case 3:
#ejecucion case 3
            print("Descansando zZZ")
            case1 = 0
            tiempo -=1
            if energia >= 100:
                energia += 0
            else:
                energia += 15
                
            if alarma == True:
                print("ATENCION!! ALARMA ENCENDIDA > se descuentan 10 puntos de energia ")
                energia -= 10 

        case 0:
            print("Hasta luego...")
            break
#Condiciones de fin        
if cerraduras_abiertas == 3:
    print("MISION CUMPLIDA, felicidades agente",agente)
if energia <= 0:
    print("DERROTA## Te quedaste sin energía.")
if tiempo <= 0:
    print("DERROTA## Se agotó el tiempo.")

#observacion: cuando ingresas 3 veces a forzar cerradura, coincide con if energia <40, 
# por lo que aparece simultaneamente la funcion del riesgo de alarma con la alarma activada.
