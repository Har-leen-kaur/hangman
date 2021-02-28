import random
import art
import words  


print(art.logo)
print()
print()


# word_list = ["aardvark", "baboon", "camel"]
stages = art.stages
word_list = words.word_list
chosen_word = random.choice(word_list)
#print(f"The word is {chosen_word}")


lives = 6 


display = []
for letter in chosen_word:
  display.append('_')
print(display) 


isEmpty = False 
gameOver = False
  
while not gameOver: 
  print()
  guess = input("Guess a letter\n").lower()
  for i in range(len(display)):
    if guess == chosen_word[i]:
      display[i] = guess
      
  if guess not in chosen_word:
    if lives == 0: 
      print(stages[0])
      print("Game Over")
      print(f"The word was {chosen_word}")
      gameOver = True
      break 
    print(stages[lives])
    lives -= 1 

  print(display) 

  if not '_' in display:
    gameOver = True
    print('You Win')

    


