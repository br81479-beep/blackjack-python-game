


































































































import random
import time



#officially the largest game I have ever made
#hand crafted by jaybird
#im so kewl
#over 500 lines of code
#:O



#global varibles

first = 0
second = 0
third = 0
fourth = 0
fifth = 0
dfirst = 0
dsecond = 0
dthird = 0
dfirstint = 0
dsecondint = 0
dthirdint = 0
firstint = 0
secondint = 0
thirdint = 0
fourthint = 0
fifthint = 0
chips = 500
bet = 0
dscore = 0
score = 0
wins = 0
loss = 0
red = "\033[31m"
black = "\033[0m"


def restart():
    global first,second, third,fourth,fifth,firstint,secondint,thirdint,fourthint,fifthint,dfirst,dsecond,dthird,dfirstint,dsecondint,dthirdint,cards,wins,loss
    
    print("\033[H\033[J", end="")
    
    
    #player cards
    first = random.randrange(2,14)
    firstint = first
    second = random.randrange(2,14)
    secondint = second
    third = random.randrange(2,14)
    thirdint = third
    fourth = random.randrange(2,14)
    fourthint = fourth
    fifth = random.randrange(2,14)
    fifthint = fifth

    #dealer cards
    dfirst = random.randrange(2,14)
    dfirstint = dfirst
    dsecond = random.randrange(2,14)
    dsecondint = dsecond
    dthird = random.randrange(2,14)
    dthirdint = dthird
    
    
    cards()

def cards():
    global firstint, first, secondint, second, thirdint, third, fourthint, fourth, fifthint, fifth, game, dfirst, dsecond, dthird, dfirstint, dsecondint, dthirdint
    if first == 11 or 12 or 13 or 14:
        if first == 11:
            first = "jack"
            firstint = 10
    
    
        elif first == 12:
            first = "queen"
            firstint = 10
    
        
        elif first == 13:
            first = "king"
            firstint = 10
    
        
        elif first == 14:
            first = "ace"
            firstint = 11


    if second == 11 or 12 or 13 or 14:

        if second == 11:
            second = "jack"
            secondint = 10

        
        elif second == 12:
            second = "queen"
            secondint = 10

        
        elif second == 13:
            second = "king"
            secondint = 10

        
        elif second == 14:
            second = "ace"
            secondint = 11

    
    if third == 11 or 12 or 13 or 14:

        if third == 11:
            third = "jack"
            thirdint = 10

        
        elif third == 12:
            third = "queen"
            thirdint = 10

        
        elif third == 13:
            third = "king"
            thirdint = 10

        
        elif third == 14:
            third = "ace"
            thirdint = 11

        
    if fourth == 11 or 12 or 13 or 14:

        if fourth == 11:
            fourth = "jack"
            fourthint = 10

        
        elif fourth == 12:
            fourth = "queen"
            fourthint = 10

        
        elif fourth == 13:
            fourth = "king"
            fourthint = 10

        
        elif fourth == 14:
            fourth = "ace"
            fourthint = 11

            
            
    if fifth == 11 or 12 or 13 or 14:

        if fifth == 11:
            fifth = "jack"
            fifthint = 10
        

        elif fifth == 12:
            fifth = "queen"
            fifthint = 10

        
        elif fifth == 13:
            fifth = "king"
            fifthint = 10

        
        elif fifth == 14:
            fifth = "ace"
            fifthint = 11

            
    if dfirst == 11 or 12 or 13 or 14:

        if dfirst == 11:
            dfirst = "jack"
            dfirstint = 10

        
        elif dfirst == 12:
            dfirst = "queen"
            dfirstint = 10

        
        elif dfirst == 13:
            dfirst = "king"
            dfirstint = 10

        
        elif dfirst == 14:
            dfirst = "ace"
            dfirstint = 11


    if dsecond == 11 or 12 or 13 or 14:

        if dsecond == 11:
            dsecond = "jack"
            dsecondint = 10

        
        elif dsecond == 12:
            dsecond = "queen"
            dsecondint = 10

        
        elif dsecond == 13:
            dsecond = "king"
            dsecondint = 10

        
        elif dsecond == 14:
            dsecond = "ace"
            dsecondint = 11

    
    if dthird == 11 or 12 or 13 or 14:

        if dthird == 11:
            dthird = "jack"
            dthirdint = 10

        
        elif dthird == 12:
            dthird = "queen"
            dthirdint = 10

        
        elif dthird == 13:
            dthird = "king"
            dthirdint = 10

        
        elif dthird == 14:
            dthird = "ace"
            dthirdint = 11


    time.sleep(0.5)
    game()
    

def game():
    global firstint, first, secondint, second, thirdint, third, fourthint, fourth, fifthint, fifth, cards, chips, bet, dealer, score, dscore, win, fin, wins, loss, load, red, black
    bet = 0
    score = firstint + secondint
    print(f"{red}you have {chips} chips{black}")
    print(f"you have {wins} wins")
    print(f"{red}you have {loss} losses{black}")
    
    if chips == 0:
        print("would you like to restart")
        print(f"{red}it will reset your wins and losses{black}")
        print("but you will get 500 chips")
        print(f"{red}press enter to reset all data{black}")
        re = input("")
        if re == "":
            wins = 0
            loss = 0
            chips = 500
            restart()
    #bet input
    bet = int(input("how much would you like to gamble? "))
    
    print(f"{red}you are betting {bet} chips{black}")
    g = 1
    while bet > chips:
        bet = int(input("too high a bet, please re-enter: "))
    if chips >= bet:
        g = 2
    
    if g == 2:
        
        chips = chips - bet
        bet = bet * 2
    
    
        #first set of cards
        print(f"your first card is a {first}")
        print(f"{red}your second card is a {second}{black}")
    
        if score > 21:
            secondint = 1
        
        if score == 21:
            load()
        print(f"your score is {score}")
        print(f"{red}1 for hit, 2 for stand{black}")
        desc1 = int(input())
    
        #start of third
        if desc1 == 2:
            time.sleep(0.5)
            load()
    
        if desc1 == 1:
            score = score + thirdint
            time.sleep(0.5)
            print(f"your third card is {third}")
        
            if score > 21 and third == "ace":
                thirdint == 1
        
            print(f"{red}your score is {score}{black}")
            print(f"you have a {first}, a {second}, a {third}")

            if score > 21:
                #loss
                load()
            
            elif score < 21:

                print(f"{red}type 1 for hit, type 2 for stand{black}")
                desc2 = int(input())
            
                if desc2 == 2:
                    load()
                
                elif desc2 == 1:
                    score = score + fourthint
                    time.sleep(0.5)
                    print(f"{red}your third card is {fourth}{black}")
        
                if score > 21 and fourth == "ace":
                    thirdint == 1
        
                print(f"your score is {score}")
                print(f"{red}you have a {first}, a {second}, a {third}, and a {fourth}{black}")

                if score > 21:
                    #loss
                    load()
            
                elif score < 21:

                    print("type 1 for hit, type 2 for stand")
                    desc3 = int(input())
                
                    if desc3 == 1:
                        score = score + fifthint

                        if score > 21 and fifth == "ace":
                            fifthint == 1
                        print(f"{red}your score is {score}{black}")
                        print(f"your fifth card is {fifth}")
                        print(f"{red}press 1 to stand{black}")
                        int(input(""))
                        dealer()
                    elif desc3 == 2:
                        restart()
                    else:
                        load()
                #desc2 else
                else:
                    load()
            elif score == 21:
         
                load()
    
        #else for desc 1
        else:
            load()
        
        
        
        
        
b = 1
a = -1
def load():
    while True:
        global b, a, dealer
        goodman = random.getrandbits(3)
        print("\033[H\033[J", end="")
        if b == 1:
            print("loading.")
            time.sleep(1)
            print("\033[H\033[J", end="")
            b = 2
            a = a + 1
        elif b == 2:
            print(f"{red}loading..{black}")
            time.sleep(1)
            print("\033[H\033[J", end="")
            b = 3
            a = a + 1
        elif b == 3:
            print("loading...")
            time.sleep(1)
            print("\033[H\033[J", end="")
            b = 1
            a = a + 1
            
        if a == goodman:
            print("\033[H\033[J", end="")
            dealer()
            break
        elif a > goodman:
            print("\033[H\033[J", end="")
            dealer()
            break
def dealer():
    global dfirst, dsecond, dthird, dfirstint, dsecondint, dthirdint, dscore, score, game
    dscore = dfirstint + dsecondint
    if dscore <= 16:
        dscore = dscore + dthirdint
        time.sleep(0.5)
        fin()
    
    else:
        time.sleep(0.5)
        fin()
        
def fin():
    global score, dscore, dealer, restart, chips, bet, loss, wins
    
    
    
    print(f"{red}your final score is {score}{black}")
    
    if score > 21:
        print(f"the dealer got {dscore}")
        print(f"{red}you lost{black}")
        bet = 0
        loss = loss + 1
        print("to play again type 1, to stop press 2 ")
        ggez = input()
        if ggez == 1:
            restart()
            
        elif ggez == 2:
            pass
        
        else:
            restart()
            

    elif score >= dscore and score < 21 or dscore > 21:
        print(f"{red}the dealer got {dscore}{black}")
        print("YOU WON!!!")
        chips = chips + bet
        bet = 0
        wins = wins + 1
        print(f"{red}to play again type 1, to stop press 2{black}")
        ggez = input()
        if ggez == 1:
            time.sleep(0.5)
            restart()
            
        elif ggez == 2:
            pass
        else:
            restart()
    elif score == 21:
        print(f"{red}BLACKJACK{black}")
        bet = bet * 2 
        score = score + bet 
        wins = wins + 1
        time.sleep(0.5)
        print("to play again type 1, to stop type 2")
        ggez = input()
        if ggez == 1:
            restart()
        if ggez == 2:
            pass
        else:
            restart()
    
    elif score < dscore:
        print(f"{red}the dealer got {dscore}{black}")
        print("you lost")
        bet = 0
        loss = loss + 1
        print(f"{red}to play again type 1, to stop press 2 {black}")
        ggez = input()
        if ggez == 1:
            restart()
            
        elif ggez == 2:
            pass
        
        else:
            restart()
    else:
        
        time.sleep(5)
        restart()


restart()





