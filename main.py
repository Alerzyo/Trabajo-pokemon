import funciones as ejecutar

print("Bienvenido al simulador")

pokemon1 = ejecutar.Data_pokemon("pokemon_data") #Sacar Datos del Pokemon
nombre, tipo, Base, ataque, defensa, especial_a, especial_d, velocidad, poder, PW = pokemon1[0], pokemon1[1], pokemon1[2], pokemon1[3], pokemon1[4], pokemon1[5], pokemon1[6], pokemon1[7], pokemon1[8], pokemon1[11]
for i in PW:
     Daño_Data = PW[1]
vida = ejecutar.Calculos_vida(Base) #Vida pokemon nivel 50
estadisticas = ejecutar.Calculos_Generales(ataque, defensa, especial_a, especial_d, velocidad) #Stats de pokemon al lvl 50
atk, Def, spe = estadisticas[0], estadisticas[3], estadisticas[4]
ataque_especial, def_especial = estadisticas[2], estadisticas[1]
print(f"El HP al nivel 50 de {nombre} es {vida}")
print(f"El Atk al nivel 50 de {nombre} es {atk}")
print(f"El Def al nivel 50 de {nombre} es {def_especial}")
print(f"El Spa al nivel 50 de {nombre} es {ataque_especial}")
print(f"El Spd al nivel 50 de {nombre} es {Def}")
print(f"El Spe al nivel 50 de {nombre} es {spe}")

pokemon2 = ejecutar.Data_pokemon2("Pokemon_data") #Datos pokemon 2
nombre2, tipo2, Base2, ataque2, defensa2, especial_a2, especial_d2, velocidad2 = pokemon2[0], pokemon2[1], pokemon2[2], pokemon2[3], pokemon2[4], pokemon2[5], pokemon2[6], pokemon2[7]
vida2 = ejecutar.Calculos_vida(Base2) #Vida lvl 50 pokemon 2
estadisticas2 = ejecutar.Calculos_Generales(ataque2,defensa2,especial_a2,especial_d2,velocidad2) #calculos generales de el pokemon 2
efectividad = ejecutar.Efectividad(tipo, tipo2) # efectividad entre los tipos
defensa_especial = estadisticas2[1]
daño = ejecutar.calculo_daño(tipo,tipo2,efectividad,ataque_especial,defensa_especial,Daño_Data)
print(f"El hp al nivel 50 de {nombre2} es {vida2} ")
print(f"El daño que realizó {nombre} a {nombre2} fue de: {daño} ")
vidafinal = vida2 - daño
print(f"{nombre2} quedo con un HP de = {vidafinal}")





