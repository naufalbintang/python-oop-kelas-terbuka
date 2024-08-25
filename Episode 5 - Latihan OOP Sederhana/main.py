class Hero:
    def __init__(self, name, health, attackPower, armorNumber):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber
        
    def serang(self, lawan):
        print(f'{self.name} menyerang {lawan.name}')
        lawan.diserang(self, self.attackPower)
        
    def diserang(self, lawan, attackPower_lawan):
        print(f'{self.name} diserang {lawan.name}')
        attack_diterima = attackPower_lawan / self.armorNumber
        print(f'Serangan diterima adalah {str(attack_diterima)}')
        self.health -= attack_diterima
        print(f'Health {self.name} tersisa {str(self.health)}')

sniper = Hero('Sniper', 100, 10, 5)
rikimaru = Hero('Rikimaru', 100, 20, 10)

sniper.serang(rikimaru)
print('')
rikimaru.serang(sniper)