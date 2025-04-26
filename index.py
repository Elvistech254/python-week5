class GameCharacter:
    def __init__(self, username, level, class_type, health_points):
        self.username = username
        self.level = level
        self.class_type = class_type
        self.health_points = health_points
        self._xp = 0  # encapsulated XP

    def attack(self):
        return f"{self.username} attacks with basic strike!"

    def level_up(self):
        self.level += 1
        self.health_points += 20
        self._xp = 0
        return f"{self.username} leveled up to {self.level}!"

    def gain_xp(self, amount):
        self._xp += amount
        return f"{self.username} gained {amount} XP!"

    def get_xp(self):
        return f"{self.username} has {self._xp} XP."








