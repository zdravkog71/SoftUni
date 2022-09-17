
from TestExercise.project_hero import Hero

from unittest import main

import unittest

# username: str, level: int, health: float, damage: float

class TestHero(unittest.TestCase):
    def setUp(self) -> None:
        self.hero = Hero('user', 1, 5.5, 1.5)

    def test_hero_init(self):
        result_username = self.hero.username
        result_level = self.hero.level
        result_health = self.hero.health
        result_damage = self.hero.damage
        expected_result_username = 'user'
        expected_result_level = 1
        expected_result_health = 5.5
        expected_result_damage = 1.5
        self.assertEqual(expected_result_username, result_username)
        self.assertEqual(expected_result_level, result_level)
        self.assertEqual(expected_result_health, result_health)
        self.assertEqual(expected_result_damage, result_damage)

    def test_battle__hero_is_enemy__raises_error(self):
        enemy_hero = Hero('user', 1, 5.5, 1.5)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual('You cannot fight yourself', str(ex.exception))

    def test_battle__health_is_zero__raises_error(self):
        enemy_hero = Hero('enemy', 1, 5.5, 1.5)
        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))

    def test_battle__health_is_negative__raises_error(self):
        enemy_hero = Hero('enemy', 1, 5.5, 1.5)
        self.hero.health = -1
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))

    def test_battle__enemy_health_is_zero__raises_error(self):
        enemy_hero = Hero('enemy', 1, 0, 1.5)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual('You cannot fight enemy. He needs to rest', str(ex.exception))

    def test_battle__enemy_and_hero_health__expect_health(self):
        enemy_hero = Hero('enemy', 1, 5, 2)
        result_player = self.hero.health
        expected_result_player = 5.5
        result_enemy = enemy_hero.health
        expected_result_enemy = 5
        self.assertEqual(expected_result_enemy, result_enemy)
        self.assertEqual(expected_result_player, result_player)

    def test_battle__player_and_enemy_negative_health__expect_draw(self):
        enemy_hero = Hero('enemy', 10, 1, 2)
        hero = Hero('zdr', 10, 1, 2)

        result = hero.battle(enemy_hero)
        expected_result = 'Draw'
        self.assertEqual(expected_result, result)

    def test_battle__enemy_health_negative__expect_player_incr(self):
        enemy_hero = Hero('enemy', 1, 1, 2)
        hero = Hero('zdr', 10, 10, 20)
        result = hero.battle(enemy_hero)
        result_player_level = hero.level
        result_player_health = hero.health
        result_player_damage = hero.damage
        expected_result = 'You win'
        expected_result_level = 11
        expected_result_health = 13
        expected_result_damage = 25
        self.assertEqual(expected_result, result)
        self.assertEqual(expected_result_level, result_player_level)
        self.assertEqual(expected_result_health, result_player_health)
        self.assertEqual(expected_result_damage, result_player_damage)

    def test_battle__player_health_negative__expect_player_incr(self):
        enemy_hero = Hero('enemy', 10, 10, 20)
        hero = Hero('zdr', 1, 1, 2)
        result = hero.battle(enemy_hero)
        result_enemy_level = enemy_hero.level
        result_enemy_health = enemy_hero.health
        result_enemy_damage = enemy_hero.damage
        expected_result = 'You lose'
        expected_result_level = 11
        expected_result_health = 13
        expected_result_damage = 25
        self.assertEqual(expected_result, result)
        self.assertEqual(expected_result_level, result_enemy_level)
        self.assertEqual(expected_result_health, result_enemy_health)
        self.assertEqual(expected_result_damage, result_enemy_damage)

    def test_string_repr(self):
        result = self.hero.__str__()
        expeted_result = 'Hero user: 1 lvl\nHealth: 5.5\nDamage: 1.5\n'
        self.assertEqual(expeted_result, result)


        """
        enemy_hero.level += 1
        enemy_hero.health += 5
        enemy_hero.damage += 5
        return "You lose"
        """

        # username: str, level: int, health: float, damage: float
        # player_damage = self.damage * self.level

if __name__ == "__main__":
    main()