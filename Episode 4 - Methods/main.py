class Hero:
    # class variable
    jumlah_hero = 0
    
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1
        
    # void function, method tanpa return, tanpa argumen
    def siapa(self):
        print(f'Namaku adalah {self.name}')
        
    # method dengan argumen, tanpa return
    def healthUp(self, up):
        self.health += up
        
    # method dengan return
    def getHealth(self):
        return self.health
    
hero1 = Hero('Sniper', 100, 10, 5)
hero2 = Hero('Mario Bros', 90, 5, 10)

print(hero1.__dict__)
print(hero2.__dict__)

hero1.siapa()
hero1.healthUp(10)
print(hero1.health)
print(hero1.getHealth())