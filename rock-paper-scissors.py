import random
import time

choices = ['Rock', 'Paper', 'Scissors']
playing = True
player = ''

def find_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        print("Game tied\n")
    else:
        if player_choice == 'Rock':
            if computer_choice == 'Paper':
                print("You lose\n")
            else:
                print("You win\n")
        elif player_choice == 'Paper':
            if computer_choice == 'Scissors':
                print("You lose\n")
            else:
                print("You win\n")
        else:
            if computer_choice == 'Rock':
                print("You lose\n")
            else:
                print("You win\n")


while playing:
    print("\n-------------------------------")
    print("Welcome to rock paper scissors!")
    print("-------------------------------\n")

    computer = choices[random.randint(0,2)]

    bad_input = True
    while bad_input:
        player_input = input("Your Choices:\n1)Rock\n2)Paper\n3)Scissors\n\nWhich would you like to play: ")
        if player_input == '1' or player_input == '2' or player_input == '3':
            player = choices[int(player_input) - 1]
            bad_input = False
        else:
            print("\nInvalid input, try again!\n")
    
    print("\nROCK")
    time.sleep(1)
    print("\nPAPER")
    time.sleep(1)
    print("\nSCISSORS\n")
    time.sleep(1)

    print("Player shows: " + player)
    print("Computer shows: " + computer + "\n")
    find_winner(player, computer)

    while True:
        play_again_input = input("Would you like to play again (Y/N): ")
        if play_again_input.lower() == 'y':
            playing = True
            break
        elif play_again_input.lower() == 'n':
            playing = False
            break
        else:
            print("\nInvalid input, try again!\n")

