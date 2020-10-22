class Frog(object):
    """Game using Frogs as obstacles."""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f'{self} the Frog encounters {obstacle} and {act}'
        print(msg)


class Bug(object):
    def __str__(self):
        return 'a bug'

    def action(self):
        return 'eats it'

class FrogWorld(object):
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return "\n\n\t---- Frog World ---\n"

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()

class Wizard(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f'{self} the Wizard battles against {obstacle} and {act}'
        print(msg)

class Ork(object):
    def __str__(self):
        return 'an evil ork'

    def action(self):
        return 'kills it'

class WizardWorld(object):
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t------ Wizard ----\n'

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()

class GameEnvironment(object):
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


def validate_age(name):
    try:
        age = int(input(f'Welcome {name}. How old are you? '))
        # age = int(age)
    except ValueError as err:
        print(f"Age {age} is invalid, please try again...")
        return (False, age)
    return (True, age)

def main():
    name = input("Hello. What's your name? ")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
    game = FrogWorld if age < 18 else WizardWorld
    environment = GameEnvironment(game(name))
    environment.play()


# frog = Frog("flippy")
# frog.interact_with("Wall")
if __name__ == '__main__':
    main()
