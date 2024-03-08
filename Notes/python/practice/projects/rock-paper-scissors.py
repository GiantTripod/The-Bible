import random

choices = ['rock', 'paper', 'scissors']

player1_wins = []
player2_wins = []

def run_game():
    # create two players that will play
    player1 = random.choice(choices) # create random generated selection for computer player
    player2 = random.choice(choices) # create random generated selection fro computer player

    if player1 != player2:
        if (player1  == 'rock') and (player2 != 'paper'):
            player1_wins.append(round_number)
            return player1_wins
        else:
            player2_wins.append(round_number)
            return player2_wins
        if (player1 == 'scissors') and (player2 != 'rock'):
            player1_wins.append(round_number)
            return player1_wins
        else:
            player2_wins.append(round_number)
            return player2_wins
        if (player1 == 'paper') and (player2 != 'scissors'):
            player1_wins.append(round_number)
            return player1_wins
        else:
            player2_wins.append(round_number)
            return player2_wins
    else:
        print('we tied!')


# create a game state that checks for rounds
def choose_rounds():
    # set number of rounds for global access
    global rounds
    # creat input to decide how many rounds there will be
    rounds = input('how many rounds do you want to play?: ')
    if rounds == '':
        return choose_rounds()
    else: 
        rounds = int(rounds)
        if rounds == 0:
            return choose_rounds()
        else: 
            return rounds

choose_rounds()

for round in list(range(rounds)):
    global round_number
    round_number = round
    run_game()


if len(player1_wins) > len(player2_wins):
    print('Player1 wins!')
else:
    print('Player2 wins!')


