from pydantic import Field, BaseModel
from random import randint


class GameConfig(BaseModel):
    width: int = 1280
    height: int = 800
    fps: int = 120
    ball_size: tuple = (20, 20)
    enemy_size: tuple = (20, 20)
    velocity: int = 4
    game_object: dict = {
        "enemy": {
            "rect": (width, randint(0, height)),
            "size": (20, 20),
            "speed": (0, velocity - 2),
            "img": "./graphics/enemy.png",
        },
        "bonus": {"rect": "bonus_rect", "size": (20, 20), "bonus_img": "./graphics/bonus.png"},
    }


config = GameConfig()
