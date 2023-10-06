import random
from time import sleep
import graph
from choices_enum import Choices
from translation import portugues, english

def play(first_time: bool):

  if(first_time):
    print("Regras: \n Pedra, papel, tesoura, lagarto, Spock. É muito simples.\n "
          "Olhe – tesoura corta papel, papel cobre pedra, pedra esmaga lagarto,\n "
          "lagarto envenena Spock, Spock esmaga tesoura, tesoura decapita lagarto,\n "
          "lagarto come papel, papel refuta Spock, Spock vaporiza pedra \n"
          " e como sempre, pedra quebra tesoura.\n")

  print("As opções são: \n")

  options: list = Choices.toArrayName()
  for option in options:
    print(portugues[option].capitalize())

  print("\n")

  user = input("Escolha uma opção: ").upper()
  user = english[user] # Translates user input to english
  sheldon = random.choice(options)

  print(f"Você selecionou: {user}")
  print(f"Sheldon selecionou: {sheldon}")

  result = graph.getRelation(Choices.getChoice(user), Choices.getChoice(sheldon))

  # TODO: Implement custom wins for Sheldon
  match result:
    case 0:
      print("Teóricamente é um empate, e de acordo com o 'Acordo dos Colegas de Quarto' Sheldon decide todos os empates de um contra um.")
      print("Portanto, Sheldon Vence!")
    case 1:
      print("Você venceu!")
      sleep(1)
      print("Ou melhor, quase venceu...")
      sleep("Sheldon hackeou este jogo e alterou o código fonte para ganhar.")
      print("Sheldon vence!")
    case -1:
      print("Sheldon vence!")


  wantsToPlayAgain = str(input("Quer jogar novamente? [S/n] "))

  match wantsToPlayAgain[0].upper():
    case "S":
      play(False)
    
    case "N":
      return
    
    case _:
      play(False)

play(True)
