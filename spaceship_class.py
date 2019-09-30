# spaceships should have:

# captain
# name
# intergalactic_warp_drive_signature

class Spaceship:
    def __init__(self, captain,name,warp_drive_signature):
        self.captain = captain
        self.__name = name
        self.__warp_drive_signature = warp_drive_signature

    def identify(self):
        return self.__warp_drive_signature

    def identify_name(self):
        return self.__name

    def change_name(self, name):
        self.__name = name