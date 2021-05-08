import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

trophy = '''
                  {}
                 /__\
               /|    |\
              (_|    |_)
                 \  /
                  )(
                _|__|_
              _|______|_
             |__________|
'''
duck = '''
   __
__(o )
===  |
   | \___/|
   \ \=== |
    \_\==/
      ||
     ===  

'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]


def rock_paper_scis_assoc():
    user_win = 0
    comp_win = 0
    i = int(input("How many round do you prefer to play? Enter odd number: "))
    if i % 2 != 0:
        for x in range(i):
            user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))
            if user == 0 or user == 1 or user == 2:
                print(game[user])
                comp = random.randint(0, 2)
                print(f"Computer Choice: {comp}")
                if comp == 0 or comp == 1 or comp == 2:
                    print(game[comp])
                if user == 0 and comp == 2:
                    print("You Win!")
                    user_win += 1
                elif comp == 0 and user == 2:
                    print("You Lose")
                    comp_win += 1
                elif comp > user:
                    print("You Lose")
                    comp_win += 1
                elif user > comp:
                    print("You win!")
                    user_win += 1
                else:
                    print("It's a draw")
                    comp_win += 1
                    user_win += 1

            else:
                print("Invalid Choice. You Lose")
            print(f"User: {user_win} ")
            print(f"Comp: {comp_win} ")
        if user_win > comp_win:
            print("You Won the Series!")
            print(trophy)
        elif comp_win > user_win:
            print("You Lose to Computer! Better try next time!")
            print(duck)
        else:
            print("It's a Draw Series")
        valid = input("Would you like to re-match ?Enter Y for Yes or N for No: ")
        if valid == "Y" or valid == "y":
            rock_paper_scis_assoc()
        elif valid == "N" or valid == "n":
            print("----------Thank You ---------- ")
        else:
            print("Enter valid character:")
    else:
        print("Enter a valid Odd number")


rock_paper_scis_assoc()








