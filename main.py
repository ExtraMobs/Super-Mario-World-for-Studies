import math
import os

import pygame

from gameengine import Animations, Display, GameEngine, GameResources, Window


class SpriteTest(pygame.sprite.DirtySprite):
    def __init__(self):
        super().__init__()
        self.image = GameResources.get_surface("Mario SpriteSheet")
        self.rect = self.image.get_rect()


class GameManager(pygame.sprite.LayeredDirty):
    def __init__(self) -> None:
        super().__init__()

        self.sprite_test = SpriteTest()
        self.add(self.sprite_test)

    def update(self) -> None:
        super().update()
        if GameEngine.request_quit:
            GameEngine.quit()


class Game:
    def __init__(self):

        Window.set_title("Super Mario World [Python]")
        Display.set_scale(4)

        GameEngine.init((720, 405))

        self.load_sprites()

        GameEngine.set_framerate(60)
        GameEngine.set_current_scene(GameManager())

    def load_sprites(self):
        playable_characters = os.path.abspath("assets\Playable Characters")
        GameResources.add_surface_from_file(
            "Mario SpriteSheet",
            os.path.join(playable_characters, "SNES - Super Mario World - Mario.png"),
        )
        GameResources.add_surface_from_file(
            "Luigi SpriteSheet",
            os.path.join(
                playable_characters, "SNES - Super Mario World - Luigi All-Stars.png"
            ),
        )
        self.save_playable_sprites()

    def save_playable_sprites(self):
        mario_spritesheet = GameResources.get_surface("Mario SpriteSheet")
        a = pygame.PixelArray(mario_spritesheet)
        a.replace((0, 148, 148), (0, 0, 0, 0))
        # a.replace((0,52,52), (0,0,0,0))
        # a.replace((0,84,84), (0,0,0,0))
        # a.replace((0,66,66), (0,0,0,0))
        # a.replace((0,116,116), (0,0,0,0))
        a.replace((88, 168, 240), (0, 0, 0, 0))

        playable_pos = [
            (8, 33),
            (8, 97),
            (8, 174),
            (8, 251),
            (8, 328),
            (8, 410),  # 5
            (8, 461),  # 6
            (8, 576),  # 7
            (8, 647),
            (8, 724),
            (8, 801),
            (8, 878),
            (8, 963),  # 12
            (8, 1014),  # 13
            (8, 1129),
            (8, 1193),
            (8, 1257),
            (8, 1321),
            (8, 1372),
            (8, 1436),
            (8, 1487),
            (8, 1551),  # 21
            (8, 1627),
            (8, 1691),
            (8, 1755),
            (8, 1819),
            (8, 1883),
            (8, 1960),
            (8, 2024),
            (8, 2088),
            (8, 2152),
            (8, 2203),
            (8, 2267),
            (8, 2318),
            (8, 2395),
            (8, 2459),
            (8, 2524),
            (8, 2588),
            (8, 2665),
            (8, 2729),
            (8, 2806),
            (8, 2870),
            (8, 2947),
            (8, 2998),  # 43
            (8, 3052),  # 44
            (8, 3119),  # 45
            (8, 3200),  # 46
            (8, 3293),
            (8, 3370),  # 48
        ]
        names = [None for _ in range(len(playable_pos))]
        names[0] = [
            {"path": "sprites/mario/small/idle.png", "qtd": 1},
            {"path": "sprites/mario/small/look up.png", "qtd": 1},
            {"path": "sprites/mario/small/duck.png", "qtd": 1},
            {"path": "sprites/mario/small/walk.png", "qtd": 3},
            {"path": "sprites/mario/small/run.png", "qtd": 3},
            {"path": "sprites/mario/small/wall run.png", "qtd": 4},
            {"path": "sprites/mario/small/skid.png", "qtd": 1},
        ]
        names[1] = [
            {"path": "sprites/mario/small/pipe vertical.png", "qtd": 1},
            {"path": "sprites/mario/small/jump.png", "qtd": 1},
            {"path": "sprites/mario/small/fall.png", "qtd": 1},
            {"path": "sprites/mario/small/run jump.png", "qtd": 1},
            {"path": "sprites/mario/small/spin jump.png", "qtd": 4},
            {"path": "sprites/mario/small/slide.png", "qtd": 1},
            {"path": "sprites/mario/small/kick.png", "qtd": 1},
            {"path": "sprites/mario/small/swim.png", "qtd": 3},
            {"path": "sprites/mario/small/victory.png", "qtd": 1},
        ]
        names[2] = [
            {"path": "sprites/mario/small/hold/idle.png", "qtd": 1},
            {"path": "sprites/mario/small/hold/look up.png", "qtd": 1},
            {"path": "sprites/mario/small/hold/duck.png", "qtd": 1},
            {"path": "sprites/mario/small/hold/walk run jump.png", "qtd": 3},
            {"path": "sprites/mario/small/hold/swim.png", "qtd": 3},
            {"path": "sprites/mario/small/riding yoshi/idle.png", "qtd": 1},
            {"path": "sprites/mario/small/riding yoshi/eat.png", "qtd": 2},
            {"path": "sprites/mario/small/riding yoshi/turn.png", "qtd": 1},
            {"path": "sprites/mario/small/riding yoshi/pipe horizontal.png", "qtd": 1},
            {"path": "", "qtd": 1},
            {"path": "sprites/mario/small/riding yoshi/victory.png", "qtd": 1},
        ]
        names[3] = [
            {"path": "sprites/mario/small/climbing vine net/idle.png", "qtd": 2},
            {"path": "sprites/mario/small/climbing vine net/punch.png", "qtd": 2},
            {"path": "sprites/mario/small/climbing vine net/turn.png", "qtd": 5},
            {"path": "sprites/mario/small/other/p ballon.png", "qtd": 1},
            {"path": "sprites/mario/small/other/death.png", "qtd": 1},
            {"path": "sprites/mario/small/other/grow up.png", "qtd": 3},
        ]
        names[4] = [
            {"path": "sprites/mario/small/cutscenes/castle 3.png", "qtd": 3},
            {"path": "sprites/mario/small/cutscenes/castle 4.png", "qtd": 2},
            {"path": "sprites/mario/small/cutscenes/castle 5.png", "qtd": 3},
            {"path": "sprites/mario/small/cutscenes/castle 6.png", "qtd": 3},
            {"path": "sprites/mario/small/cutscenes/bowsers castle.png", "qtd": 2},
        ]
        names[5] = [
            {"path": "sprites/mario/small/cutscenes/castle 3 assemble.png", "qtd": 11},
            {"path": "sprites/mario/small/cutscenes/castle 6 1.png", "qtd": 4},
        ]
        names[6] = [
            {"path": "sprites/mario/small/cutscenes/castle 6 2.png", "qtd": 16},
        ]
        for i, pos in enumerate(playable_pos):
            names_index = 0
            count = 0
            for x in range(19):
                if names[i] is not None and names_index < len(names[i]):
                    if count == 0:
                        count = names[i][names_index]["qtd"]
                        path = names[i][names_index]["path"]
                        if path != "":
                            path = os.path.abspath(path)
                        sprites = []
                        names_index += 1
                sub_x = x * 52 + pos[0]
                sub_pos = (sub_x, pos[1])
                rect_size = (52, 48)
                if i == 5:
                    if x >= 11:
                        sub_x += (x - 11) * 10
                        sub_pos = (sub_x, 405)
                        rect_size = (62, 53)
                elif i in (6, 13):
                    rect_size = (52, 78)
                elif i == 7:
                    if x == 13:
                        sub_pos = (708, 576)
                    elif x >= 14:
                        sub_pos = (800, 576)
                    elif x >= 9:
                        rect_size = (54, 55)
                elif i == 12:
                    if x >= 15:
                        sub_pos = (800, 576)
                    elif x >= 11:
                        sub_x += (x - 11) * 10
                        rect_size = (62, 56)
                        sub_pos = (sub_x, sub_pos[1] - 8)
                    elif x >= 4:
                        sub_pos = (sub_x, sub_pos[1] - 3)
                        rect_size = (52, 51)
                elif i == 21:
                    if x < 4:
                        rect_size = (58, 60)
                        sub_x += x * 6
                    else:
                        sub_x += 4 * 6
                    sub_pos = (sub_x, pos[1])
                elif i in (43, 44):
                    rect_size = (52, 51)
                elif i == 45:
                    rect_size = (62, 56)
                    sub_x += x * 10
                    if x == 15:
                        rect_size = (58, 56)
                    sub_pos = (sub_x, pos[1])
                elif i == 46:
                    if x == 0:
                        rect_size = (62, 56)
                    else:
                        rect_size = (52, 78)
                        sub_pos = (sub_pos[0] + 10, sub_pos[1] - 22)
                elif i == 48:
                    if x < 4:
                        rect_size = (58, 60)
                        sub_x += x * 6
                    else:
                        sub_x += 4 * 6
                    if x >= 9:
                        sub_x += 11
                    elif x == 4:
                        rect_size = (53, 48)
                    else:
                        sub_x += 1
                    sub_pos = (sub_x, sub_pos[1])

                rect = pygame.Rect(sub_pos, rect_size)
                try:
                    sub = mario_spritesheet.subsurface(rect)
                    sub = sub.subsurface(sub.get_bounding_rect())
                    # print((x, i), sub_pos, sub.get_bounding_rect())
                except ValueError:
                    ...
                if count > 0:
                    count -= 1
                    sprites.append(sub)
                if len(sprites) > 0 and count == 0:
                    if path != "":
                        w = 0
                        h = 0
                        for sprite in sprites:
                            w += sprite.get_width()
                            h = max(sprite.get_height(), h)
                        sprite_sheet = pygame.Surface((w, h)).convert_alpha()
                        x_path = 0
                        for sprite in sprites:
                            sprite_sheet.blit(sprite, (x_path, 0))
                            x_path += sprite.get_width()
                        if not os.path.exists(os.path.dirname(path)):
                            os.makedirs(os.path.dirname(path))
                        pygame.image.save(sprite_sheet, path)
                        sprites.clear()

    def run(self):
        GameEngine.start_loop()


if __name__ == "__main__":
    Game().run()
