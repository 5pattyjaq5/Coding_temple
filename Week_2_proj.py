suits = ('hearts', 'diamonds', 'spades', 'clubs')
numbers = ('2', '3', '4', '5', '6', '7', '8', '9','J', 'Q', 'K', 'A')
sets = ('2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,'J':10, 'Q':10, 'K':10, 'A':11)

class Card:
    def __init__(self, suits, numbers,sets):
        self.suits = suits
        self.numbers = numbers
        self.sets = sets
    def __str__(self):
        return {self.numbers} + 'of' + {self.suits} + 'of' + {self.sets}    
    

    
class Deck:
    def __init__(self):
        self.deck = []
        self.hand = []
        self.cards =  [Card(suit, number) for suit in suits for number in numbers]
        self.shuffle_deck()
        
    def shuffle_deck(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()


player = []       
class Player: 
    def __init__(self):
        self.player = player
        self.hand = [player (Card)]
        return {self.hand} + {self.set}
    
    def bust(self):
        return f' Player bust' > 21
              
    #Create a method that will show the hand of the user/player
    def __init(self):
        if player : self.hand

    #Create a method displaying blackjack to the player        
    def blackjack(self):
        return f'Player wins' == 21

    def __init__(self):
        if player == ['blackjack'] == "True":
            if player ==[21] == "True" :
                
                def win(self):
                    print(f'{self.player} wins!')


          
class Human(Player):
    def __init__(self):
        super().__init__()
    def choose_action(self):
        while True:
            choice = input("Do you want to hit or stand? ")
            if choice.lower() == "hit" or choice.lower() == "stand":
                return choice.lower()
            else:
                print("Invalid choice. Please enter 'hit' or 'stand'.")

    

class Dealer(Player):
    def __init__(self):
        super().__init__()
    def choose_action(self):
        if self.score < 17:
            return "hit"
        else:
            return "stand"
  

class Game:
    def __init__ (self, dealer, human):
        self.dealer = dealer
        self.human = human
        self.player = [self.dealer, self.human]
        
    #Define a method to display a message if the user/player wins
    def victory(self):
        return f"Player wins!"

              
    #Define a method to display a message if the user/player pushes
    def push(self):
        return f"Push"

    #Define a method to display a message if the user/player loses
    def defeat(self):
        return f"Player loses"

def Main():
    bj_deck = Deck()
    bj_player = Player()
    bj_human = Human()
    bj_dealer = Dealer()
    bj_game = Game(bj_dealer, bj_player)
    #Ask the player how many decks they want to use - Then print the number of decks
    num_decks = int(input("How many decks do you want to use? "))
    print("You've chosen to use", num_decks, "decks.")
    deck.play_deck *= num_decks
    #Shuffle the deck
    Deck.shuffle_deck()

    Dealer.deal_hand(Deck, Human)
 # Game loop
    while True:
        # Show player's hand
        print("Your hand:", Human.display_hand())
 # Ask the player if they want a hit
        if input("Do you want a hit? (yes/no) ").lower() == "yes":
            Dealer.hit(Deck, Human)
        else:  # Player stands
            # Dealer takes cards while their score is less than 16
            while Dealer.score < 16:
                Dealer.add_card(Deck.play_deck.pop())
            # Compare scores and display result
            if Human.bust():
                print("You busted!")
                Game.defeat()
                break
            elif Dealer.bust() or Human.score > Dealer.score:
                Game.victory()
                break
            elif Human.score < Dealer.score:
                Game.defeat()
                break
            else:  # human.score == dealer.score
                Game.push()
                break
    # Ask the player if they want to play again
    play_again = input("Do you want to play again? (yes/no) ").lower()
    if play_again == "yes" or play_again == "yes"