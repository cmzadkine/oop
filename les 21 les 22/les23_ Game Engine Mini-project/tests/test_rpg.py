"""
tests/test_rpg.py
-------------------
Unittests voor Player, Enemy, Item en Level.
De opdracht noemt losse handmatige "✅ Test:"-stappen per stap;
hier staan ze als automatische unittests zodat je ze steeds kan
her-draaien.

Run met:
    python -m unittest
"""

import unittest

from models.player import Player
from models.enemy import Enemy
from models.item import Item
from models.level import Level


class TestPlayer(unittest.TestCase):

    def test_take_damage_niet_onder_nul(self):
        player = Player("Held", hp=10, attack_power=5)
        player.take_damage(100)
        self.assertEqual(player.hp, 0)
        self.assertFalse(player.is_alive())

    def test_heal_niet_boven_max_hp(self):
        player = Player("Held", hp=100, attack_power=5)
        player.take_damage(50)
        player.heal(1000)
        self.assertEqual(player.hp, 100)

    def test_attack_doet_damage_bij_enemy(self):
        player = Player("Held", hp=100, attack_power=15)
        enemy = Enemy("Wolf", hp=20, attack_power=4)
        player.attack(enemy)
        self.assertEqual(enemy.hp, 5)

    def test_use_item_heal(self):
        player = Player("Held", hp=100, attack_power=10)
        player.take_damage(50)  # hp nu 50/100, zodat healen ruimte heeft
        potion = Item("Potion", "heal", 20)
        player.add_item(potion)
        player.use_item("Potion")
        self.assertEqual(player.hp, 70)
        self.assertEqual(len(player.inventory), 0)

    def test_use_item_attack_boost(self):
        player = Player("Held", hp=50, attack_power=10)
        sword = Item("Sword", "attack_boost", 5)
        player.add_item(sword)
        player.use_item("Sword")
        self.assertEqual(player.attack_power, 15)

    def test_use_niet_bestaand_item(self):
        player = Player("Held")
        boodschap = player.use_item("Onbestaand")
        self.assertIn("geen item", boodschap)


class TestEnemy(unittest.TestCase):

    def test_enemy_attack_op_player(self):
        player = Player("Held", hp=100, attack_power=10)
        enemy = Enemy("Goblin", hp=25, attack_power=6)
        enemy.attack(player)
        self.assertEqual(player.hp, 94)

    def test_enemy_is_alive(self):
        enemy = Enemy("Goblin", hp=10, attack_power=6)
        enemy.take_damage(10)
        self.assertFalse(enemy.is_alive())


class TestLevel(unittest.TestCase):

    def test_is_cleared_true_zonder_enemies(self):
        level = Level("Forest", "Een bos")
        self.assertTrue(level.is_cleared())

    def test_is_cleared_false_met_levende_enemy(self):
        level = Level("Forest", "Een bos", enemies=[Enemy("Wolf", hp=10)])
        self.assertFalse(level.is_cleared())

    def test_is_cleared_true_na_dode_enemy(self):
        wolf = Enemy("Wolf", hp=10)
        wolf.take_damage(10)
        level = Level("Forest", "Een bos", enemies=[wolf])
        self.assertTrue(level.is_cleared())

    def test_remove_item_bestaand(self):
        potion = Item("Potion", "heal", 20)
        level = Level("Forest", "Een bos", items=[potion])
        gevonden = level.remove_item("potion")
        self.assertEqual(gevonden, potion)
        self.assertEqual(len(level.items), 0)

    def test_remove_item_niet_bestaand(self):
        level = Level("Forest", "Een bos", items=[])
        gevonden = level.remove_item("onbestaand")
        self.assertIsNone(gevonden)


if __name__ == "__main__":
    unittest.main()
