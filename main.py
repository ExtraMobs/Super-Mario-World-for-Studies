import pygame

from assets import load_assets
from gameengine import Display, GameEngine, GameResources, Window


class SpriteTest(pygame.sprite.DirtySprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = GameResources.Global.get_global_data("assets").mario.small._idle
        self.rect = self.image.get_rect()


class GameManager(pygame.sprite.LayeredDirty):
    def __init__(self) -> None:
        super().__init__(SpriteTest())

    def update(self) -> None:
        super().update()
        if GameEngine.request_quit:
            GameEngine.quit()


class Game:
    def __init__(self):

        Window.set_title("Super Mario World [Python]")
        Display.set_scale(4)

        GameEngine.init((720, 405))

        GameResources.Global.set_global_data("assets", load_assets())

        GameEngine.set_framerate(60)
        GameEngine.set_current_scene(GameManager())

    def run(self):
        GameEngine.start_loop()


if __name__ == "__main__":
    Game().run()
