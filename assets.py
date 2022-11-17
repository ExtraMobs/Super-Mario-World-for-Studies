import os

from gameengine import Animations, GameResources

assets = None

class Assets:
    def __init__(self, dict_data: dict):
        for key, item in dict_data.items():
            if type(item) == dict:
                item = Assets(item)
            setattr(self.__class__, key, item)


def load_assets_to_dict(path):
    folder_dict = {}
    for item in os.listdir(path):
        path_temp = os.path.join(path, item)
        item = item.split(".")[0].strip().replace(" ", "_")
        if os.path.isdir(path_temp):
            folder_dict[item] = load_assets_to_dict(path_temp)
        else:
            folder_dict["_" + item] = GameResources.Surface.load_surface_from_file(path_temp)
    return folder_dict


def build_animations():
    # Animations.add_animation_data("mario_small_walk", Animations.AREA_TYPE, assets.mario.small._walk, (0,0,48,48))
    Animations.add_animation_data("mario_small_walk", Animations.AREA_TYPE, assets.mario.small._walk, (48,0,48,48))
    Animations.add_animation_data("mario_small_walk", Animations.AREA_TYPE, assets.mario.small._walk, (96,0,48,48))


def load_assets():
    global assets
    assets = Assets(load_assets_to_dict(os.path.abspath("assets")))
    build_animations()
