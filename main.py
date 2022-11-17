import pygame

import assets
from gameengine import Display, GameEngine, GameResources, Window, Animations


class Mario(pygame.sprite.DirtySprite):
    def __init__(self) -> None:
        super().__init__()
        self.animation = Animations.get_animation("mario_small_walk", 5)
        
        self.image = self.animation.get_current_frame()
        self.rect = self.image.get_rect()
        self.rect.topleft = (10, 10)
        self.dirty = 2

    def update(self):
        super().update()
        self.animation.update(GameEngine.deltatime)

        self.image = self.animation.get_current_frame()
        


class GameManager(pygame.sprite.LayeredDirty):
    def __init__(self) -> None:
        self.mario = Mario()
        super().__init__(self.mario)

    def update(self) -> None:
        super().update()
        if GameEngine.request_quit:
            GameEngine.quit()


class Game:
    def __init__(self):

        Window.set_title("Super Mario World [Python]")
        Display.set_scale(4)

        Window.set_size((720, 405))
        Display.update_display_from_window()
        Display.update_background_from_display()

        assets.load_assets()

        GameEngine.set_framerate(60)
        GameEngine.set_scene(GameManager())

    def run(self):
        GameEngine.start_loop()


if __name__ == "__main__":
    Game().run()
