#expeditions should have:

# an origin (probably always gazorpazorp spacestations?)
# should have a desination
# a spaceship assigned to it
# a list of passengers

class Expedition:
    def __init__(self,destination,spaceship,passenger_list = [],origin = 'Gazorpazorp Station'):
        self.destination = destination
        self.spaceship = spaceship
        self.passenger_list =[]
        self.origin = origin