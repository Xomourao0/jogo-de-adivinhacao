import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0 

    chute = int(input("A máquina irá escolher um número aleatório entre 1 e 100. Tente adivinhar, Digite o seu número:"))
    
    while chute != numero_secreto:
        tentativas += 1 
        
        if chute > numero_secreto:
           print("Errado! Esse número é maior")
        elif chute < numero_secreto:
             print("Errado! Esse número é menor")
     
     
        tentativas += 1 
        chute = int(input("tente novamente:"))

    print (f"O chute esta certo!! Parabens! Você acertou em {tentativas} tentativas.")  

jogo_adivinhacao()

 
