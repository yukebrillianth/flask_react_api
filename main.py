from random import randint


class Hero ():
    def __init__(self, HeroName, HeroHealth, HeroDamage):
        self.name = HeroName
        self.health = HeroHealth
        self.Damage = HeroDamage

    def attckingHero(self, hero, count):
        print(self.name, 'is attacking', hero.name)
        print(hero.name, 'has attacked by', self.name)
        attackCount = 1
        while (attackCount < count):
            heroHealth = randint(self.Damage//1.2, self.Damage) * attackCount
            if hero.health - heroHealth < 2:
                print(hero.name, 'is Dead!')
                break
            print('sisa darah', hero.name, hero.health - heroHealth)
            attackCount += 1

    # def attcked(self, Hero):


Hero1 = Hero("Nashwa", 100, 7)
Hero2 = Hero("Yuke", 120, 3)

Hero1.attckingHero(Hero2, 100)
# Hero1.attcked(Hero2)
