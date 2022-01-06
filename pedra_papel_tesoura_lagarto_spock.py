# Pedra, Papel, Tesoura, Lagarto, Spock, por Sheldon Cooper
# Programado por: Gabriel Morishita
import random
import time

while True:
    escolhas = ["PEDRA", "PAPEL", "TESOURA", "LAGARTO", "SPOCK"]

    computador = random.choice(escolhas)
    usuario = None
    print("Regras: \n Pedra, papel, tesoura, lagarto, Spock. É muito simples.\n "
          "Olhe – tesoura corta papel, papel cobre pedra, pedra esmaga lagarto,\n "
          "lagarto envenena Spock, Spock esmaga tesoura, tesoura decapita lagarto,\n "
          "lagarto come papel, papel refuta Spock, Spock vaporiza pedra \n"
          " e como sempre, pedra quebra tesoura.\n")

    while usuario not in escolhas:

        usuario = input("Escolha entre: Pedra, Papel, Tesoura, Lagarto ou Spock: ").upper()

        if usuario == computador:
            print("Você: ", usuario)
            print("Sheldon: ", computador)
            time.sleep(1)
            print("Teóricamente é um empate, e de acordo com o 'Acordo dos Colegas de Quarto',"
                  " Sheldon decide todos os empates de um contra um, portanto")
            time.sleep(3)
            print("Sheldon Vence!")

        elif usuario == "PEDRA":
            if computador == "PAPEL":
                print("Você: ", usuario)
                print("Sheldon: ", computador)
                time.sleep(1)
                print("Sua pedra foi coberta pelo papel de Sheldon")
                time.sleep(1)
                print("Sheldon Vence!")
            if computador == "TESOURA":
                print("Você: ", usuario)
                print("Sheldon: ", computador)
                time.sleep(1)
                print("Sua pedra esmaga a tesoura de Sheldon.")
                time.sleep(1)
                print("Sheldon taca a pedra pela janela")
                time.sleep(1)
                print("Sheldon Vence!")
            if computador == "LAGARTO":
                print("Você: ", usuario)
                print("Sheldon: ", computador)
                time.sleep(1)
                print("Sua pedra esmaga o lagarto de Sheldon.")
                time.sleep(1)
                print("Lagarto se regenera e foge")
                time.sleep(1)
                print("Sheldon taca a pedra pela janela")
                time.sleep(1)
                print("Sheldon Vence!")
            if computador == "SPOCK":
                print("Você: ", usuario)
                print("Sheldon: ", computador)
                time.sleep(1)
                print("Spock vaporiza a sua pedra")
                time.sleep(1)
                print("Sheldon Vence!")
        elif usuario == "PAPEL":
            if computador == "PEDRA":
                print("Você: ", usuario)
                print("Sheldon: ", computador)
                time.sleep(1)
                print("Seu papel cobre a pedra de Sheldon")
                time.sleep(1)
                print("Sheldon amassa seu papel")
                time.sleep(1)
                print("Sheldon Vence!")
            if computador == "TESOURA":
                print("Você: ", usuario)
                print("Sheldon: ", computador)
                time.sleep(1)
                print("A tesoura de Sheldon corta seu papel")
                time.sleep(1)
                print("Sheldon Vence!")
            if computador == "LAGARTO":
                print("Você: ", usuario)
                print("Sheldon: ", computador)
                time.sleep(1)
                print("Seu papel foi engolido pelo lagarto de Sheldon")
                time.sleep(1)
                print("Sheldon Vence!")
            if computador == "SPOCK":
                print("Você: ", usuario)
                print("Sheldon: ", computador)
                time.sleep(1)
                print("Seu papel refuta Spock")
                time.sleep(1)
                print("Spock não fala português e não entende o que está escrito")
                time.sleep(1)
                print("Spock rasga o papel")
                time.sleep(1)
                print("Sheldon Vence!")
        elif usuario == "TESOURA":
            if computador == "PEDRA":
                print("Você: ", usuario)
                print("Sheldon: ", computador)
                time.sleep(1)
                print("Sua tesoura foi esmagada pela pedra de Sheldon")
                time.sleep(1)
                print("Sheldon Vence!")
            if computador == "PAPEL":
                print("Você: ", usuario)
                print("Sheldon: ", computador)
                time.sleep(1)
                print("Você corta o papel de Sheldon")
                time.sleep(1)
                print("Sheldon pega a sua tesoura e quebra")
                time.sleep(1)
                print("Sheldon ainda tem um papel em seu bolso")
                time.sleep(1)
                print("Sheldon Vence!")
            if computador == "LAGARTO":
                print("Você: ", usuario)
                print("Sheldon: ", computador)
                time.sleep(1)
                print("Sua tesoura degola o lagarto de Sheldon")
                time.sleep(1)
                print("Sheldon chama a Penny que estava com medo do Lagarto")
                time.sleep(1)
                print("Penny pega a sua tesoura emprestada e nunca mais devolve")
                time.sleep(1)
                print("Sheldon Vence!")
            if computador == "SPOCK":
                print("Você: ", usuario)
                print("Sheldon: ", computador)
                time.sleep(1)
                print("Sua pedra foi amassada por Spock")
                time.sleep(1)
                print("Sheldon Vence!")
        elif usuario == "LAGARTO":
            if computador == "PEDRA":
                print("Você: ", usuario)
                print("Sheldon: ", computador)
                time.sleep(1)
                print("Seu lagarto foi esmagado pela pedra de Sheldon")
                time.sleep(1)
                print("Sheldon Vence!")
            if computador == "PAPEL":
                print("Você: ", usuario)
                print("Sheldon: ", computador)
                time.sleep(1)
                print("Seu lagarto comeu o papel de Sheldon")
                time.sleep(1)
                print("O papel tinha sonífero")
                time.sleep(1)
                print("Seu lagarto dorme e Sheldon aprisiona ele em um pote")
                time.sleep(1)
                print("Sheldon Vence!")
            if computador == "TESOURA":
                print("Você: ", usuario)
                print("Sheldon: ", computador)
                time.sleep(1)
                print("Seu lagarto foi degolado pela tesoura de Sheldon")
                time.sleep(1)
                print("Sheldon Vence!")
            if computador == "SPOCK":
                print("Você: ", usuario)
                print("Sheldon: ", computador)
                time.sleep(1)
                print("Seu lagarto envenena Spock")
                time.sleep(1)
                print("Spock tomou um antídoto para se recuperar")
                time.sleep(1)
                print("Spock captura o seu lagarto")
                time.sleep(1)
                print("Sheldon Vence!")
        elif usuario == "SPOCK":
            if computador == "PEDRA":
                print("Você: ", usuario)
                print("Sheldon: ", computador)
                time.sleep(1)
                print("Spock vaporiza a pedra de Sheldon")
                time.sleep(1)
                print("Sheldon arremessa outra pedra na cabeça de Spock")
                time.sleep(1)
                print("Sheldon Vence!")
            if computador == "PAPEL":
                print("Você: ", usuario)
                print("Sheldon: ", computador)
                time.sleep(1)
                print("Spock foi refutado pelo papel escrito em Klingon de Sheldon")
                time.sleep(1)
                print("Sheldon Vence!")
            if computador == "TESOURA":
                print("Você: ", usuario)
                print("Sheldon: ", computador)
                time.sleep(1)
                print("Spock amassa a tesoura de Sheldon")
                time.sleep(1)
                print("Agora Spock não pode cortar o papel")
                time.sleep(1)
                print("Sheldon mostra a Clausula 47 do Acordo de Colégas de Quarto")
                time.sleep(1)
                print("Clausula 47: Spock perde")
                time.sleep(1)
                print("Sheldon Vence!")
            if computador == "LAGARTO":
                print("Você: ", usuario)
                print("Sheldon: ", computador)
                time.sleep(1)
                print("Spock foi envenenado pelo lagarto de Sheldon")
                time.sleep(1)
                print("Sheldon Vence!")

    jogar_de_novo = input("Jogar novamente? (sim/não): ").lower()

    if jogar_de_novo != "sim":
        break
print("Até mais!")
