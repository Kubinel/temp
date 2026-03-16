class Postava:
    def __init__(self, hp, utok):
        self.hp = hp
        self.utok = utok

    def is_alive(self):
        return self.hp > 0

    def minus_hp(self, utok_protihraca):
        self.hp -= utok_protihraca

p = Postava(10, 7)
print(p.hp)
print(p.utok)

p.minus_hp(2)
print(p.hp)

print(p.is_alive())

