HUDVIEW_ID = 'HUD'
CLOSEVIEW_ID = 'CLOSE'
PAUSEVIEW_ID = 'PAUSE'
STARTVIEW_ID = 'START'
CONFIGVIEW_ID = 'CONFIG'
DEADVIEW_ID = 'DEAD',
RESTART_ID = 'RESTART'

WEAPONS_DB = {
    'CAULE': {
        'COST': 1,
        'DAMAGE': 5,
        'FIRE_RATE': 150,
        'BULLET_SPEED': 7,
        'SIZE': (80, 80),
        'IMAGE_FILE': 'items/weapons/caule.png'
    },
    'BAMBUZINHO': {
        'COST': 0,
        'DAMAGE': 1,
        'FIRE_RATE': 200,
        'BULLET_SPEED': 4,
        'SIZE': (60, 60),
        'IMAGE_FILE': 'items/weapons/bambuzinho.png'
    },
    'AK47': {
        'COST': 0,
        'DAMAGE': 50,
        'FIRE_RATE': 100,
        'BULLET_SPEED': 4,
        'SIZE': (80, 40),
        'IMAGE_FILE': 'items/weapons/ak47.png'
    },
    'BAD_PISTOL': {
        'COST': 0,
        'DAMAGE': 1,
        'FIRE_RATE': 150,
        'BULLET_SPEED': 4,
        'SIZE': (60, 60),
        'IMAGE_FILE': 'items/weapons/bad_pistol.png'
    },
    'BUBBLE_GUN': {
        'COST': 0,
        'DAMAGE': 1,
        'FIRE_RATE': 200,
        'BULLET_SPEED': 4,
        'SIZE': (60, 60),
        'IMAGE_FILE': 'items/weapons/bubble_gun.png'
    },
    'CHERRY_BLOSSOM': {
        'COST': 0,
        'DAMAGE': 1,
        'FIRE_RATE': 200,
        'BULLET_SPEED': 4,
        'SIZE': (60, 60),
        'IMAGE_FILE': 'items/weapons/cherry_blossom.png'
    },
    'SNOW_FOX': {
        'COST': 0,
        'DAMAGE': 1,
        'FIRE_RATE': 200,
        'BULLET_SPEED': 4,
        'SIZE': (60, 60),
        'IMAGE_FILE': 'items/weapons/snow_fox.png'
    }
}

ENEMIES_DB = {
  "WOGOL": {
    'SPEED': 2,
    'HP': 100,
    'WEAPON': WEAPONS_DB["BAMBUZINHO"],
    'IMAGE_FILE': 'characters/enemies/wogol.png'
  },
  "SWAMPY": {
    'SPEED': 2,
    'HP': 100,
    'WEAPON': WEAPONS_DB["CAULE"],
    'IMAGE_FILE': 'characters/enemies/swampy.png'
  },
  "SKELETON": {
    'SPEED': 2,
    'HP': 100,
    'WEAPON': WEAPONS_DB["SNOW_FOX"],
    'IMAGE_FILE': 'characters/enemies/skelet.png'
  },
  "GOBLIN": {
    'SPEED': 4,
    'HP': 50,
    'WEAPON': WEAPONS_DB["BUBBLE_GUN"],
    'IMAGE_FILE': 'characters/enemies/goblin.png'
  },
  "NECROMANCER": {
    'SPEED': 2,
    'HP': 100,
    'WEAPON': WEAPONS_DB["CHERRY_BLOSSOM"],
    'IMAGE_FILE': 'characters/enemies/necromancer.png'
  },
  "IMP": {
    'SPEED': 3,
    'HP': 100,
    'WEAPON': WEAPONS_DB["BAMBUZINHO"],
    'IMAGE_FILE': 'characters/enemies/imp.png'
  },
  "ORC_WARRIOR": {
    'SPEED': 1,
    'HP': 100,
    'WEAPON': WEAPONS_DB["CAULE"],
    'IMAGE_FILE': 'characters/enemies/orc.png'
  }
}

BOSS_DB = {
  "ORC_SHAMAN": {
    'SPEED': 3,
    'HP': 150,
    'WEAPON': WEAPONS_DB["BAD_PISTOL"],
    'IMAGE_FILE': 'characters/enemies/orc_shaman.png'
  },
  
  "BIG_ZOMBIE": {
    'SPEED': 2,
    'HP': 400,
    'WEAPON': WEAPONS_DB["CAULE"],
    'IMAGE_FILE': 'characters/enemies/zombie.png'
  },
  "OGRE": {
    'SPEED': 2,
    'HP': 300,
    'WEAPON': WEAPONS_DB["BAD_PISTOL"],
    'IMAGE_FILE': 'characters/enemies/ogre.png'
  },
  "MUDDY": {
    'SPEED': 1,
    'HP': 400,
    'WEAPON': WEAPONS_DB["SNOW_FOX"],
    'IMAGE_FILE': 'characters/enemies/muddy.png'
  },
  "LIZARD": {
    'SPEED': 3,
    'HP': 300,
    'WEAPON': WEAPONS_DB["CHERRY_BLOSSOM"],
    'IMAGE_FILE': 'characters/enemies/lizard.png'
  },
  "FROZEN_LIZARD": {
    'SPEED': 1,
    'HP': 100,
    'WEAPON': WEAPONS_DB["BUBBLE_GUN"],
    'IMAGE_FILE': 'characters/enemies/frozen_lizard.png'
  },
  "KNIGHT":{
    'SPEED': 2,
    'HP': 250,
    'WEAPON': WEAPONS_DB["BAD_PISTOL"],
    'IMAGE_FILE': 'characters/enemies/knight.png'
  },
  "ICE_ZOMBIE": {
    'SPEED': 1,
    'HP': 100,
    'WEAPON': WEAPONS_DB["SNOW_FOX"],
    'IMAGE_FILE': 'characters/enemies/ice_zombie.png'
  },
  "CHORT": {
    'SPEED': 1,
    'HP': 100,
    'WEAPON': WEAPONS_DB["BAMBUZINHO"],
    'IMAGE_FILE': 'characters/enemies/chort.png'
  },
  "DEMON": {
    'SPEED': 2,
    'HP': 200,
    'WEAPON': WEAPONS_DB["CAULE"],
    'IMAGE_FILE': 'characters/enemies/demon.png'
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
                "ENEMIES": [BOSS_DB['KNIGHT']]
            }
        ]
    }
}