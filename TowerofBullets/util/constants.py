HUDVIEW_ID = 'HUD'
CLOSEVIEW_ID = 'CLOSE'
PAUSEVIEW_ID = 'PAUSE'
STARTVIEW_ID = 'START'
CONFIGVIEW_ID = 'CONFIG'
DEADVIEW_ID = 'DEAD'

WEAPONS_DB = {
    'CAULE': {
        'DAMAGE': 1,
        'FIRE_RATE': 200,
        'BULLET_SPEED': 1,
        'IMAGE_FILE': 'items/weapons/caule.png'
    },
    'BAMBUZINHO': {
        'DAMAGE': 1,
        'FIRE_RATE': 200,
        'BULLET_SPEED': 1,
        'IMAGE_FILE': 'items/weapons/bambuzinho.png'
    },
    'AK47': {
        'DAMAGE': 1,
        'FIRE_RATE': 250,
        'BULLET_SPEED': 1,
        'IMAGE_FILE': 'items/weapons/ak47.png'
    },
    'BAD_PISTOL': {
        'DAMAGE': 1,
        'FIRE_RATE': 150,
        'BULLET_SPEED': 1,
        'IMAGE_FILE': 'items/weapons/bad_pistol.png'
    },
    'BUBBLE_GUN': {
        'DAMAGE': 1,
        'FIRE_RATE': 200,
        'BULLET_SPEED': 1,
        'IMAGE_FILE': 'items/weapons/bubble_gun.png'
    },
    'CHERRY_BLOSSOM': {
        'DAMAGE': 1,
        'FIRE_RATE': 200,
        'BULLET_SPEED': 1,
        'IMAGE_FILE': 'items/weapons/cherry_blossom.png'
    },
    'SNOW_FOX': {
        'DAMAGE': 1,
        'FIRE_RATE': 200,
        'BULLET_SPEED': 1,
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
        'STRUCTURE': {
            'LAYOUT': '1607133545.txt'
        },
        'WAVES': [
            {
                "AMOUNT": 1,
                "ENEMIES": [ENEMIES_DB['WOGOL'], ENEMIES_DB['SWAMPY']],
            },
            {
                "AMOUNT": 1,
                "ENEMIES": [BOSS_DB['BIG_ZOMBIE']]
            },
            {
                "AMOUNT": 4,
                "ENEMIES": [ENEMIES_DB['GOBLIN'], ENEMIES_DB['NECROMANCER']]
            },
            {
                "AMOUNT": 1,
                "ENEMIES": [BOSS_DB['BIG_ZOMBIE']]
            }
        ]
    },
    'SALA2': {
        'STRUCTURE': {
            'LAYOUT': '02.txt'
        },
        'WAVES': [
            {
                "AMOUNT": 5,
                "ENEMIES": [ENEMIES_DB['SKELETON'], ENEMIES_DB['NECROMANCER']],
            },
            {
                "AMOUNT": 1,
                "ENEMIES": [ENEMIES_DB['IMP'], ENEMIES_DB['ORC_WARRIOR']]
            },
            {
                "AMOUNT": 1,
                "ENEMIES": [BOSS_DB['KNIGHT']]
            }
        ]
    }
}