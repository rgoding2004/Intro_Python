#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 16:25:17 2021

@author: ryangoding
"""
 
import random
import time

class Colors:
	""" Class used for color printing of letters 
	"""
	blue = '\033[94m'
	endc = '\033[0m'
	bold = '\033[1m'
	red ='\033[31m'
	green='\033[32m'

class UnoCard():
    '''This is a playing card class
    Attributes: 
    Rank
    Suit
    '''
    #Class Attributes
    rank =['0','1','2','3','4','5','6','7','8','9','Reverse', 'Skip','Draw 2']
    color = ['Red','Yellow','Blue','Green']
    
    #Set Instance and its attributes
    def __init__(self, rank, color):
        self.rank = rank
        self.color = color
        if rank not in UnoCard.rank:
            print("Invalid rank!")  
        if color not in UnoCard.color:
            print("Invalid Color!")
    #Special method that returns rank and suit of card
    def __str__(self):
        rep = self.color + ' ' + self.rank
        return rep
    
    def __repr__(self):
        rep = self.color + ' ' + self.rank
        return rep
    
    #Magic Method to compare cards to each other
    def __eq__(self, other):
        if self.rank == other.rank or self.color == other.color:
            return True
        else:
            return False
           
class UnoPlayer:
    
    def __init__(self):
        #Each player has a list of cards for their hand
        self.hand = []
     
    def draw(self, numberofcards, deck):
        self.numberofcards = numberofcards
        self.deck = deck
        self.x = 0
        for self.x in range(0,self.numberofcards):
            self.hand.append(self.deck.cards.pop(0))
    
    def play_draw(self, numberofcards, deck):
        self.numberofcards = numberofcards
        self.deck = deck
        self.play_draw_list = []
        self.x = 0
        for self.x in range(0,self.numberofcards):
            self.play_draw_list.append(self.deck.cards.pop(0))
            return self.play_draw_list
            
    def play_card(self, card):
        self.card = card
        #Checks if valid move, if True removes it from hand
        return self.hand.pop(card-1)
        
        #Special method that returns list of cards with number to play them
    def __str__(self):
        self.handstring = ''
        self.x = 1
        for cards in self.hand:
            self.handstring += str(self.x) + '. ' + str(cards) + '\n'
            self.x +=1
        self.x = 1  
        return self.handstring
    
    def __repr__(self):
        rep = self.name
        return rep
    
class UnoCompPlayer(UnoPlayer):
    
    def __init__(self):
        self.hand = []
        
    
        

class Discard_Pile():
    def __init__(self, numberofcards):
        self.numberofcards = numberofcards
        self.discardpilelist = []
     
    def __str__(self):
        #Returns value of top card in list, this will always be replaced after a turn
     
     return self.discardpilelist[0] 
        

class UnoDeck():
    ''' This is a deck class
    Attributes:
        Cards that hold list of playingcard objects
    
    Methods:
        shuffle_deck() - Randomly changes order of cards in deck
        deal_card(card_count) - Removes first card_count cards from the deck
        and returns them as a list
        '''
    
   
    #Set Deck Instance and its attributes
    def __init__(self, suit=''):
        self.cards = []
        for rank in UnoCard.rank:
            #two of every card in uno, except 0s
            if rank != '0':
                for color in UnoCard.color:
                    self.cards.append(UnoCard(rank,color))
                    self.cards.append(UnoCard(rank,color))
            else:
                for color in UnoCard.color:
                    self.cards.append(UnoCard(rank,color))
        self.shuffle_deck()
    
    
    #shuffle deck function, random.shuffle input list and randomizes the list
    def shuffle_deck(self):
        random.shuffle(self.cards)
        
    def deck_count(self):
        return len(self.cards)
    
    def __str__(self):
        return str(self.cards)
    
    def __repr__(self):
        return str(self.cards)
    
class Menu():
    """Class used for user interface
    Menu start will 
    1) Get number of players
    2) Get name of players and then draw cards
    3) Offer a help menu
    
    """
    def __init__(self):
        
        #Generates deck for play
        self.unodeck = UnoDeck()
        #Discard top of unodeck into discard pile
        self.discardpile = Discard_Pile(0)
        self.discardpile.discardpilelist.append(self.unodeck.cards.pop(0))
        print('Welcome to the Uno Card game.\n')
        #Create player and computer
        self.player = UnoPlayer()
        self.compplayer = UnoCompPlayer()
        #Draw seven cards for player and comp player's hand
        self.player.draw(7, self.unodeck)
        self.compplayer.draw(7, self.unodeck)
        #Starts play_game method to handle all user inputs
        print('Seven Cards has been dealt to you and the computer. \n')
        #Starts play_game method
        self.play_game()
           
    def play_game(self):
        #starts game with turn player
        self.turn = 'player'
        while self.turn != 'end':
            #while game isn't at end, use method self.turns to change turns
            self.turn = self.turns(self.turn)
            print("It is", self.turn, "turn")
            continue
        return
    
    #Method to keep track of player or computer turn       
    def turns(self, turn):
        self.turn = turn
        if self.turn == 'player':
            self.human_turn()
            self.turn = 'computer'
            time.sleep(1)
        else:
            self.computer_turn()
            self.turn = 'player'
            time.sleep(1)
            
        #Calls game_tracker to determine if game is over
        if self.game_tracker() == 0:
            return turn
        elif self.game_tracker() == 1:
            print("Uno Player has lost to the computer")
        else:
            print("Uno Player has Won!")
        return 'end'
    
    def menu_display(self):
        print('Please select from the available menu options:')
        print('C - Displays Deck Count')
        print("D - Draw from Deck (if you can't play any cards in hand)")
        print('M - Displays Help Menu')
        print('H - Displays your current hand')
        print('P - Play a card from your hand')
        print('X - Exit Game')
        self.player_input = input("Player's Choice: ")
        self.player_input = self.player_input.lower()
    
    def human_turn(self):
        print('Shown below is your hand:\n')
        #Displays Player's Current Hand
        print(self.player)
        print("Card in discard pile to play from: ", self.discardpile.discardpilelist[0], '\n')
        while True:
            self.menu_display()
            if self.player_input == 'c':
                print('There are ', self.unodeck.deck_count(), 'cards remaining \n')
            elif self.player_input == 'd':
                self.player.play_draw(1, self.unodeck)
                self.drew_card = self.player.play_draw_list[0]
                if self.drew_card == self.discardpile.discardpilelist[0]:
                    print("You drew and played", self.drew_card )
                    #Replace discard card with played card
                    self.discardpile.discardpilelist[0] = self.drew_card
                    self.turns('computer')
                else:
                    print("You drew a", self.drew_card, "and is not playable\n")
                    self.player.hand.append(self.drew_card)
                    self.turns('computer')
            elif self.player_input == 'm':
              self.help_menu()       
            elif self.player_input == 'h':
                print(self.player)
            elif self.player_input == 'p':
                #redisplay hand and choices
                print("Please select from the following cards in your hand:")
                print("Or select 0 to go back\n")
                print(self.player)
                print("Card in discard pile to play from: ", self.discardpile.discardpilelist[0], '\n')
                self.player_input = input("Card Choice: ")
                if int(self.player_input) in range(1,len(self.player.hand) +1):
                    print("You played", self.player.hand[int(self.player_input)-1], '\n')
                    #Checks if valid turn, if true removes card from hand and places on discard pile
                    if self.valid_turn(int(self.player_input)):
                        #Remove Card from player's hand and then set it to top of discard pile
                        self.discardpile.discardpilelist[0] = self.player.play_card(int(self.player_input)) 
                        self.turns('computer')
                    else:
                        print('That is not a valid move, please try again')
                elif self.player_input == '0':
                    pass
                else:
                    print("You did not select a valid card option")
            elif self.player_input == 'x':
                break
            else:
                print("You have not entered a valid input, please try again\n")
                
    def computer_turn(self):
        print("It is now the computer's turn")
        time.sleep(2)
        for cards in self.compplayer.hand:
            if cards == self.discardpile.discardpilelist[0]:
                print("The computer is playing:", cards)
                self.discardpile.discardpilelist[0] = cards
                self.turns('player')
                break
            else: 
                self.compplayer.play_draw(1, self.unodeck)
                self.drew_card = self.compplayer.play_draw_list[0]
                if self.drew_card == self.discardpile.discardpilelist[0]:
                    print("Computer played", self.drew_card, "It is now your turn\n")
                    #Replace discard card with played card
                    self.discardpile.discardpilelist[0] = self.drew_card
                    self.turns('player')
                else:
                    print("Computer drew a", self.drew_card, "and is not playable. It is now  your turn \n")
                    self.compplayer.hand.append(self.drew_card)
                    self.turns('player')

    #Method to check if card is playable
    def valid_turn(self, card):
        #takes card played as integer and compares to discard pile
        if self.player.hand[card-1] == self.discardpile.discardpilelist[0]:
            return True
        else:
            return False
        
    def game_tracker(self):
        """
        Checks if any player's hand has zero cards, if so ends the game.
        """
        if len(self.player.hand) == 0 or len(self.compplayer.hand) ==0:
            self.game_tracker == 1
        else:
            self.game_tracker == 0
  
    def help_menu(self):
        print('')
        print("Game Rules:")
        print("On a player's turn, they must do one of the following:")
        print("Play one card matching the discard in color, number, or symbol")
        print("Play a Wild card, or a playable Wild Draw Four card")
        print("Or draw the top card from the deck, then play it if possible\n")
        
         
    def __str__(self):
        pass
    
Menu()