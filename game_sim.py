
class Player:
    def __init__(self, pname, hand:set) -> None:
        self.pname = pname
        self.hand = hand
    
    score = 0
    selection = None
    unplayed_cards = [] #TODO list of all unknown cards, e.g. cards that this player has not made visual contact with

    def choose(self, card:int) -> None: #this is how the player chooses a card and puts it face down
        assert card in self.hand
        self.selection = card
        self.hand.remove(card)


class Game:
    def __init__(self, num_players:int) -> None:
        self.p = [] #list of player objects
        for i in range(num_players):
            self.p.append(Player(str(i)))
    
    turns = 10
    deck = set(range(1,105))
    middle = [[23], [69], [2], [90]] #TODO randomize


    def flip(self):
        #gather all cards, order cards, place them, nmmt as necessary, reset selection for each player, count turn down
        pass

    def Nmmt(self, cards, player):
        pass

myGame = Game(7)
print(myGame.p[0])





class Person:
  lastname = "someone"

  def __init__(self, name):
    self.name = name

p1 = Person("Linus")
p2 = Person("Emil")

p1.lastname = "Alfred"

print(p1.lastname)
print(p2.lastname)

Person.lastname = "Refsnes"

print(p1.lastname)
print(p2.lastname)

# Source - https://stackoverflow.com/a
# Posted by Hugh Bothwell
# Retrieved 2025-11-17, License - CC BY-SA 3.0

class Room(object):      # note: class name is Capitalized
    def __init__(self, number):
        self.number = number

    # get_ methods are non-Pythonic.
    # If you need to do some processing to retrieve room number,
    # make it a @property; otherwise, just use the field name

class House(object):
    def __init__(self, num_rooms):
        # I assume you don't want a room 0?
        self.rooms = [Room(i) for i in range(1, num_rooms+1)]
    def __iter__(self):
        return iter(self.rooms)

mansion = House(10)
for room in mansion:
    print(room.number)
