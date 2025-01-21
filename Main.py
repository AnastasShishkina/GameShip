from Game import Game, configShips
def inputShipName():
    while True:
        shipName = raw_input("Enter ship name: ").strip()
        if shipName  in configShips:
            return shipName
        print('Invalid Ship Name! Try Again!')


def inputDistance():
    while True:
        distance = raw_input("Enter distance: ").strip()
        if distance.isdigit() and int(distance)>=0 and int(distance)<=30:
            return distance
        print('Invalid distance! Try Again! [0,30]!')



if __name__ == '__main__':
    shipName1 = inputShipName()
    shipName2 = inputShipName()
    distance = inputDistance()
    # for test
    # shipName1 = 'Bismarck'
    # shipName2 = 'Hipper'
    # distance = 23
    game = Game(shipName1, shipName2,distance)
    game.play()

