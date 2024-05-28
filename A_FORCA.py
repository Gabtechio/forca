# O JOGO DA FORCA
import os,time
def jogar():
    jogada = (input("insirá uma letra"))
def tempo():
    time.sleep(3)
def espaco():
    print("          ")
def limpar():
    os.system("cls")
limpar()
print('''
        ___          _______   ______   .______        ______     ___      
       /   \        |   ____| /  __  \  |   _  \      /      |   /   \     
      /  ^  \       |  |__   |  |  |  | |  |_)  |    |  ,----'  /  ^  \    
     /  /_\  \      |   __|  |  |  |  | |      /     |  |      /  /_\  \   
    /  _____  \     |  |     |  `--'  | |  |\  \----.|  `----./  _____  \  
   /__/     \__\    |__|      \______/  | _| `._____| \______/__/     \__\ 
                                                                           
      ''')
tempo()
limpar()

desafiante = (input("Desafiante:"))
competidor = (input("Competidor:"))
limpar()

print (f"desafiante {desafiante} insirá:")
espaco()
chave = (input("Palavra chave: "))
palavrachave = ""
for letra in chave:
    palavrachave = palavrachave + "*"
espaco()
dica1 = (input("Dica 1: "))
espaco()
dica2 = (input("Dica 2: "))
espaco()
dica3 = (input("Dica 3: "))
limpar()

listachave = palavrachave
while True:
    print(f"PREPARE SE {competidor}")
    tempo()
    limpar()
    print(f'''
         |----------
         |         |
         |         O
         |        /|)
         |        / )
         |
         |
             {palavrachave}      ''')
    
    escolha = int(input("Jogar[1] ou Dica[2] ? "))
    if escolha == 2:
        jogadaletra = (input(f'''
 dica1: {dica1} 
 agora insirá uma letra: '''))
    else:
        jogadaletra = (input("insirá uma letra:"))
        
        jogada = jogadaletra
        palavrachave = ""
        for letra in chave:
            if letra == jogada:
                palavrachave = palavrachave + letra
            else:
                  palavrachave = palavrachave + "*" 
                  
            limpar()

    
   






        

                
    
        
    





    
    

    


