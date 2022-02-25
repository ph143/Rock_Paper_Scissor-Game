import random
import time
def game(comp, a):
    if comp == 'S':
        if a == 'P':
            print('You loss as computer choosen',comp,'\nso better luck next time') 
            #return False 
        elif a == 'R':
            print('You Won as computer choosen',comp)
            #return True
        else:
            print('oops!!!...The match is Draw as you and computer choosen the same i.e Scissor')
            #return None
    elif comp == 'R':
        if a == 'R':
            print('oops!!!...The match is Draw as you and computer choosen the same i.e Rock')
            #return None 
        elif a == 'S':
            print('You loss as computer choosen',comp,'\nso better luck next time') 
            #return False
        else:
            print('You Won as computer choosen',comp)
            #return True 
    elif comp == 'P': 
        if a == 'R':
             print('You loss as computer choosen',comp,'\nso better luck next time') 
            #return False
        elif a == 'S':
            print('You Won as computer choosen',comp)
            #return True 
        else: 
            print('oops!!!...The match is Draw as you and computer choosen the same i.e Paper')
            #return None
    else:
        exit()
           
while True:
    y = ['R','P','S']
    randno = random.randint(1,3)
    if randno == 1:
        comp = 'R'
    elif randno == 2:
        comp = 'P'
    else:
        comp = 'S' 
    print("Now Computer's Turn........")
    time.sleep(1)
    print("Yeah computer has choosen it's option")
    time.sleep(0.3)
    print('Now your turn')
    time.sleep(0.3)
    a=input("choose one \nS-Scissor \nR-Rock \nP-Paper\n")
    if a not in y:
        print('Choose betweeen S, R and P')
    else:
        game(comp, a)
    x=input('\nDo you wanna play again (Y/N)?')
    if x == 'y':
        print('Great Choice......\n___________________________\n')
        pass
    else:
        exit()


    
