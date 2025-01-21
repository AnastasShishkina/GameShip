import math


class Nation(object):
    UK = 'UK'
    GERMANY = 'Germany'


class ShipType(object):
    BATTLESHIP = 'Battleship'
    CRUISER = 'Cruiser'


configShips = {
    'Belfast': {
        'shipType': ShipType.CRUISER,
        'nation': Nation.UK,
        'damage': 4000,
        'attackDistance': 14,
        'maxHealth': 30000,
        'speed': 2
    },
    'Hood': {
        'shipType': ShipType.BATTLESHIP,
        'nation': Nation.UK,
        'damage': 12000,
        'attackDistance': 20,
        'maxHealth': 50000,
        'speed': 1.5
    },
    'Hipper': {
        'shipType': ShipType.CRUISER,
        'nation': Nation.GERMANY,
        'damage': 4000,
        'attackDistance': 14,
        'maxHealth': 30000,
        'speed': 2
    },
    'Bismarck': {
        'shipType': ShipType.BATTLESHIP,
        'nation': Nation.GERMANY,
        'damage': 12000,
        'attackDistance': 20,
        'maxHealth': 50000,
        'speed': 1.5
    },
}


class Ship():
    def __init__(self, name, config):
        self.name = name
        self.shipType = config['shipType']
        self.nation = config['nation']
        self.damage = config['damage']
        self.attackDistance = config['attackDistance']
        self.maxHealth = config['maxHealth']
        self.health = self.maxHealth
        self.speed = config['speed']
        self.countSeriesAttack = 0

    def getDamageWithNationCoeff(self, distance, damage):
        if self.nation == Nation.UK and distance > 8:
            return math.floor(0.5 * damage)
        elif self.nation == Nation.GERMANY:
            return 0.8 * damage
        return damage

    def getAttackWithShipTypeCoeff(self, distance, damage):
        if self.shipType == ShipType.BATTLESHIP and self.countSeriesAttack == 1:
            self.countSeriesAttack = 0
            return 0
        elif self.shipType == ShipType.CRUISER and distance <= 5:
            return 4 * damage
        self.countSeriesAttack += 1
        return damage

    def attack(self, enemy, distance):
        if distance <= self.attackDistance:
            realAttack = self.getAttackWithShipTypeCoeff(distance, self.damage)
            enemy.getDamage(realAttack, distance)

    def getDamage(self, damage, distance):
        realDamage = self.getDamageWithNationCoeff(distance, damage)
        print('Damage', realDamage)
        self.health -= realDamage



class Game(object):

    def __init__(self, shipName1, shipName2, distanceBetweenShips):
        self.ship1 = Ship(shipName1, configShips[shipName1])
        self.ship2 = Ship(shipName2, configShips[shipName2])
        self.distanceBetweenShips = int(distanceBetweenShips)

    def play(self):
        print('Start Game Between Ships', self.ship1.name, self.ship2.name, 'start distance ', self.distanceBetweenShips)
        step = 1
        while not self.isFinal():
            print('---------------------------')
            print('Step Game', step)
            print('distance Between Ships', self.distanceBetweenShips)
            print('Ship1', self.ship1.name, 'attack', 'Ship2', self.ship2.name)
            self.ship1.attack(self.ship2, self.distanceBetweenShips)
            print('Ship2', self.ship2.name, 'attack', 'Ship1', self.ship1.name)
            self.ship2.attack(self.ship1, self.distanceBetweenShips)
            self.move()
            step += 1

    def isFinal(self):
        if self.ship1.health <= 0 and self.ship2.health <= 0:
            print('Draw! The ships killed each other at the same time')
            return True
        elif self.ship1.health <= 0:
            print('Victory! ',self.ship2.name, 'won!')
            return True
        elif self.ship2.health <= 0:
            print('Victory! ',self.ship1.name, 'won!')
            return True
        elif abs(self.distanceBetweenShips) > self.ship1.attackDistance and abs(
                self.distanceBetweenShips) > self.ship2.attackDistance and self.distanceBetweenShips<0:
            print('Draw! The ships sailed very far away')
            return True
        return False

    def move(self):
        self.distanceBetweenShips -= self.ship1.speed + self.ship2.speed




