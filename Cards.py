import random
#   Input validation packages here?  Checks to see if user entering proper values?


class Card():
    '''
    A simple card object.  Has a value and a suit.
    '''


    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        
        self.value_string = str(value)


    def show_card(self):
        print(f'{self.value} of {self.suit}')


class Deck():
    '''A deck of cards.  Generates a list of card objects. Allows for shuffling and showing all cards.'''

    def __init__(self, has_joker=False):
        self.cards = []
        self.create_deck(has_joker)

    def create_deck(self, has_joker=False):
        '''Create a stack of cards.  May include a standard pair of Jokers.'''

        for i, value in enumerate([x for x in ['Ace'] + list(range(2,11)) + ['Jack','Queen','King']]):
            for suit in ['Spades', 'Hearts','Diamonds','Clubs']:
                self.cards.append(Card(value, suit))

        if has_joker:
            for color in ['red','black']:
                self.cards.append(Card(color,'Joker'))

    def empty_deck(self):
        self.cards = []
        print('Deck is now emptied')

    def show_cards(self):
        print(f'There are {len(self.cards)} cards')
        for card in self.cards:
            card.show_card()

    def shuffle_cards(self):
        random.shuffle(self.cards)

class Player():
    '''Simple player.  Can draw cards and show hand.'''

    def __init__(self, name):
        self.hand = []
        self.name = name
        self.points = 0

    def draw_cards(self, Deck, number_of_cards):        # With replacement...
        '''Select a number of cards from a deck.  Place those cards in hand.'''

        try:
            assert number_of_cards > 0
        except AssertionError as e:
            print(f'{self.name}: You must draw at least positive 1 card!!!')
        print(f'{self.name} is drawing {number_of_cards} cards' if number_of_cards != 1 else f'{self.name} is drawing {number_of_cards} card')

        for i in range(number_of_cards):
            self.inspect_deck(Deck)
            self.hand.append(Deck.cards.pop())

    def inspect_deck(self, Deck):
        '''Generate a new deck if there are no more cards.'''
        if len(Deck.cards) == 0:
            Deck.create_deck()

    def put_deck_in_the_fire(self, Deck):
        '''Just completely obliterate the deck.'''
        Deck.cards = []

    def show_hand(self):
        '''Display all cards in hand.'''
        print(f'{self.name} is showing a hand.')
        for card in self.hand:
            card.show_card()

    def ask_if_card(self):
        if len(self.hand) != 0:
            card_value = ''
            while card_value not in [c.value_string for c in self.hand]:
                card_value = input(f'{self.name} Card value? ')
                if card_value not in [c.value_string for c in self.hand]:
                    print('You must type a value in hand.')
            print(f'Got any {card_value}s?')
            return card_value
        else:
            print('Your hand is empty :-(')
    
    def discard_card(self, number_of_cards):
        if number_of_cards <= len(self.hand):
            for i in range(number_of_cards):
                self.hand.pop()
        else:
            print(f'For {self.name}: Too many or some kind of weird negative number.  Or your deck is empty. Unable to discard anything.')


class Table():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.area = height * width

        self.decks = []
        self.players = []

    def add_deck(self, deck):
        self.decks.append(deck)

    def get_area_taken_by_decks(self):
        return sum([5 for x in self.decks])

    def get_space_left(self):
        return self.area - self.get_area_taken_by_decks()

    def add_players(self, players):
        ''':arg
        Takes a list of one or more players and adds them.
        '''
        for p in players:
            self.players.append(p)

    def get_number_of_players(self):
        return len(self.players)






my_deck = Deck(has_joker=False)
my_deck.shuffle_cards()
player_1 = Player('Jonathan')
player_1.draw_cards(my_deck,7)
player_1.show_hand()
player_2 = Player('Samantha')
player_2.draw_cards(my_deck, 7)
player_2.show_hand()



playing_table = Table(5,5)
playing_table.add_players([player_1,player_2])

print(playing_table.get_number_of_players())

print(playing_table.area)
playing_table.add_deck(my_deck)
print(playing_table.get_space_left())


for p in playing_table.players:
    print(p.points)

'''
turns = 0

while (len(player_1.hand) != 0 or len(player_2.hand) != 0) and turns < 2:
    asked_card = player_1.ask_if_card()
    if asked_card in [c.value_string for c in player_2.hand]:

        for i, o in enumerate(player_1.hand):
            if o.value_string == asked_card:
                del player_1.hand[i]

        for i, o in enumerate(player_2.hand):
            if o.value_string == asked_card:
                del player_2.hand[i]
                player_1.points += 1    # Give player 1 a point for each card eliminated from player 2 hand.


        print('Yes, I have that card.')


    else:
        print('Go fish.')
        print(len(player_1.hand))
        player_1.draw_cards(my_deck,1)
        print(len(player_1.hand))

    print()
    player_1.show_hand()
    print()
    player_2.show_hand()

    asked_card = player_2.ask_if_card()

    if asked_card in [c.value_string for c in player_1.hand]:

        for i, o in enumerate(player_1.hand):
            if o.value_string == asked_card:
                del player_1.hand[i]
                player_2.points += 1

        for i, o in enumerate(player_2.hand):
            if o.value_string == asked_card:
                del player_2.hand[i]


        print('Yes, I have that card.')
    else:
        print('Go fish.')
        print(len(player_2.hand))
        player_2.draw_cards(my_deck,1)
        print(len(player_2.hand))

    print()
    player_1.show_hand()
    print()
    player_2.show_hand()

    turns += 1


for p in [player_1, player_2]:
    print(f'{p.name} has {p.points - len(p.hand)} Points') # Winner is highest.







other_deck = Deck()

other_deck.empty_deck()
other_deck.show_cards()



#my_deck.show_cards()

print()

my_deck.shuffle_cards()

#my_deck.show_cards()

print(len(my_deck.cards)) # Before bob draws from the deck.

bob = Player('Bob')
bob.draw_cards(my_deck, 5)
bob.show_hand()

print(len(my_deck.cards)) # After bob draws from the deck.

#bob.put_deck_in_the_fire(my_deck)
my_deck.show_cards()
'''

