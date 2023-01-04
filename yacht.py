# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    set_list = list(set(dice))
    cur_score = 0
    
    if (category == ONES):
        cur_score = dice.count(1) * 1
    elif (category == TWOS):
        cur_score = dice. count(2) * 2
    elif (category == THREES):
        cur_score = dice. count(3) * 3
    elif (category == FOURS):
        cur_score = dice. count(4) * 4
    elif (category == FIVES):
        cur_score = dice. count(5) * 5
    elif (category == SIXES):
        cur_score = dice. count(6) * 6
    elif (category == CHOICE):
        cur_score = sum(dice)
    elif (category == YACHT):
        if len(set_list) == 1:
            cur_score = 50
    elif (category == LITTLE_STRAIGHT):
        if len(set_list) == 5:
            if sum(set_list) == 15:
                cur_score = 30
    elif (category == BIG_STRAIGHT):
        if len(set_list) == 5:
            if sum(set_list) == 20:
                cur_score = 30
    elif (category == FULL_HOUSE):
        if len(set_list) == 2:
            if (dice.count(set_list[0]) == 2) or (dice.count(set_list[0]) == 3) :
                cur_score = sum(dice)
    elif (category == FOUR_OF_A_KIND):
        if len(set_list) == 1:
            cur_score = 4 * selt_list[0]
        elif len(set_list) == 2:
            if dice.count(set_list[0]) == 4:
                cur_score = 4 * set_list[0]
            elif dice.count(set_list[1]) == 4:
                cur_score = 4 * set_list[1]
    return cur_score
            
         
      
        
