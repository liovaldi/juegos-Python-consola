#TP integrador – Repetitivas- Condicionales y Secuenciales. // Iovaldi Ludmila // Comision 2
#Ejercicio 5  — “Escape Room:"La Arena del Gladiador"

#Mensaje de bienvenida:
print("⚔️ --- BIENVENIDO A LA ARENA DEL GLADIADOR --- ⚔️")
print("Las puertas se abren y el rugido del público retumba en tus oídos. La arena está lista, el enemigo espera, y tu destino se decide aquí.")
print("🔹 Tu misión:")
print("Derrotar al enemigo antes de que él acabe contigo. Solo uno saldrá con vida.")
print("🔹 Reglas del combate:")
print("Ataca con fuerza: Un Golpe Pesado puede volverse crítico si el enemigo está debilitado.")
print("Desata tu furia: La Ráfaga Veloz golpea tres veces seguidas, desgastando a tu rival.")
print("Sobrevive con astucia: Usa tus pociones para recuperar fuerzas… pero cuidado, ¡son limitadas!")
print("🔹 El riesgo:")  
print("Tras cada acción, el enemigo contraataca sin piedad. Si tus puntos de vida llegan a 0, la arena se teñirá con tu derrota.")
print("El combate comienza ahora…")
print("¡Gladiador, demuestra tu valor y conquista la victoria!")

#Nombre del usuario 
gladiador=input("Introduzca el nombre del gladiador: ").strip().upper()
while not gladiador.isalpha():
    print("Error# solo se permiten letras.")
    gladiador=input("Introduzca el nombre del gladiador: ").strip().upper()
print("=== INICIO DEL COMBATE ===")

#Variables
vida_gladiador = 100
vida_enemigo = 100
pociones_vida = 3
daño_base_pesado = 15
daño_base_enemigo = 12
turno_gladiador = True

#Condicion de inicio
while vida_gladiador and vida_enemigo > 0:
    print(f"| {gladiador}: {vida_gladiador} vs. ENEMIGO: {vida_enemigo} | POCIONES DE VIDA: {pociones_vida} | ")
#Menu de combate
    print("1) Ataque pesado")
    print("2) Rafaga veloz")
    print("3) Curar")
    opcion_combate= input("Escoje tu opcion para combatir: ").strip()
#Validacion de datos
    while not opcion_combate.isdigit():
        print("Error# escoja un numero correcto")
        opcion_combate= input("Escoje tu opcion para combatir: ").strip()
    opcion_combate=int(opcion_combate)
    while opcion_combate < 1 or opcion_combate > 3:
        print("Error# escoja un numero correcto")
        opcion_combate= input("Escoje tu opcion para combatir: ").strip()
        while not opcion_combate.isdigit():
            print("Error# escoja un numero correcto")
            opcion_combate= input("Escoje tu opcion para combatir: ").strip()
        opcion_combate=int(opcion_combate)

    match opcion_combate: 
        case 1: #Accion A: ataque pesado
            daño_final= 0
            if vida_enemigo < 20:
                daño_final = daño_base_pesado *1.5
                vida_enemigo -= daño_final
                daño_final=float(daño_final)
                print(f"Atacaste al enemigo por {daño_final} puntos. ")
                turno_gladiador = False
                vida_gladiador -= daño_base_enemigo
                print(">>¡El enemigo contraataca con 12 puntos de daño!")
            else:
                vida_enemigo-=daño_base_pesado
                print(f"Atacaste al enemigo por {daño_base_pesado} puntos. ")
                turno_gladiador = False
                vida_gladiador -= daño_base_enemigo
                print(">>¡El enemigo contraataca con 12 puntos de daño!")

        case 2: #Accion B: rafaga veloz
            print(">> Inicias una rafaga de golpes!")
            for golpe in range (1,4):
                vida_enemigo -= 5
                print(f">Golpe {golpe} conectado por 5 puntos de daño.")
            turno_gladiador = False
            vida_gladiador -= daño_base_enemigo
            print(">>¡El enemigo contraataca con 12 puntos de daño!")
        
        case 3: #Accion C: curar
            if pociones_vida > 0:
                vida_gladiador += 30
                pociones_vida -=1
            else:
                print("---¡No te quedan mas pociones!---")
                vida_gladiador -= daño_base_enemigo
                print(">>¡El enemigo contraataca con 12 puntos de daño!")
#Fin del juego
if vida_gladiador > 0:
    print(f"¡VICTORIA! <<{gladiador} ha ganado la batalla>>")
else:
    print(f"DERROTA. has Has caído en combate.")