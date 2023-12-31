import game_ptbr as br
import game_enus as us
import game_dede as de

languages = ["Inglês (en-US)", "Português do Brasil (pt-BR)", "Alemão (de-DE)"]
options = len(languages)

def language():
            
    while True:
        
        print("Language Select | Escolha o idioma:")
        
        for indice,language in enumerate(languages):
            print(f'{indice + 1} - {language}')
        
        choice = input("=> ")
        
        match choice:
            case "1":
                us.menu_us()
                break
            case "2":
                br.menu_br()
                break
            case "3":
                de.menu_de()
                break
            case _:
                print("Invalid selection. Please select a valid option\n"
                      "Seleção inválida. Por favor, selecione uma opção válida:\n")
                
                

   



        