#expeditions should have:

# an origin (probably always gazorpazorp spacestations?)
# should have a desination
# a spaceship assigned to it
# a list of passengers

class Expedition:
    def __init__(self,destination,spaceship,passenger_list = [],origin = 'Gazorpazorp Station'):
        self.__destination = destination
        self.__spaceship = spaceship
        self.__passenger_list =[]
        self.__origin = origin

    def assign_spaceship(self, new_ship):
        self.__spaceship = new_ship

    def expo_details(self):
        # we want to send a dictionary with:
            #origin
            #destination
            #ship
            #passenger list
        expo_details = {
            'origin': self.__origin,
            'destination': self.__destination,
            'ship': self.__spaceship,
            'pass_list': self.__passenger_list
        }
        return expo_details

    def add_pass_to_expo(self, passenger):
        self.__passenger_list.append(passenger)

    def get_destination(self):
        return self.__destination

    def get_origin(self):
        return self.__origin

    def get_spaceship(self):
        return self.__spaceship

    def get_pass_list(self):
        return self.__passenger_list

    def print_list_passengers(self):
        for passenger in self.get_pass_list():
            print('Name: ' + passenger.name + ',', 'Species: ' + passenger.species + ',', 'IDR: ' + passenger.intergalactic_dna_reg)