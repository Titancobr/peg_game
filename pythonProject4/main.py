import random


def roll():
    minvalue=1
    maxvalue=6
    roll = random.randint(minvalue,maxvalue)
    return roll


while True:
    player = input("enter the no of players(2-4): ")
    if player.isdigit():
        player=int(player)
        if 2<=player<=4:
            break
        else:
            print("should be between (2-4)")
    else:
        print("invalid enter no")


max_score= 50
player_score = [0 for _ in range(player)]

while max(player_score) < max_score:

    for pd in range(player):
        print('\nplayer number',pd +1,'turn started\n')
        print('your total score is ',player_score[pd])

        c_score = 0
        while True:

          should_roll= input("would you like to roll(y) ?: ")
          if should_roll.lower()!="y":
             break

          else:
             value= roll()

          if value==1:
             print("your no is 1! turn done")
             c_score = 0

          else:
             c_score += value
             print("you rolled :",value)
             print("your score is ",c_score)
        player_score[pd] += c_score
        print("your total score is:",player_score[pd])


max_score = max(player_score)
windf = player_score.index(max_score)
print('player number',windf + 1,'is the winner ',max_score)
