class TV:

    def __init__(self):
        self.isTVOn = True
        self.isTVOff = False

    def isOn(self, isTVOn: bool):
        if self.isTVOff is False:
            self.isTVOff is True
        return isTVOn

    def isOff(self, isTVOff: bool):
        if self.isTVOn is True:
            self.isTVOn = False

    def increaseVolume(self, increaseVolume):
        self.increaseVolume(0)
        increaseVolume + 1

    def decreaseVolume(self, decreaseVolume):
        self.decreaseVolume(decreaseVolume)
        decreaseVolume - 1
