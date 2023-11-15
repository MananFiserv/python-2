from src.Character import Character

class Dwarf(Character):
    pass

    def __repr__(self) -> str:
        return f'Dwarf: {self.hit_points} hit points'