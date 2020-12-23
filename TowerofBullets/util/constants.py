HUDVIEW_ID = 'HUD'
CLOSEVIEW_ID = 'CLOSE'
PAUSEVIEW_ID = 'PAUSE'
STARTVIEW_ID = 'START'
CONFIGVIEW_ID = 'CONFIG'
DEADVIEW_ID = 'DEAD',
WAITVIEW_ID = 'WAIT'
CHOOSEWEAPONVIEW_ID = 'CHOOSEWEAPON'

WEAPONS_DB = {
    'CAULE': {
        'COST': 2,
        'FIRE_RATE': 450,
        'SIZE': (80, 80),
        'IMAGE_FILE': 'caule.png',
        'BULLET': {
            'DAMAGE': 15,
            'SPEED': 4,
            'SIZE': (32, 32),
            'IMAGE_FILE': 'green_bullet.png'
        },
    },
    'BAMBUZINHO': {
        'COST': 1,
        'FIRE_RATE': 450,
        'SIZE': (60, 60),
        'IMAGE_FILE': 'bambuzinho.png',
        'BULLET': {
            'DAMAGE': 10,
            'SPEED': 4,
            'SIZE': (32, 32),
            'IMAGE_FILE': 'green_bullet.png'
        }
    },
    'AK47': {
        'COST': 1,
        'FIRE_RATE': 200,
        'SIZE': (80, 40),
        'IMAGE_FILE': 'ak47.png',
        'BULLET': {
            'DAMAGE': 10,
            'SPEED': 15,
            'SIZE': (20, 20),
            'IMAGE_FILE': 'sun.png'
        }
    },
    'BAD_PISTOL': {
        'COST': 0,
        'FIRE_RATE': 500,
        'SIZE': (60, 60),
        'IMAGE_FILE': 'bad_pistol.png',
        'BULLET': {
            'DAMAGE': 5,
            'SPEED': 3,
            'SIZE': (20, 20),
            'IMAGE_FILE': 'default.png'
        }
    },
    'BUBBLE_GUN': {
        'COST': 3,
        'FIRE_RATE': 500,
        'SIZE': (60, 60),
        'IMAGE_FILE': 'bubble_gun.png',
        'BULLET': {
            'DAMAGE': 50,
            'SPEED': 2,
            'SIZE': (64, 64),
            'IMAGE_FILE': 'bubble.png'
        }
    },
    'CHERRY_BLOSSOM': {
        'COST': 4,
        'FIRE_RATE': 300,
        'SIZE': (60, 60),
        'IMAGE_FILE': 'cherry_blossom.png',
        'BULLET': {
            'DAMAGE': 35,
            'SPEED': 2,
            'SIZE': (32, 32),
            'IMAGE_FILE': 'sakura.png'
        }
    },
    'SNOW_FOX': {
        'COST': 4,
        'FIRE_RATE': 250,
        'SIZE': (60, 60),
        'IMAGE_FILE': 'snow_fox.png',
        'BULLET': {
            'DAMAGE': 10,
            'SPEED': 5,
            'SIZE': (32, 32),
            'IMAGE_FILE': 'snowflake.png'
        }
    }
}

ENEMIES_DB = {
    "WOGOL": {
        'SPEED': 2,
        'HP': 150,
        'WEAPON': WEAPONS_DB["BAMBUZINHO"],
        'IMAGE_FILE': 'wogol/'
    },
    "SWAMPY": {
        'SPEED': 1,
        'HP': 100,
        'WEAPON': WEAPONS_DB["BUBBLE_GUN"],
        'IMAGE_FILE': 'swampy/'
    },
    "SKELETON": {
        'SPEED': 2,
        'HP': 150,
        'WEAPON': WEAPONS_DB["SNOW_FOX"],
        'IMAGE_FILE': 'skelet/'
    },
    "GOBLIN": {
        'SPEED': 4,
        'HP': 50,
        'WEAPON': WEAPONS_DB["BAD_PISTOL"],
        'IMAGE_FILE': 'goblin/'
    },
    "NECROMANCER": {
        'SPEED': 2,
        'HP': 150,
        'WEAPON': WEAPONS_DB["CHERRY_BLOSSOM"],
        'IMAGE_FILE': 'necromancer/'
    },
    "IMP": {
        'SPEED': 3,
        'HP': 70,
        'WEAPON': WEAPONS_DB["BAMBUZINHO"],
        'IMAGE_FILE': 'imp/'
    },
    "ORC_WARRIOR": {
        'SPEED': 1,
        'HP': 200,
        'WEAPON': WEAPONS_DB["AK47"],
        'IMAGE_FILE': 'orc/'
    },
    "LIZARD": {
        'SPEED': 3,
        'HP': 100,
        'WEAPON': WEAPONS_DB["BAMBUZINHO"],
        'IMAGE_FILE': 'lizard/'
    }
}

BOSS_DB = {
    "ORC_SHAMAN": {
        'SPEED': 1,
        'HP': 500,
        'WEAPON': WEAPONS_DB["BAD_PISTOL"],
        'IMAGE_FILE': 'orc_shaman/'
    },

    "BIG_ZOMBIE": {
        'SPEED': 1,
        'HP': 350,
        'WEAPON': WEAPONS_DB["BUBBLE_GUN"],
        'IMAGE_FILE': 'zombie/'
    },
    "OGRE": {
        'SPEED': 2,
        'HP': 300,
        'WEAPON': WEAPONS_DB["AK47"],
        'IMAGE_FILE': 'ogre/'
    },
    "MUDDY": {
        'SPEED': 1,
        'HP': 400,
        'WEAPON': WEAPONS_DB["BUBBLE_GUN"],
        'IMAGE_FILE': 'muddy/'
    },
    "FROZEN_LIZARD": {
        'SPEED': 2,
        'HP': 200,
        'WEAPON': WEAPONS_DB["SNOW_FOX"],
        'IMAGE_FILE': 'frozen_lizard/'
    },
    "KNIGHT": {
        'SPEED': 2,
        'HP': 250,
        'WEAPON': WEAPONS_DB["BAD_PISTOL"],
        'IMAGE_FILE': 'knight/'
    },
    "ICE_ZOMBIE": {
        'SPEED': 1,
        'HP': 500,
        'WEAPON': WEAPONS_DB["SNOW_FOX"],
        'IMAGE_FILE': 'ice_zombie/'
    },
    "CHORT": {
        'SPEED': 5,
        'HP': 100,
        'WEAPON': WEAPONS_DB["AK47"],
        'IMAGE_FILE': 'chort/'
    },
    "DEMON": {
        'SPEED': 3,
        'HP': 250,
        'WEAPON': WEAPONS_DB["CHERRY_BLOSSOM"],
        'IMAGE_FILE': 'big_demon/'
    }
}

ROOMS_DB = {
    'SALA1': {
        'SPAWN_POINT': (100, 400),
        'STRUCTURE': {
            'LAYOUT': '01.txt'
        },
        'WAVES': [
            {
                "ENEMY_QUANTITY": 1,
                "ENEMIES": [ENEMIES_DB['WOGOL'], ENEMIES_DB['SWAMPY']],
            },
            {
                "ENEMY_QUANTITY": 1,
                "ENEMIES": [BOSS_DB['BIG_ZOMBIE']]
            },
            {
                "ENEMY_QUANTITY": 4,
                "ENEMIES": [ENEMIES_DB['GOBLIN'], ENEMIES_DB['NECROMANCER']]
            },
            {
                "ENEMY_QUANTITY": 1,
                "ENEMIES": [BOSS_DB['BIG_ZOMBIE']]
            }
        ]
    },
    'SALA2': {
        'SPAWN_POINT': (650, 80),
        'STRUCTURE': {
            'LAYOUT': '02.txt'
        },
        'WAVES': [
            {
                "ENEMY_QUANTITY": 5,
                "ENEMIES": [ENEMIES_DB['SKELETON'], ENEMIES_DB['NECROMANCER']],
            },
            {
                "ENEMY_QUANTITY": 1,
                "ENEMIES": [ENEMIES_DB['IMP'], ENEMIES_DB['ORC_WARRIOR']]
            },
            {
                "ENEMY_QUANTITY": 1,
                "ENEMIES": [BOSS_DB['OGRE']]
            }
        ]
    },
    'SALA3': {
        'SPAWN_POINT': (320, 150),
        'STRUCTURE': {
            'LAYOUT': '03.txt'
        },
        'WAVES': [
            {
                "ENEMY_QUANTITY": 4,
                "ENEMIES": [ENEMIES_DB['IMP'], ENEMIES_DB['WOGOL']],
            },
            {
                "ENEMY_QUANTITY": 1,
                "ENEMIES": [BOSS_DB['DEMON']]
            },
            {
                "ENEMY_QUANTITY": 4,
                "ENEMIES": [ENEMIES_DB['LIZARD']]
            },
            {
                "ENEMY_QUANTITY": 1,
                "ENEMIES": [BOSS_DB['FROZEN_LIZARD']]
            }
        ]
    },
    'SALA4': {
        'SPAWN_POINT': (300, 400),
        'STRUCTURE': {
            'LAYOUT': '04.txt'
        },
        'WAVES': [
            {
                "ENEMY_QUANTITY": 6,
                "ENEMIES": [ENEMIES_DB['LIZARD']],
            },
            {
                "ENEMY_QUANTITY": 1,
                "ENEMIES": [BOSS_DB['DEMON']]
            },
            {
                "ENEMY_QUANTITY": 3,
                "ENEMIES": [ENEMIES_DB['LIZARD']]
            },
            {
                "ENEMY_QUANTITY": 5,
                "ENEMIES": [ENEMIES_DB['LIZARD']]
            },
            {
                "ENEMY_QUANTITY": 1,
                "ENEMIES": [BOSS_DB['FROZEN_LIZARD']]
            }
        ]
    }
}
