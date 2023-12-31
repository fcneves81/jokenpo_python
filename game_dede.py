from random import randint
from time import sleep

"""
SCHNICK ✌️
SCHNACK 🖐️
SCHNUCK 👊

"""

vitorias = 0
empates = 0
derrotas = 0

def menu_de():
    
    while True:
      
        print("\nMake your choice:")
        
        opcoes = ["✌️  Schnick", "🖐️  Schnack","👊 Schnuck", "🤔 SPIELANLEITUNG" , "🛑 AUSGEHEN"]
                
        for indice,opcao in enumerate(opcoes):
            print(f'{indice + 1} - {opcao}')
            
        jogada = input("=> ")
        jogada_pc = randint(1,3)
                        
        match jogada:
            case "1":
                jokenpo()              
                print("Du wählst SCHNICK ✌️")
                sleep(1)
                if jogada_pc == 1:
                  print("Der Computer wählte auch SCHNICK ✌️")
                  sleep(1)
                  empate()
                elif jogada_pc == 2:
                  print("Der Computer wählte SCHNACK 🖐️")
                  sleep(1)
                  vitoria()
                else:
                  print("Der Computer wählte SCHNUCK 👊")
                  sleep(1)
                  derrota()
                break
            
            case "2":
                jokenpo()
                print("Du wählst SCHNACK 🖐️")
                sleep(1)
                if jogada_pc == 1:
                  print("Der Computer wählte SCHNICK ✌️")
                  sleep(1)
                  derrota()
                                    
                elif jogada_pc == 2:
                  print("Der Computer wählte auch SCHNACK 🖐️")
                  sleep(1)
                  empate()
                else:
                  print("Der Computer wählte SCHNUCK 👊")
                  sleep(1)
                  vitoria()
                break
                
            case "3":
                jokenpo()
                print("Du wählst SCHNUCK 👊")
                sleep(1)
                if jogada_pc == 1:
                  print("Der Computer wählte SCHNICK ✌️")
                  sleep(1)
                  vitoria()
                elif jogada_pc == 2:
                  print("Der Computer wählte SCHNACK 🖐️")
                  sleep(1)
                  derrota()
                else:
                  print("Der Computer wählte auch SCHNUCK 👊")
                  sleep(1)
                  empate()
                break
            
            case "4":
                print("\nSie wählen zwischen SCHNICK, SCHINACK oder SCHNUCK\n"
                      "Der Computer trifft ebenfalls eine Auswahl und das Ergebnis wird definiert:\n"
                      "SCHNICK gewinnt aus SCHNACK\n"
                      "SCHNACK gewinnt aus SCHNUCK\n"
                      "SCHNUCK gewinnt aus SCHNICK")
                menu_de()
                break
            case "5":
                print("🤩  Danke fürs Spielen! 🤩")
                sleep(1)
                resultado()
                break
            case _:
                print("❗ Ungültige Auswahl. Bitte wählen Sie eine gültige Option! ❗")
        

def jokenpo():
  sleep(1)
  print("SCHNICK.. ✌️")
  sleep(1)
  print(".SCHNACK.🖐️")
  sleep(1)
  print("..SCHNUCK 👊")
  sleep(1)

def vitoria():
  print("😁 DU GEWINNST!!!!!!")
  global vitorias
  vitorias += 1
  menu_de()
    
  
def derrota():
  print("😖 Was für eine Schande... du hast verloren")
  global derrotas
  derrotas += 1
  menu_de()
  
def empate():
  print("😐 Es ist eine Zeichnung!")
  global empates
  empates += 1
  menu_de()      

def resultado():
  global vitorias
  global derrotas
  global empates
  
  if vitorias == 0 and empates == 0 and derrotas == 0:
    print("🚨 Leider ist kein Punktestand vorhanden 🚨")
  else:
    print()
    print("=" * 45)
    print("✨✨✨ SPIELERGEBNISSE ✨✨✨".center(40))
    print("=" * 45)
    print()
    print(f"😁  SIEGE: \t\t{vitorias}\n"
          f"😖  NIEDERLAGEN: \t{derrotas}\n"
          f"😐  KRAWATTEN: \t\t{empates}\n")
    print("=" * 45)
    