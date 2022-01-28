import moves as move
import random
def Data_pokemon(nombre_archivo):
     libreria=open(nombre_archivo, "r")
     contador = 2
     pokemon = input("Ingrese el nombre del primer Pokémon: ")
     print(f"Nombre del Pokémon seleccionado: {pokemon}")
     for linea in libreria:
          Datos_pokemon = linea.split(",")
          if(pokemon == Datos_pokemon[0]):
               nombre=Datos_pokemon[0]
               tipo = Datos_pokemon[1]
               hp = int(Datos_pokemon[2])
               ataquefisico = int(Datos_pokemon[3])
               defensafisica = int(Datos_pokemon[4])
               ataqueespecial = int(Datos_pokemon[5])
               defensaespecial = int(Datos_pokemon[6])
               velocidad = int(Datos_pokemon[7])
               ataques = Datos_pokemon[8].split(";")
               nro = contador
               print(f"  - HP = {hp} ")
               print(f"  - Ataque = {ataquefisico}")
               print(f"  - Defensa = {defensafisica}")
               print(f"  - Ataque especial = {ataqueespecial}")
               print(f"  - Defensa especial = {defensaespecial}")
               print(f"  - Velocidad = {velocidad}")
               numeros = 0
               poderes = []
               print("Movimientos que puede aprender el pokémon: ")
               for i in ataques:
                    print(f"{numeros} - {i}")
                    poderes.append(i)
                    numeros += 1
               poder = int(input("Seleccione un ataque a ejecutar: "))
               print(f"El ataque seleccionado es: {poderes[poder]}")
               moves = move.get_move(poderes[poder])
               print(f"Poder del ataque es : {moves[1]}")
               Poderataque = moves[1]
               while Poderataque == 0:
                    poder = int(input("El ataque seleccionado tiene un poder igual a 0, ingrese otro poder: "))
                    moves = move.get_move(poderes[poder])
                    print(f"El ataque seleccionado es: {poderes[poder]}")
                    print(f"Poder del ataque es : {moves[1]}")
                    Poderataque = moves[1]
               if Poderataque != 0:
                    Poderataque = moves[1]

               return nombre,tipo, hp, ataquefisico, defensafisica, ataqueespecial, defensaespecial, velocidad, nro, ataques, poder, moves, Poderataque
          contador = contador + 1
     libreria.close()
def Data_pokemon2(nombre_archivo):
     libreria=open(nombre_archivo, "r")
     contador = 2
     pokemon = input("Ingrese el nombre a atacar Pokémon: ")
     for linea in libreria:
          Datos_pokemon = linea.split(",")
          if (pokemon == Datos_pokemon[0]):
               nombre = Datos_pokemon[0]
               tipo = Datos_pokemon[1]
               hp = int(Datos_pokemon[2])
               ataquefisico = int(Datos_pokemon[3])
               defensafisica = int(Datos_pokemon[4])
               ataqueespecial = int(Datos_pokemon[5])
               defensaespecial = int(Datos_pokemon[6])
               velocidad = int(Datos_pokemon[7])
               nro = contador
               ataques = Datos_pokemon[8].split(";")
               print(f"Nombre del Pokémon seleccionado: {pokemon}")
               return nombre,tipo, hp, ataquefisico, defensafisica, ataqueespecial, defensaespecial, velocidad, nro, ataques
          contador = contador + 1
     libreria.close()

def Calculos_vida(Base):
     EV, IV, Level = 250, 31, 50
     HP = ((((Base + IV) * 2 + (EV**(0.5)) / 4) * Level) / 100) + Level + 10
     return HP
def Calculos_Generales(data_atk,data_Def,data_s_atk,data_s_def,data_Spe):
     EV, Level, IV = 250, 50, 31
     Atk = ((((data_atk + IV) * 2 + (EV **(0.5)) / 4) * Level) / 100) + 5
     Def = ((((data_Def + IV) * 2 + (EV **(0.5)) / 4) * Level) / 100) + 5
     S_atk = ((((data_s_atk + IV) * 2 + (EV **(0.5)) / 4) * Level) / 100) + 5
     S_def = ((((data_s_def + IV) * 2 + (EV **(0.5)) / 4) * Level) / 100) + 5
     Spe = ((((data_Spe + IV) * 2 + (EV **(0.5)) / 4) * Level) / 100) + 5
     return Atk,Def,S_atk,S_def,Spe

def Efectividad(atacante, atacado):
     libreria=open("tabla_efectividad.csv","r")
     linea = libreria.readline().strip()
     data = linea.split(",").index(atacado)
     while linea:
          linea = libreria.readline()
          datax = linea.split(",")
          if datax[0] == atacante:
               return float(datax[data])

def calculo_daño(tipo,tipo2,type, ataque_especial, defensa_especial, Daño_Data):
     Randomnum = random.uniform(0.85,1)
     stab = 0
     if(tipo == tipo2):
          stab = 1
     elif(tipo != tipo2):
          stab = 1.2
     modifier = float(type * stab * Randomnum * 1)
     Damage = ((((((2 * 50) / 5) + 2) * Daño_Data * ataque_especial / defensa_especial) / 50) + 2) * modifier
     return Damage
