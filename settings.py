from pydantic import Field, BaseModel


class GameConfig(BaseModel):
    width: int = 1280
    height: int = 800
    fps: int = 60
    ball_size: tuple = (20, 20)
    enemy_size: tuple = (20, 20)
    velocity: int = 4


config = GameConfig()
