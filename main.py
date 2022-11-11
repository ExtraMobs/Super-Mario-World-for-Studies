import pygame
from gameengine import GameEngine


class SpriteTest(pygame.sprite.DirtySprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(
            r"assets\Playable Characters\SNES - Super Mario World - Luigi All-Stars.png"
        )
        self.rect = self.image.get_rect()


class GameManager(pygame.sprite.LayeredDirty):
    def __init__(self) -> None:
        super().__init__()

        self.sprite_test = SpriteTest()
        self.add(self.sprite_test)


class Game:
    def __init__(self):
        GameEngine.init()

        GameEngine.set_scale(4)

        GameEngine.set_window_title("Super Mario World [Python]")
        GameEngine.set_window_size((720, 405))

        GameEngine.set_framerate(60)

        GameEngine.set_current_scene(GameManager())

    def run(self):
        GameEngine.start_loop()


if __name__ == "__main__":
    Game().run()
