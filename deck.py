


class Deck:
    def __init__(self, game,
                 deck: list):

        self.game = game

        self.deck = deck

        self.damage_summ = self.get_damage_summ()
        self.armor_summ = self.get_armor_summ()

    def get_damage_summ(self):
        damage_summ = 0

        for i in self.deck:
            damage_summ += i.damage

        return damage_summ

    def get_armor_summ(self):
        armor_summ = 0

        for i in self.deck:
            armor_summ += i.armor

        return armor_summ
