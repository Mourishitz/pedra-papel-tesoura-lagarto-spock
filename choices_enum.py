from enum import Enum

class Choices(Enum):
  ROCK = 0
  PAPER = 1
  SCISSORS = 2
  LIZARD = 3
  SPOCK = 4

  @staticmethod
  def getChoice(x: str)-> int:
    return Choices[x].value

  @staticmethod
  def toArrayName()-> list:
    names = []
    for element in list(Choices):
      names.append(element.name)
    
    return names
