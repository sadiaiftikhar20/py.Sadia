# py.Sadia
hangman project
import random 
hangman= [
    # 6 lives left
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    # 5 lives left: head
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    # 4 lives left: body
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    # 3 lives left: left arm
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    # 2 lives left:
    """
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    # 1 life left: left leg
    """
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,
    # 0 lives left: right leg (game over)
    """
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """
]

 # it has [0], [1], [2], [3], [4], [5], [6] so the chances to make mistakes are 6 so lives will be = 6 

Secret_list=["cute", "tall", "rich", "smart", "pretty"]
choosen_word= random.choice(Secret_list)
print(choosen_word)

blank= ["_"] *len(choosen_word)
print(blank)

lives= 6

while "_" in blank and lives>0:
    user_guess= input("guess the letter: ").lower()

    for i in range (len(choosen_word)):
        if choosen_word[i]== user_guess:
            blank[i]= user_guess
            
    print(blank)

    if user_guess not in choosen_word:
        lives-= 1 
        print(f"{lives} try again") 
        
    print(hangman[6-lives])
    print(blank)

if  lives==0:
    print ("you loose try again")
else: 
    print("correct guess! you win")
