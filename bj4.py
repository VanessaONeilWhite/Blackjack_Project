#a deck with appropriate values (list?)
#card class that generates a deck of cards
#UI that generates the game

import random
import os

def clear_screen():
    os.system('cls' if os.name == "nt" else 'clear')



class Cards():
    global suits, values
    suits= ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values= ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    for points in range(len(values)):
        for suit in range(len(suits)):
            print(values[points],suits[suit])

    def __init__(self):
        pass

class Deck(Cards):
    def __init__(self):
        Cards.__init__(self)
        self.mydeck=[]
        for suit in suits:
            for points in values:
                self.mydeck.append(points+ "of" + suit)
        random.shuffle(Deck.mydeck)


class BlackJack(self):
    def __init__(self):
        self.gamedeck=Deck.mydeck
        self.player_hand=[]
        self.dealer_hidden=[]
        self.dealer_hand=[]
        self.dealer_points=[]
        self.player_points=[]
        self.dealer_bj = False
        self.dealer_bj = False
    def deal(self):
        self.dealer_hidden.append(self.gamedeck.pop())
        self.dealer_hand.append(self.gamedeck.pop())
        self.player_hand.append(self.gamedeck.pop())
        self.player_hand.append(self.gamedeck.pop())
        self.dealer_total()
        if self.dealer_total ==21:
            self.dealer_bj = True
            self.end_game()
        self.player_score()
        if self.player_total == 21:
            self.player_bj = True
            self.end_game()
        self.dealer_points.clear()
        self.player_points.clear()

#This is a really inefficient way to do this but I couldn't figure out how to set the cards as a dictionary and then shuffle the keys/values.
#there has to be a way to do that
    def player_score(self):
        for card in self.player_hand:
            x=1
            if card == "2":
                self.player_points.append(x +1)
            elif card == "3":
                self.player_points.append(x+2)
            elif card =="4":
                self.player_points.append(x+3)
            elif card =="5":
                self.player_points.append(x+4)
            elif card =="6":
                self.player_points.append(x+5)
            elif card =="7":
                self.player_points.append(x+6)
            elif card =="8":
                self.player_points.append(x+7)
            elif card =="9":
                self.player_points.append(x+8)
            elif card =="10":
                self.player_points.append(x+9)
            elif card =="Jack":
                self.player_points.append(x+10)
            elif card =="Queen":
                self.player_points.append(x+10)
            elif card =="King":
                self.player_points.append(x+10)
            elif card =="Ace":
                self.player_points.append(x+11)
        self.player_total = sum(self.player_points)
        
    def player_score(self):
        for card in self.dealer_hand:
            x=1
            if card == "2":
                self.dealer_points.append(x +1)
            elif card == "3":
                self.dealer_points.append(x+2)
            elif card =="4":
                self.dealer_points.append(x+3)
            elif card =="5":
                self.dealer_points.append(x+4)
            elif card =="6":
                self.dealer_points.append(x+5)
            elif card =="7":
                self.dealer_points.append(x+6)
            elif card =="8":
                self.dealer_points.append(x+7)
            elif card =="9":
                self.dealer_points.append(x+8)
            elif card =="10":
                self.dealer_points.append(x+9)
            elif card =="Jack":
                self.dealer_points.append(x+10)
            elif card =="Queen":
                self.dealer_points.append(x+10)
            elif card =="King":
                self.dealer_points.append(x+10)
            elif card =="Ace":
                self.dealer_points.append(x+11)
        
        for card in self.dealer_hidden:
            x=1
            if card == "2":
                self.dealer_points.append(x +1)
            elif card == "3":
                self.dealer_points.append(x+2)
            elif card =="4":
                self.dealer_points.append(x+3)
            elif card =="5":
                self.dealer_points.append(x+4)
            elif card =="6":
                self.dealer_points.append(x+5)
            elif card =="7":
                self.dealer_points.append(x+6)
            elif card =="8":
                self.dealer_points.append(x+7)
            elif card =="9":
                self.dealer_points.append(x+8)
            elif card =="10":
                self.dealer_points.append(x+9)
            elif card =="Jack":
                self.dealer_points.append(x+10)
            elif card =="Queen":
                self.dealer_points.append(x+10)
            elif card =="King":
                self.dealer_points.append(x+10)
            elif card =="Ace":
                self.dealer_points.append(x+11)
        self.dealer_total = sum(self.dealer_points)

    def hit(self):
        self.player_hand.append(self.gamedeck.pop())
        self.player_points.clear()
        self.player_score()
        clear_screen()
        self.lay_cards()


    def dealer_turn(self):
        while self.dealer_total < 17 and self.dealer_total <= self.player_total:
            self.dealer_hand.append(self.gamedeck.pop())
            clear_screen()
            print(self.dealer_hand)
            self.dealer_points.clear()
            self.dealer_total()
            if self.dealer_total > self.player_total and self.dealer_total <=21:
                self.end_game()
                break
            elif self.dealer_total >21:
                self.end_game()
                break 

    def lay_cards(self):
        print(f"Dealer's Hand: |?|, {self.dealer_hand}")
        print(f"Your hand: {self.player_hand}")
        print(self.dealer_total)
        print(self.player_total)

    def end_game(self):
        if self.dealer_bj == True:
            return 7
        elif self.dealer_bj ==True:
            return 8
        elif self.player_total >21: 
            return 1
        elif self.dealer_total>21:
            return 2 
        elif self.player_total > self.dealer_total:
            return 3 
        elif self.dealer_total >= self.player_total:
            return 4
        else:
            return 0
    
    def player_check(self):
        if self.player_total > 21:
            self.end_game()
        return True 


class UI():
    class UI():
        game = BlackJack()
        @classmethod
        def play_game(cls):
            print(
                """
                ============================================
                Welcome to BlackJack, want to test your luck?
                =============================================
                """
            )
            cls.game.player_hand.clear()
            cls.game.dealer_hand.clear()
            cls.game.dealer_hidden.clear()
            while True:

                start_game = input("Would you like to start a new game? Type 'N' for no or 'Enter' to start: ")
                if start_game.lower().strip() == 'n':
                    print("See you next time!")
                    break 
                cls.game.deal()
                clear_screen()
                cls.game.dealer_total()
                cls.game.player_score()
                cls.game.lay_cards()
                while True:
                    response = input("Would you like to hit? Enter 'Y' or 'N' ")
                    if response.lower().strip() == "y":
                        cls.game.hit()
                        cls.game.player_check()
                        if cls.game.player_check:
                            break 
                    elif response.lower().strip() == "n":
                        cls.game.dealer_turn()
                        break
                    else: 
                        print("Please use a valid entry.")
            
                if cls.game.end_game()== 7:
                    clear_screen()
                    print(f'{cls.game.dealer_hidden}{cls.game.dealer_hand}')
                    print(cls.game.player_hand)
                    print("Dealer has BlackJack")
                    cls.play_game()

                elif cls.game.end_game()== 8:
                    clear_screen()
                    print(f"{cls.game.dealer_hidden}{cls.game.dealer_hand}")
                    print(cls.game.player_hand)
                    print("You have BlackJack!")
                    cls.play_game()
            
                if cls.game.end_game() ==1:
                    clear_screen()
                    print(f'{cls.game.dealer_hidden}{cls.game.dealer_hand}')
                    print(cls.game.player_hand)
                    print("You bust! Dealer wins")
                    cls.play_game()
            
                elif cls.game.end_game == 2:
                    clear_screen()
                    print(f"{cls.game.dealer_hidden}{cls.game.dealer_hand}")
                    print(cls.game.player_hand)
                    print("Dealer busts! You win!")
                    cls.play_game()
            
                elif cls.game.end_game() ==3:
                    clear_screen()
                    print(f'{cls.game.dealer_hidden}{cls.game.dealer_hand}')
                    print(cls.game.player_hand)
                    print("You win!")
                    cls.play_game()
            
                elif cls.game.end_game() == 4:
                    clear_screen()
                    print(f'{cls.game.dealer_hidden}{cls.game.dealer_hand}')
                    print(cls.game.player_hand)
                    print("Dealer wins!")
                    cls.play_game()

new_game = UI()
new_game.play_game()
