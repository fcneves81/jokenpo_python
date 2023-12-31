from random import randint
from time import sleep

vitorias = 0
empates = 0
derrotas = 0

def menu_br():
    
    while True:
      
        print("\nQual será a sua jogada:")
        
        opcoes = ["👊 Pedra", "🖐️  Papel", "✌️  Tesoura", "🤔 Como jogar", "🛑 SAIR"]
                
        for indice,opcao in enumerate(opcoes):
            print(f'{indice + 1} - {opcao}')
            
        jogada = input("=> ")
        jogada_pc = randint(1,3)
                        
        match jogada:
            case "1":
                jokenpo()              
                print("Você escolheu PEDRA 👊")
                sleep(1)
                if jogada_pc == 1:
                  print("O computador também escolheu PEDRA 👊")
                  sleep(1)
                  empate()
                elif jogada_pc == 2:
                  print("O computador escolheu PAPEL 🖐️")
                  sleep(1)
                  derrota()
                else:
                  print("O computador escolheu TESOURA ✌️")
                  sleep(1)
                  vitoria()
                break
            
            case "2":
                jokenpo()
                print("Você escolheu PAPEL 🖐️")
                sleep(1)
                if jogada_pc == 1:
                  print("O computador escolheu PEDRA 👊")
                  sleep(1)
                  vitoria()
                                    
                elif jogada_pc == 2:
                  print("O computador também escolheu PAPEL 🖐️")
                  sleep(1)
                  empate()
                else:
                  print("O computador escolheu TESOURA ✌️")
                  sleep(1)
                  derrota()
                break
                
            case "3":
                jokenpo()
                print("Você escolheu TESOURA ✌️")
                sleep(1)
                if jogada_pc == 1:
                  print("O computador escolheu PEDRA 👊")
                  sleep(1)
                  derrota()
                elif jogada_pc == 2:
                  print("O computador escolheu PAPEL 🖐️")
                  sleep(1)
                  vitoria()
                else:
                  print("O computador também escolheu TESOURA ✌️")
                  sleep(1)
                  empate()
                break
            
            case "4":
                print("\nVocê escolhe entre PEDRA, PAPEL ou TESOURA\n"
                      "O computador também irá fazer uma escolha e será definido o resultado:\n"
                      "PEDRA ganha de TESOURA (A pedra quebra a tesoura)\n"
                      "PAPEL ganha de PEDRA (O papel enrola a pedra)\n"
                      "TESOURA ganha de PAPEL (A tesoura corta o papel)")
                menu_br()
                break
            case "5":
                print("🤩  Obrigado por jogar! 🤩")
                sleep(1)
                resultado()
                break
            case _:
                print("❗ Seleção inválida. Por favor, selecione uma opção válida! ❗")
        

def jokenpo():
  sleep(1)
  print("JO.. 👊")
  sleep(1)
  print(".KEN.🖐️")
  sleep(1)
  print("..PO ✌️")
  sleep(1)

def vitoria():
  print("😁 VOCÊ VENCEU!!!!!!")
  global vitorias
  vitorias += 1
  menu_br()
    
  
def derrota():
  print("😖 Que pena, você perdeu")
  global derrotas
  derrotas += 1
  menu_br()
  
def empate():
  print("😐 Temos um empate!")
  global empates
  empates += 1
  menu_br()      

def resultado():
  global vitorias
  global derrotas
  global empates
  
  if vitorias == 0 and empates == 0 and derrotas == 0:
    print("🚨 Infelizmente não há um placar para mostrar 🚨")
  else:
    print()
    print("=" * 45)
    print("✨✨✨ RESULTADOS DA PARTIDA ✨✨✨".center(40))
    print("=" * 45)
    print()
    print(f"😁  VITÓRIAS: \t{vitorias}\n"
          f"😖  DERROTAS: \t{derrotas}\n"
          f"😐  EMPATES: \t{empates}\n")
    print("=" * 45)