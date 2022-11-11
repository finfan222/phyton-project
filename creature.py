class Actor:
    name: str = "Actor"


class Player(Actor):
    target: Actor = None

    def set(self, newTarget: Actor):
        self.target = newTarget

    def get(self):
        return self.target
