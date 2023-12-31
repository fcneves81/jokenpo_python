from random import randint
from time import sleep

vitorias = 0
empates = 0
derrotas = 0

def menu_us():
    
    while True:
      
        print("\nMake your choice:")
        
        opcoes = ["👊 Rock", "🖐️  Paper", "✌️  Scissors", "🤔 How to play", "🛑 EXIT"]
                
        for indice,opcao in enumerate(opcoes):
            print(f'{indice + 1} - {opcao}')
            
        jogada = input("=> ")
        jogada_pc = randint(1,3)
                        
        match jogada:
            case "1":
                jokenpo()              
                print("You choose ROCK 👊")
                sleep(1)
                if jogada_pc == 1:
                  print("The computer also chose ROCK 👊")
                  sleep(1)
                  empate()
                elif jogada_pc == 2:
                  print("The computer chose PAPER 🖐️")
                  sleep(1)
                  derrota()
                else:
                  print("The computer chose SCISSORS ✌️")
                  sleep(1)
                  vitoria()
                break
            
            case "2":
                jokenpo()
                print("You choose PAPER 🖐️")
                sleep(1)
                if jogada_pc == 1:
                  print("The computer chose ROCK 👊")
                  sleep(1)
                  vitoria()
                                    
                elif jogada_pc == 2:
                  print("The computer also chose PAPER 🖐️")
                  sleep(1)
                  empate()
                else:
                  print("The computer chose SCISSORS ✌️")
                  sleep(1)
                  derrota()
                break
                
            case "3":
                jokenpo()
                print("You choose SCISSORS ✌️")
                sleep(1)
                if jogada_pc == 1:
                  print("The computer chose ROCK 👊")
                  sleep(1)
                  derrota()
                elif jogada_pc == 2:
                  print("The computer chose PAPER 🖐️")
                  sleep(1)
                  vitoria()
                else:
                  print("The computer also chose SCISSORS ✌️")
                  sleep(1)
                  empate()
                break
            
            case "4":
                print("\nYou choose between ROCK, PAPER ou SCISSORS\n"
                      "The computer will also make a choice and the result will be defined:\n"
                      "ROCK wins from SCISSORS (The ROCK breaks the SCISSORS)\n"
                      "PAPER wins from ROCK (The PAPER wraps the ROCK)\n"
                      "SCISSORS wins from PAPER (The SCISSORS cut PAPER)")
                menu_us()
                break
            case "5":
                print("🤩  Thanks for playing! 🤩")
                sleep(1)
                resultado()
                break
            case _:
                print("❗ Invalid selection. Please select a valid option! ❗")
        

def jokenpo():
  sleep(1)
  print("JO.. 👊")
  sleep(1)
  print(".KEN.🖐️")
  sleep(1)
  print("..PO ✌️")
  sleep(1)

def vitoria():
  print("😁 YOU WIN!!!!!!")
  global vitorias
  vitorias += 1
  menu_us()
    
  
def derrota():
  print("😖 What a shame... you lost")
  global derrotas
  derrotas += 1
  menu_us()
  
def empate():
  print("😐 It's a draw!")
  global empates
  empates += 1
  menu_us()      

def resultado():
  global vitorias
  global derrotas
  global empates
  
  if vitorias == 0 and empates == 0 and derrotas == 0:
    print("🚨 Unfortunately there is no score to show 🚨")
  else:
    print()
    print("=" * 45)
    print("✨✨✨ MATCH RESULTS ✨✨✨".center(40))
    print("=" * 45)
    print()
    print(f"😁  VICTORIES: \t{vitorias}\n"
          f"😖  DEFEATS: \t{derrotas}\n"
          f"😐  TIES: \t{empates}\n")
    print("=" * 45)