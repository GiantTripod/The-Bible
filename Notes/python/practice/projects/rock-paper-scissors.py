import random


# Game choices for players
choices = ['rock', 'paper', 'scissors']

# lists to store what rounds were run
player1_wins = []
player2_wins = []


# main game logic, first generates choices then dertermines winner
def run_game():
    # create two players that will play
    # randomly generate their choice for each round
    player1 = random.choice(choices) 
    player2 = random.choice(choices) 

    if player1 != player2:
        if player1  == 'rock' and player2 != 'paper':
            player1_wins.append(round_number)
            return player1_wins
        elif player1 == 'scissors' and player2 == 'paper':
            player1_wins.append(round_number)
            return player1_wins
        elif (player1 == 'paper') and (player2 == 'rock'):
            player1_wins.append(round_number)
            return player1_wins
        else:
            player2_wins.append(round_number)
            return player2_wins
    else:
        print('you tied!')


# Track how many and what rounds each player has won
def choose_rounds():
    # set number of rounds for global access
    global rounds
    # creat input to decide how many rounds there will be
    rounds = input('how many rounds do you want to play?: ')
    # if there is no entry, re run the function
    if rounds == '':
        return choose_rounds()
    # if there is a valid entry, convert it to int and if 0 re-run the function
    else: 
        rounds = int(rounds)
        if rounds == 0:
            return choose_rounds()
        # if not 0 return rounds and store for use
        else: 
            return rounds

choose_rounds()

# for each round run the main game logic and store the round number
for round in list(range(rounds)):
    global round_number
    round_number = round
    run_game()


print(player1_wins)
print(player2_wins)


# decide who has won by comparing total rounds won in each list
if len(player1_wins) > len(player2_wins):
    print('Player1 wins!')
elif len(player2_wins) > len(player1_wins):
    print('Player2 wins!')
else:
    print('you tied the big game!')


