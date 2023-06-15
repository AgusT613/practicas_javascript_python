from enum import Enum

class Player(Enum):
    P1 = 'PLAYER 1'
    P2 = 'PLAYER 2'
    
score_table, tie = ["Love", 15, 30, 40], "Deuce"
sequence = [Player.P1, Player.P2, Player.P1, Player.P2, Player.P1, Player.P2, Player.P1, Player.P1]

def evaluate_sequence(sequence: list):
    # Initial Score and State of Tie
    score_player_1, score_player_2 = 0, 0
    state_of_tie = False
    # Each Player Score
    for player in sequence:
        # In case of having 3 points each player, then it´s a tie
        if score_player_1 == 3 and score_player_2 == 3 and state_of_tie == False:
            print(f'It´s a tie! {tie}!')
            state_of_tie = True
        # Scores player 1. If it has 3 points one after the other, it ends there
        elif player.value == 'PLAYER 1' and not state_of_tie:
            if score_player_1 == 3: 
                print('Player 1 Wins')
                break
            score_player_1 += 1
            print(f'{score_table[score_player_1]} ---- {score_table[score_player_2]}')
        # Same logic in this section
        elif player.value == 'PLAYER 2' and not state_of_tie:
            if (score_player_2 == 3):
                print('Player 2 Wins')
                break
            score_player_2 += 1
            print(f'{score_table[score_player_1]} ---- {score_table[score_player_2]}')
        # Final winner here if there was a tie
        else:
            print( 'Player 1 Wins' if player.value == 'PLAYER 1' else 'Player 2 Wins' )

evaluate_sequence(sequence)