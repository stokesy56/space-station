# import all classes
from passenger_class import *
from spaceship_class import *
from expedition_class import *
# create object here
    # generate 6 passengers
passenger1 = Passenger('Vish', 'Which', '007')
passenger2 = Passenger('Mous', 'Marching', '684')
passenger3 = Passenger('David', 'Which', '666')
passenger4 = Passenger('Lennok', 'Marching', '777')
passenger5 = Passenger('Dan', 'Pluton', '584')
passenger6 = Passenger('Chewie', 'Wookie', '657')
    # generate 3 spaceships
ship1 = Spaceship('Morgan', 'RPS', 'xyz')
ship2 = Spaceship('Marvel', 'Dissapointos', 'GPO1345')
ship3 = Spaceship('Sparrow', 'Black Pearl', 'BP56070')
    # generate 3 expeditions
        # keep list of generated expeditions (empty list of expeditions)


        #assign spacecraft to each
            # should be able to assign on creation of objects
            # should be able to assign post-facto
expedition1 = Expedition('Mars', ship3)
expedition2 = Expedition('Death Star', ship2)
expedition3 = Expedition('Destination Unknown', ship1)

expedition_list = []
expedition_list.append(expedition1)
expedition_list.append(expedition2)
expedition_list.append(expedition3)
    # assign to each expedition 2 passengers (append)(method)
expedition1.add_pass_to_expo(passenger1)
expedition1.add_pass_to_expo(passenger2)
expedition2.add_pass_to_expo(passenger1)
expedition2.add_pass_to_expo(passenger2)
expedition3.add_pass_to_expo(passenger1)
expedition3.add_pass_to_expo(passenger2)

    # iterate over list of expeditions and print
for expedition in expedition_list:
    print('Origin: ' + expedition.get_origin() + ',', 'Destination: ' + expedition.get_destination() + ',', 'Spaceship: ' + expedition.get_spaceship().identify_name())

    # iterate over list of expeditions and print
        # iterate over list of passenger objects
        # print out passenger details
expedition1.print_list_passengers()
# Create while llop here
    #use input() to get user input and generated objects dynamically




# create while loop here