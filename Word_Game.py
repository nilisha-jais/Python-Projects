import random

def ask_again():
    global play
    play=input("Do you want to play again(yes/no):")
    if play=="yes":
        global chances,index,word,guess_index,guesses
        chances=5
        index=random.randint(0,len(words))
        word=words[index]
        guess_index=random.sample(range(0,len(word)),3)
        guesses=""
        for i in guess_index:
            guesses+=word[i]


name=input("Enter your name:")
print(f"Hello {name}!! Welcome to the fruit guessing game")
words=["apple","grapes","pomegranate","guava","banana","pineapple","orange","pear","watermelon","strawberry"]
index=random.randint(0,len(words))
word=words[index]
guess_index=random.sample(range(0,len(word)),3)
guesses=""
for i in guess_index:
    guesses+=word[i]
chances=5
play="yes"
while play=="yes":
  while chances>0:
    won=True
    for ch in word:
        if ch in guesses:
          print(ch,end=" ")
        else:
            print("_",end=" ")
            won=False
    if won:
        print("\nYou won")
        print(f"Your score is {chances}")
        ask_again()
        break
    guess=input('\nEnter your guess:')
    guesses+=guess
    if guess not in word:
        chances-=1
        print(f"Wrong answer!!Try again\nYou have {chances} chances left")
        if chances==0:
            print("You loose")
            ask_again()
            break