from InheritanceExercises.project_hero.hero import Hero

class Elf(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)

