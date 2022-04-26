import random


def comp_choice():
    choice = random.randint(1, 3)
    if choice == 1:
        comp_result = 'Boulder'
    elif choice == 2:
        comp_result = 'Parchment'
    else:
        comp_result = 'Shears'
    return comp_result


def logic(comp, player):
    # 4 means tie, 5 means player wins, 6 means computer wins
    if comp == player:
        return 4
    elif comp == 'boulder' and player == 'parchment':
        return 5
    elif comp == 'boulder' and player == 'shears':
        return 6
    elif comp == 'parchment' and player == 'boulder':
        return 6
    elif comp == 'parchment' and player == 'shears':
        return 5
    elif comp == 'shears' and player == 'boulder':
        return 5
    elif comp == 'shears' and player == 'parchment':
        return 6


def game(player_choice, computer_choice):
    final = logic(computer_choice, player_choice)
    return final
