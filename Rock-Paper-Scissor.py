import random as rnd
import time as t


def check(comp_in,user_in):

    '''checks the winner'''

    if comp_in==user_in:
        return 0
    elif (comp_in==0 and user_in==1) and (comp_in==2 and user_in==0) or (comp_in==1 and user_in==2):
        return 1
    else: 
        return -1


regards=["Congo! You got a good luck","Hurray! You won","Keep going, Good"]
wishes=["Bad luck, try again","Don't give up"]
val=[0,1,2]
objs=['Rock','Paper','Scissor']
comp_count=0
user_count=0
    

print("***Welcome! This is ROCK-PAPER-SCISSOR, enter 'start'/'START' for playing***")
inp=input()

if not (inp=='start'or inp=='START'):
    raise ValueError("You have given inavlid input\nPlease restart to play")


elif inp=='start'or inp=='START':
    count=0
    while True:
        
        if count>2:
            print("\n\nIf you want to quit enter '0' (or) enter '1' to continue")
            con=int(input())
            if con==0:
                break
            if con==1:
                count=0
                continue

        print("\n>>>> Wait! Computer is taking it's turn <<<<")
        comp_in=rnd.choice(val)
        t.sleep(4)
        print("\n### Enter '0' for 'Rock','1' for 'Paper' (or) '2' for 'Scissor' ###")
        user_in=int(input())
        
        print("\nYour choice: ",objs[user_in])
        t.sleep(4)
        print("\nComputer's choice: ",objs[comp_in])
        t.sleep(1)
        
        result=check(comp_in,user_in)
        
        if result==1:
            print('\n>> '+rnd.choice(regards)+' <<')
            user_count+=1
        elif result==-1:
            print('\n>> '+rnd.choice(wishes)+' <<')
            comp_count+=1
        elif result==0:
            print("\n:) It's a draw (:")

        count+=1

print("\n\nComputer's score is: ",comp_count)
print("Your score is : ",user_count)
if comp_count>user_count:
    print("\n\n***    Hope you have Greater Luck next time    ***")
elif comp_count==user_count:
    print("\n\n***    You and Computer had an equal Luck    ")
else:
    print(f"\n\n***    Congratulations! You beat the Computer by {comp_count-user_count} points    ***")