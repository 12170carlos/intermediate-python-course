import random
def main():
  dice_rolls = int ( input ( '¿Cuántos dados te gustaría tirar? ' ))
  dice_size  =  int ( input ( '¿Cuántos lados tienen los dados? ' ))

  dice_sum = 0
  for i in range(0,dice_rolls):
    roll = random.randint(1,dice_size)
    dice_sum +=roll
    if roll == 1:
      print(f'!Has lanzado un {roll} ! Critical Fail')
    elif  roll  ==  dice_size :
     print ( f'Has obtenido una { roll} ! ¡Éxito crítico!' )
    else:
      print(f'!Has lanzado un {roll} ')
  print(f'Has obtenido un total de {dice_sum}')
    

if __name__== "__main__":
  main()