HUDVIEW_ID = 'HUD'
CLOSEVIEW_ID = 'CLOSE'
PAUSEVIEW_ID = 'PAUSE'
STARTVIEW_ID = 'START'
CONFIGVIEW_ID = 'CONFIG'
DEADVIEW_ID = 'DEAD',
WAITVIEW_ID = 'WAIT'

WEAPONS_DB = {
    'CAULE': {
        'COST': 10,
        'FIRE_RATE': 350,
        'SIZE': (80, 80),
        'IMAGE_FILE': 'caule.png',
        'BULLET': {
          'DAMAGE': 50,
          'SPEED': 13,
          'SIZE': (30, 30),
          'IMAGE_FILE': 'bubble.png'
        },
    },
    'BAMBUZINHO': {
        'COST': 0,
        'FIRE_RATE': 200,
        'SIZE': (60, 60),
        'IMAGE_FILE': 'bambuzinho.png',
        'BULLET': {
          'DAMAGE': 5,
          'SPEED': 7,
          'SIZE': (18, 18),
          'IMAGE_FILE': 'green_bullet.png'
        }
    },
    'AK47': {
        'COST': 1,
        'FIRE_RATE': 100,
        'SIZE': (80, 40),
        'IMAGE_FILE': 'ak47.png',
        'BULLET': {
          'DAMAGE': 5,
          'SPEED': 5,
          'SIZE': (15, 15),
          'IMAGE_FILE': 'default.png'
        }
    },
    'BAD_PISTOL': {
        'COST': 0,
        'FIRE_RATE': 150,
        'SIZE': (60, 60),
        'IMAGE_FILE': 'bad_pistol.png',
        'BULLET': {
          'DAMAGE': 5,
          'SPEED': 5,
          'SIZE': (15, 15),
          'IMAGE_FILE': 'default.png'
        }
    },
    'BUBBLE_GUN': {
        'COST': 0,
        'FIRE_RATE': 200,
        'SIZE': (60, 60),
        'IMAGE_FILE': 'bubble_gun.png',
        'BULLET': {
          'DAMAGE': 5,
          'SPEED': 5,
          'SIZE': (15, 15),
          'IMAGE_FILE': 'bubble.png'
        }
    },
    'CHERRY_BLOSSOM': {
        'COST': 0,
        'FIRE_RATE': 200,
        'SIZE': (60, 60),
        'IMAGE_FILE': 'cherry_blossom.png',
        'BULLET': {
          'DAMAGE': 5,
          'SPEED': 5,
          'SIZE': (16, 16),
          'IMAGE_FILE': 'sakura.png'
        }
    },
    'SNOW_FOX': {
        'COST': 0,
        'FIRE_RATE': 100,
        'SIZE': (60, 60),
        'IMAGE_FILE': 'snow_fox.png',
        'BULLET': {
          'DAMAGE': 3,
          'SPEED': 5,
          'SIZE': (13, 13),
          'IMAGE_FILE': 'snowflake.png'
        }
    }
}

ENEMIES_DB = {
  "WOGOL": {
    'SPEED': 2,
    'HP': 100,
    'WEAPON': WEAPONS_DB["BAMBUZINHO"],
    'IMAGE_FILE': 'wogol/'
  },
  "SWAMPY": {
    'SPEED': 2,
    'HP': 100,
    'WEAPON': WEAPONS_DB["CAULE"],
    'IMAGE_FILE': 'swampy/'
  },
  "SKELETON": {
    'SPEED': 2,
    'HP': 100,
    'WEAPON': WEAPONS_DB["SNOW_FOX"],
    'IMAGE_FILE': 'skelet/'
  },
  "GOBLIN": {
    'SPEED': 4,
    'HP': 50,
    'WEAPON': WEAPONS_DB["BUBBLE_GUN"],
    'IMAGE_FILE': 'goblin/'
  },
  "NECROMANCER": {
    'SPEED': 2,
    'HP': 100,
    'WEAPON': WEAPONS_DB["CHERRY_BLOSSOM"],
    'IMAGE_FILE': 'necromancer/'
  },
  "IMP": {
    'SPEED': 3,
    'HP': 100,
    'WEAPON': WEAPONS_DB["BAMBUZINHO"],
    'IMAGE_FILE': 'imp/'
  },
  "ORC_WARRIOR": {
    'SPEED': 1,
    'HP': 100,
    'WEAPON': WEAPONS_DB["CAULE"],
    'IMAGE_FILE': 'orc/'
  }
}

BOSS_DB = {
  "ORC_SHAMAN": {
    'SPEED': 3,
    'HP': 150,
    'WEAPON': WEAPONS_DB["BAD_PISTOL"],
    'IMAGE_FILE': 'orc_shaman/'
  },
  
  "BIG_ZOMBIE": {
    'SPEED': 2,
    'HP': 400,
    'WEAPON': WEAPONS_DB["CAULE"],
    'IMAGE_FILE': 'zombie/'
  },
  "OGRE": {
    'SPEED': 2,
    'HP': 300,
    'WEAPON': WEAPONS_DB["BAD_PISTOL"],
    'IMAGE_FILE': 'ogre/'
  },
  "MUDDY": {
    'SPEED': 1,
    'HP': 400,
    'WEAPON': WEAPONS_DB["SNOW_FOX"],
    'IMAGE_FILE': 'muddy/'
  },
  "LIZARD": {
    'SPEED': 3,
    'HP': 300,
    'WEAPON': WEAPONS_DB["CHERRY_BLOSSOM"],
    'IMAGE_FILE': 'lizard/'
  },
  "FROZEN_LIZARD": {
    'SPEED': 1,
    'HP': 100,
    'WEAPON': WEAPONS_DB["BUBBLE_GUN"],
    'IMAGE_FILE': 'frozen_lizard/'
  },
  "KNIGHT":{
    'SPEED': 2,
    'HP': 250,
    'WEAPON': WEAPONS_DB["BAD_PISTOL"],
    'IMAGE_FILE': 'knight/'
  },
  "ICE_ZOMBIE": {
    'SPEED': 1,
    'HP': 100,
    'WEAPON': WEAPONS_DB["SNOW_FOX"],
    'IMAGE_FILE': 'ice_zombie/'
  },
  "CHORT": {
    'SPEED': 1,
    'HP': 100,
    'WEAPON': WEAPONS_DB["BAMBUZINHO"],
    'IMAGE_FILE': 'chort/'
  },
  "DEMON": {
    'SPEED': 2,
    'HP': 200,
    'WEAPON': WEAPONS_DB["CAULE"],
    'IMAGE_FILE': 'demon/'
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
    }
}