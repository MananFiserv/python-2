from src.Character import Character

class Fighter(Character):
    pass
    
    def __repr__(self) -> str:
        return f'Fighter: {self.hit_points} hit points' 