# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass
    print("\n\n**************************\n")
    

def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

#####################################

def deal_cards(deck):
     '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''
     dealer=[]
     human=[]
     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE
     for i in range(0,len(deck)):
         if i%2==0:
             dealer.append(deck[i])
         if i%2!=0:
             human.append(deck[i])
     return (dealer, human)
 


def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''
    no_pairs=[]

    l.sort()#raw sorted list
    #future list of duplicates
    l.append('')
    i=0
    while i<(len(l)-1):
        if l[i].strip('♣'+'♢'+'♡'+'♠') != l[i+1].strip('♣'+'♢'+'♡'+'♠'):
            no_pairs.append(l[i])
            i+=1
        else:
            i+=2
    random.shuffle(no_pairs)
    return no_pairs


def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''
    print( ' '.join(deck))
    
def get_valid_input(l):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''
     y=len(l)
     while y>0:
         try:
             n=int(input('I have '+str(y)+' cards. If 1 stands for my first card and\n'+str(y)+' for my last card, which of my cards would you like?\nGive me an integer between 1 and '+str(y)+': '))
         except ValueError:
             print('\nThat is invalid! Please enter a number that is between 1 and '+str(y))
             continue
         if n>y or n<1:
             print('\nUnfortunatly, that is not a card I can choose.')
         else:
             break
     return (n,y)

     
     



def play_game():
     '''()->None
     This function plays the game'''
    
     deck=make_deck()
     shuffle_deck(deck)
     tmp=deal_cards(deck)

     dealer=tmp[0]
     human=tmp[1]

     print("Hello. My name is Robot and I am the dealer.")
     print("Welcome to my card game!")
     print("Your current deck of cards is:")
     print_deck(human)
     print("Do not worry. I cannot see the order of your cards")

     print("Now discard all the pairs from your deck. I will do the same.")
     wait_for_player()
     
     dealer=remove_pairs(dealer)
     human=remove_pairs(human)
     
     # COMPLETE THE play_game function HERE
     # YOUR CODE GOES HERE
     while (len(dealer)>0 or len(human)>0):
                 if len(dealer)==0:
                     break
                 if len(human)==0:
                     break
                 print('Your turn\n\nYour current deck of cards is:\n\n')
                 print_deck(human)
                 print('\n')
                 xx=get_valid_input(dealer)
                 y=(list(xx))[1]
                 n=(list(xx))[0]
                 ll=dealer[n-1]
                 iputlist=list(str(n))
                 lol=int(iputlist[len(iputlist)-1])
                 if lol==1:
                     end='st'
                 elif lol==2:
                     end='nd'
                 elif lol==3:
                     end='rd'
                 else:
                     end='th'
                 print('You asked for my '+str(n)+end+' card.\nHere it is. It is '+str(ll)+'\n\n')
                 dealer.remove(ll)
                 human.append(ll)
                 ll1=human[len(human)-1]
                 if len(dealer)==0:
                     break
                 if len(human)==0:
                     break
                 print('With '+str(ll1)+' added, your current deck of card is:\n\n')
                 print_deck(human)
                 print('\nAnd after discarding pairs and shuffling, your deck is:\n')
                 remove_pairs(human)
                 no_pairs=remove_pairs(human)
                 human=no_pairs
                 shuffle_deck(human)
                 print_deck(human)
                 wait_for_player()
                 print('My turn.\n\n')
                 rndc=random.randrange(0,len(human))
                 if rndc==0:
                     rndc=1
                 ll2=human[rndc-1]
                 iputlist2=list(str(rndc))
                 lol2=int(iputlist2[len(iputlist2)-1])
                 if lol2==1:
                     end2='st'
                 elif lol2==2:
                     end2='nd'
                 elif lol2==3:
                     end2='rd'
                 else:
                     end2='th'
                 print('I took your '+str(rndc)+end2+' card.') 
                 human.remove(ll2)
                 dealer.append(ll2)
                 remove_pairs(dealer)
                 no_pairs=remove_pairs(dealer)
                 dealer=no_pairs
                 shuffle_deck(dealer)
                 wait_for_player()
                 if len(dealer)==0:
                     break
                 if len(human)==0:
                     break
     if len(dealer)==0:
         print('Ups. I do not have any more cards\nYou lost! I, Robot, win')
     if len(human)==0:
         print('Ups. You do not have any more cards\nCongratulations! You, Human, win')

# main
play_game()
