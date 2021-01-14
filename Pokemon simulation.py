import random
import copy

pokedex = {
    "bulbasaur": {
        'typing': ['gra', 'poi'],
        'health': 45,
        'atk': 49,
        'def': 49,
        'spatk': 65,
        'spdef': 65,
        'spd': 45
    },
    "ivysaur": {
        'typing': ['gra', 'poi'],
        'health': 60,
        'atk': 62,
        'def': 63,
        'spatk': 80,
        'spdef': 80,
        'spd': 60
    },
    "venosaur": {
        'typing': ['gra', 'poi'],
        'health': 80,
        'atk': 82,
        'def': 83,
        'spatk': 100,
        'spdef': 100,
        'spd': 80
    },
    "charmander": {
        'typing': ['fir'],
        'health': 39,
        'atk': 52,
        'def': 43,
        'spatk': 60,
        'spdef': 50,
        'spd': 65
    },
    "charmeleon": {
        'typing': ['fir'],
        'health': 58,
        'atk': 64,
        'def': 58,
        'spatk': 80,
        'spdef': 65,
        'spd': 80
    },
    "charizard": {
        'typing': ['fir', 'fly'],
        'health': 78,
        'atk': 84,
        'def': 78,
        'spatk': 109,
        'spdef': 85,
        'spd': 100
    },
    "squirtle": {
        'typing': ['wat'],
        'health': 44,
        'atk': 48,
        'def': 65,
        'spatk': 50,
        'spdef': 64,
        'spd': 43
    },
    "wartortle": {
        'typing': ['wat'],
        'health': 59,
        'atk': 63,
        'def': 80,
        'spatk': 65,
        'spdef': 80,
        'spd': 58
    },
    'blastoise': {
        'typing': ['wat'],
        'health': 79,
        'atk': 83,
        'def': 100,
        'spatk': 85,
        'spdef': 105,
        'spd': 78
    }
}

# print(pokedex["charizard"]['typing'])

move_info = {
    'sample_move': {
        'typing': 'nor',
        'side': 'phy',
        'pwr': 1,
        'acc': 1,
        'pp': 1,
        'status_eff': ('par', .1),
        'stat_eff': ('atk', -1, .1, 'target'),
        'recoil': ('dmg', .1)
    },
    'pound': {
        'typing': 'nor',
        'side': 'phy',
        'pwr': 40,
        'acc': 1,
        'pp': 35,
        'status_eff': None,
        'stat_eff': None,
        'recoil': None
    },
    'karate chop': {
        'typing': 'fig',
        'side': 'phy',
        'pwr': 50,
        'acc': 1,
        'pp': 25,
        'status_eff': None,
        'stat_eff': None,
        'recoil': None
    },
    'fire punch': {
        'typing': 'fir',
        'side': 'phy',
        'pwr': 75,
        "acc": 1,
        "pp": 15,
        "status_eff": ('bur', .1),
        "stat_eff": None,
        "recoil": None
    },
    'ice punch': {
        'typing': 'ice',
        'side': 'phy',
        'pwr': 75,
        "acc": 1,
        "pp": 15,
        "status_eff": ('fre', .1),
        "stat_eff": None,
        "recoil": None
    },
    'thunder punch': {
        'typing': 'fir',
        'side': 'phy',
        'pwr': 75,
        "acc": 1,
        "pp": 15,
        "status_eff": ('par', .1),
        "stat_eff": None,
        "recoil": None
    },
    'swords dance': {
        'typing': 'nor',
        'side': None,
        'pwr': None,
        "acc": None,
        "pp": 20,
        "status_eff": None,
        "stat_eff": [('atk', +2, None, 'self')],
        "recoil": None
    },
    'sand attack': {
        'typing': 'gro',
        'side': None,
        'pwr': None,
        'acc': 1,
        'pp': 15,
        'status_eff': None,
        'stat_eff': [('acc', -1, None, 'target')],
        'recoil': None
    },
    'body slam': {
        'typing': 'nor',
        'side': 'phy',
        'pwr': 85,
        'acc': 1,
        'pp': 15,
        'status_eff': ('par', .3),
        'stat_eff': None,
        'recoil': None
    },
    'take down': {
        'typing': 'nor',
        'side': 'phy',
        'pwr': 90,
        "acc": .85,
        'pp': 20,
        "status_eff": None,
        "stat_eff": None,
        "recoil": ('dmg', .25)
    },
    'double-edge': {
        'typing': 'nor',
        'side': 'phy',
        'pwr': 120,
        'acc': 1,
        'pp': 15,
        'status_eff': None,
        'stat_eff': None,
        'recoil': ('dmg', .33)
    },
    'sing': {
        'typing': 'nor',
        'side': None,
        'pwr': None,
        'acc': .55,
        'pp': 15,
        'status_eff': ('slp', 1),
        'stat_eff': None,
        'recoil': None
    },
    'flamethrower': {
        'typing': 'fir',
        'side': 'spe',
        'pwr': 90,
        'acc': 1,
        'pp': 15,
        'status_eff': ('bur', .1),
        'stat_eff': None,
        'recoil': None
    },
    'hydro pump': {
        'typing': 'wat',
        'side': 'spe',
        'pwr': 110,
        'acc': .8,
        'pp': 5,
        'status_eff': None,
        'stat_eff': None,
        'recoil': None
    },
    'surf': {
        'typing': 'wat',
        'side': 'spe',
        'pwr': 90,
        'acc': 1,
        'pp': 15,
        'status_eff': None,
        'stat_eff': None,
        'recoil': None
    },
    'ice beam': {
        'typing': 'ice',
        'side': 'spe',
        'pwr': 90,
        'acc': 1,
        'pp': 10,
        'status_eff': ('fre', .1),
        'stat_eff': None,
        'recoil': None
    },
    'blizzard': {
        'typing': 'ice',
        'side': 'spe',
        'pwr': 110,
        'acc': .7,
        'pp': 5,
        'status_eff': ('fre', .1),
        'stat_eff': None,
        'recoil': None
    },
    'drill peck': {
        'typing': 'fly',
        'side': 'spe',
        'pwr': 80,
        'acc': 1,
        'pp': 20,
        'status_eff': None,
        'stat_eff': None,
        'recoil': None
    },
    'leech seed': {
        'typing': 'gra',
        'side': None,
        'pwr': None,
        'acc': .9,
        'pp': 10,
        'status_eff': ('lee', 1),
        'stat_eff': None,
        'recoil': None
    },
    'poison powder': {
        'typing': 'poi',
        'side': None,
        'pwr': None,
        'acc': .75,
        'pp': 35,
        'status_eff': ('poi', 1),
        'stat_eff': None,
        'recoil': None
    },
    'stun spore': {
        'typing': 'gra',
        'side': None,
        'pwr': None,
        'acc': .75,
        'pp': 30,
        'status_eff': ('par', 1),
        'stat_eff': None,
        'recoil': None
    },
    "sleep powder": {
        'typing': 'gra',
        'side': None,
        'pwr': None,
        "acc": .75,
        "pp": 15,
        "status_eff": ('slp', 1),
        "stat_eff": None,
        "recoil": None
    },
    'string shot': {
        'typing': 'bug',
        'side': None,
        'pwr': None,
        'acc': .95,
        'pp': 40,
        'status_eff': None,
        'stat_eff': [('spd', -1, None, 'target')],
        'recoil': None
    },
    'thunderbolt': {
        'typing': 'ele',
        'side': 'spe',
        'pwr': 90,
        'acc': 1,
        'pp': 15,
        'status_eff': ('par', .1),
        'stat_eff': None,
        'recoil': None
    },
    'thunder wave': {
        'typing': 'ele',
        'side': None,
        'pwr': None,
        'acc': .9,
        'pp': 20,
        'status_eff': ('par', 1),
        'stat_eff': None,
        'recoil': None
    },
    'thunder': {
        'typing': 'ele',
        'side': 'spe',
        'pwr': 110,
        'acc': .7,
        'pp': 10,
        'status_eff': ('par', .1),
        'stat_eff': None,
        'recoil': None
    },
    'earthquake': {
        'typing': 'gro',
        'side': 'phy',
        'pwr': 100,
        'acc': 1,
        'status_eff': None,
        'stat_eff': None,
        'recoil': None
    },
    'toxic': {
        'typing': 'poi',
        'side': None,
        'pwr': None,
        'acc': .9,
        'pp': 10,
        'status_eff': ('tox', 1),
        'stat_eff': None,
        'recoil': None
    },
    'psychic': {
        'typing': 'psy',
        'side': 'spe',
        'pwr': 90,
        'acc': 1,
        'pp': 10,
        'status_eff': None,
        'stat_eff': [('spdef', -1, .1, 'target')],
        'recoil': None
    },
    'hypnosis': {
        'typing': 'psy',
        'side': None,
        'pwr': None,
        'acc': .6,
        'pp': 20,
        'status_eff': ('slp', 1),
        'stat_eff': None,
        'recoil': None
    },
    'agility': {
        'typing': 'psy',
        'side': None,
        'pwr': None,
        'acc': None,
        'pp': 30,
        'status_eff': None,
        'stat_eff': [('spd', +2, None, 'self')],
        'recoil': None
    },
    'quick attack': {
        'typing': 'nor',
        'side': 'phy',
        'pwr': 40,
        'acc': 1,
        'pp': 30,
        'status_eff': None,
        'stat_eff': None,
        'recoil': None,
        'att': {'pri': +1}
    },
    'screech': {
        'typing': 'nor',
        'side': None,
        'pwr': None,
        'acc': .85,
        'pp': 40,
        'status_eff': None,
        'stat_eff': ('def', -2, None, 'target'),
        'recoil': None
    },
    'double team': {
        'typing': 'nor',
        'side': None,
        'pwr': None,
        'acc': None,
        'pp': 15,
        'status_eff': None,
        'stat_eff': ('eva', +1, None, 'self'),
        'recoil': None
    },
    'recover': {
        'typing': 'nor',
        'side': None,
        'pwr': None,
        'acc': None,
        'pp': 10,
        'status_eff': None,
        'stat_eff': None,
        'recoil': ('heal', 'half')
    },
    'minimize': {
        'typing': 'nor',
        'side': None,
        'pwr': None,
        'acc': None,
        'pp': 10,
        'status_eff': None,
        'stat_eff': [('eva', +1, None, 'self')],
        'recoil': None
    },
    'smokescreen': {
        'typing': 'nor',
        'side': None,
        'pwr': None,
        'acc': 1,
        'pp': 20,
        'status_eff': None,
        'stat_eff': [('acc', -1, None, 'target')],
        'recoil': None
    },
    'confuse ray': {
        'typing': 'gho',
        'side': None,
        'pwr': None,
        'acc': 1,
        'pp': 10,
        'status_eff': ('con', 1),
        'stat_eff': None,
        'recoil': None
    },
    'barrier': {
        'typing': 'psy',
        'side': None,
        'pwr': None,
        'acc': None,
        'pp': 20,
        'status_eff': None,
        'stat_eff': [('def', +2, None, 'self')],
        'recoil': None
    },
    'self-destruct': {
        'typing': 'nor',
        'side': 'phy',
        'pwr': 200,
        'acc': 1,
        'pp': 5,
        'status_eff': None,
        'stat_eff': None,
        'recoil': ('death', None)
    },
    'fire blast': {
        'typing': 'fir',
        'side': 'spe',
        'pwr': 110,
        'acc': .85,
        'pp': 5,
        'status_eff': ('bur', .1),
        'stat_eff': None,
        'recoil': None
    },
    'waterfall': {
        'typing': 'wat',
        'side': 'phy',
        'pwr': 80,
        'acc': 1,
        'pp': 15,
        'status_eff': ('fli', .2),
        'stat_eff': None,
        'recoil': None
    },
    'amnesia': {
        'typing': 'psy',
        'side': None,
        'pwr': None,
        'acc': None,
        'pp': 20,
        'status_eff': None,
        'stat_eff': [('spdef', +2, None, 'self')],
        'recoil': None
    },
    'soft boiled': {
        'typing': 'nor',
        'side': None,
        'pwr': None,
        'acc': None,
        'pp': 10,
        'status_eff': None,
        'stat_eff': None,
        'recoil': ('heal', 'half')
    },
    'high jump kick': {
        'typing': 'fig',
        'side': 'phy',
        'pwr': 130,
        'acc': .9,
        'pp': 10,
        'status_eff': None,
        'stat_eff': None,
        'recoil': None
    },
    'glare': {
        'typing': 'nor',
        'side': None,
        'pwr': None,
        'acc': 1,
        'pp': 30,
        'status_eff': ('par', 1),
        'stat_eff': None,
        'recoil': None
    },
    'leech life': {
        'typing': 'bug',
        'side': 'phy',
        'pwr': 80,
        'acc': 1,
        'pp': 10,
        'status_eff': None,
        'stat_eff': None,
        'recoil': ('heal', .5)
    },
    'lovely kiss': {
        'typing': 'nor',
        'side': None,
        'pwr': None,
        'acc': .75,
        'pp': 10,
        'status_eff': ('slp', 1),
        'stat_eff': None,
        'recoil': None
    },
    'acid armor': {
        'typing': 'poi',
        'side': None,
        'pwr': None,
        'acc': None,
        'pp': 20,
        'status_eff': None,
        'stat_eff': [('def', +2, None, 'self')],
        'recoil': None
    },
    'crabhammer': {
        'typing': 'wat',
        'side': 'phy',
        'pwr': 100,
        'acc': .9,
        'pp': 10,
        'status_eff': None,
        'stat_eff': None,
        'recoil': None,
        'att': {'hi-crit': +1}
    },
    'explosion': {
        'typing': 'nor',
        'side': 'phy',
        'pwr': 250,
        'acc': 1,
        'pp': 5,
        'status_eff': None,
        'stat_eff': None,
        'recoil': ('death', None)
    },
    'rest': {
        'typing': 'psy',
        'side': None,
        'pwr': None,
        'acc': None,
        'pp': 10,
        'status_eff': None,
        'stat_eff': None,
        'recoil': ('rest', None)
    },
    'rock slide': {
        'typing': 'roc',
        'side': 'phy',
        'pwr': 75,
        'acc': .9,
        'pp': 10,
        'status_eff': ('fli', .3),
        'stat_eff': None,
        'recoil': None
    },
    'tri attack': {
        'typing': 'nor',
        'side': 'spe',
        'pwr': 80,
        'acc': 1,
        'pp': 10,
        'status_eff': ('tri', .2),
        'stat_eff': None,
        'recoil': None
    },
    'substitute': {
        'typing': 'nor',
        'side': None,
        'pwr': None,
        'acc': None,
        'pp': 10,
        'status_eff': None,
        'stat_eff': None,
        'recoil': None
    },
    'curse': {
        'typing': 'gho',
        'side': None,
        'pwr': None,
        'acc': None,
        'pp': 10,
        'status_eff': None,
        'stat_eff': [('atk', +1, None, 'self'),
                     ('def', +1, None, 'self'),
                     ('spd', -1, None, 'self')],
        'recoil': None
    },
    'aeroblast': {
        'typing': 'fly',
        'side': 'spe',
        'pwr': 100,
        'acc': .95,
        'pp': 5,
        'status_eff': None,
        'stat_eff': None,
        'recoil': None
    },
    'cotton spore': {
        'typing': 'gra',
        'side': None,
        'pwr': None,
        'acc': None,
        'pp': 40,
        'status_eff': None,
        'stat_eff': [('def', +3, None, 'self')],
        'recoil': None
    },
    'protect': {
        'typing': 'nor',
        'side': None,
        'pwr': None,
        'acc': None,
        'pp': 10,
        'status_eff': None,
        'stat_eff': None,
        'recoil': None,
        'att': {'pri': +5}
    },
    'mach punch': {
        'typing': 'fig',
        'side': 'phy',
        'pwr': 40,
        'acc': 1,
        'pp': 30,
        'status_eff': None,
        'stat_eff': None,
        'recoil': None,
        'att': {'pri': +1}
    },
    'scary face': {
        'typing': 'normal',
        'side': None,
        'pwr': None,
        'acc': 1,
        'status_eff': None,
        'stat_eff': ('spd', -2, None, 'target'),
        'recoil': None
    }
}

# print(move_info['swords dance']["acc"])

type_list = {
    'nor': {
        'roc': .5,
        'ste': .5,
        'gho': 0
    },
    'fir': {
        'fir': .5,
        'wat': .5,
        'gra': 2,
        'ice': 2,
        'bug': 2,
        'roc': .5,
        'dra': .5,
        'ste': 2
    },
    'wat': {
        'fir': 2,
        'wat': .5,
        'gra': .5,
        'gro': 2,
        'roc': 2,
        'dra': .5,
    },
    'ele': {
        'wat': 2,
        'ele': .5,
        'gra': .5,
        'gro': 0,
        'fly': 2,
        'dra': .5
    },
    'gra': {
        'fir': .5,
        'wat': 2,
        'gra': .5,
        'poi': .5,
        'gro': 2,
        'fly': .5,
        'bug': .5,
        'roc': 2,
        'dra': .5,
        'stl': .5
    },
    'ice': {
        'fir': .5,
        'wat': .5,
        'gra': 2,
        'ice': .5,
        'gro': 2,
        'fly': 2,
        'dra': 2,
        'ste': .5
    },
    'fig': {
        'nor': 2,
        'ice': 2,
        'poi': .5,
        'fly': .5,
        'psy': .5,
        'bug': .5,
        'roc': 2,
        'gho': 0,
        'dar': 2,
        'ste': 2,
        'fai': .5
    },
    'poi': {
        'gra': 2,
        'poi': .5,
        'gro': .5,
        'roc': .5,
        'gho': .5,
        'ste': 0,
        'fai': 2
    },
    'gro': {
        'fir': 2,
        'ele': 2,
        'gra': .5,
        'poi': 2,
        'fly': 0,
        'bug': .5,
        'roc': 2,
        'ste': 2
    },
    'fly': {
        'ele': .5,
        'gra': 2,
        'fig': 2,
        'bug': 2,
        'roc': .5,
        'ste': .5
    },
    'psy': {
        'fig': 2,
        'poi': 2,
        'bug': .5,
        'dar': 0,
        'ste': .5
    },
    'bug': {
        'fir': .5,
        'gra': 2,
        'fig': .5,
        'poi': .5,
        'fly': .5,
        'psy': 2,
        'gho': .5,
        'dar': 2,
        'ste': .5,
        'fai': .5
    },
    'roc': {
        'fir': 2,
        'ice': 2,
        'fig': .5,
        'gro': .5,
        'fly': 2,
        'bug': 2,
        'ste': .5
    },
    'gho': {
        'nor': 0,
        'psy': 2,
        'gho': 2,
        'dar': .5
    },
    'dra': {
        'dra': 2,
        'ste': .5,
        'fai': 0
    },
    'dar': {
        'fig': .5,
        'psy': 2,
        'gho': 2,
        'dar': .5,
        'fai': .5
    },
    'ste': {
        'fir': .5,
        'wat': .5,
        'ele': .5,
        'ice': 2,
        'roc': 2,
        'ste': .5,
        'fai': 2
    },
    'fai': {
        'fir': .5,
        'fig': 2,
        'poi': .5,
        'dra': 2,
        'dar': 2,
        'ste': .5
    }
}


class Pokemon:
    """
    A class used to represent a specific pokemon.
    Assume level 100, no IVs, no EVs, no abilties
    Only Kanto dex
    """

    def __init__(self, species, moveslot, item=None, hp=None, status=None):
        """
        Initializes the pokmeon
        :param species: a string representing the pokemon speccies
        :param moveslot: a list of 4 moves
        :param item: a string reprenting the pokemon's held item (leftovers, life orb, choice items)
        :param hp: a float between 0 and 100 representing the health of the pokemon
        :param status: a string representing the status (burn, sleep, etc.) of a pokemon
        """
        self._alive = True
        self._species = species
        self._moveslot = moveslot
        self._item = item
        self._original_item = item
        self._choiced = False
        self._status = status
        self._protect = None
        self._pro_con = None
        # Literally just for sleep
        if self._status == 'slp':
            self._slp_counter = 0
            self._slp_len = random.randint(1, 3)
        else:
            self._slp_counter = None
            self._slp_len = None
        self._tox_counter = None
        self._confused = None
        self._con_counter = None
        self._con_len = None
        self._flinch = None
        self._leech = None
        self._sub = None
        # retrives info from pokedex
        self._typing = pokedex[species]['typing']
        if hp is not None:
            self._hp = (pokedex[species]['health'] * 2 + 110) * int(hp)
        else:
            self._hp = pokedex[species]['health'] * 2 + 110
        self._atk = pokedex[species]['atk'] * 2 + 5
        if item == 'choice band':
            self._atk += (pokedex[species]['atk'] * 2 + 5) / 2
        self._def = pokedex[species]['def'] * 2 + 5
        self._spatk = pokedex[species]['spatk'] * 2 + 5
        if item == 'choice specs':
            self._atk += (pokedex[species]['spatk'] * 2 + 5) / 2
        self._spdef = pokedex[species]['spdef'] * 2 + 5
        self._spd = pokedex[species]['spd'] * 2 + 5
        if item == 'choice scarf':
            self._spd += (pokedex[species]['spd'] * 2 + 5) / 2
        self._acc = 100
        self._eva = 100
        self._movepp = {
            moveslot[0]: move_info[moveslot[0]]['pp'],
            moveslot[1]: move_info[moveslot[1]]['pp'],
            moveslot[2]: move_info[moveslot[2]]['pp'],
            moveslot[3]: move_info[moveslot[3]]['pp']
        }

    def get_stats(self):
        """
        Retrieves the stats of the Pokemon
        :return: a dictionary of stats
        """
        return {
            'species': self._species,
            'alive': self._alive,
            'typing': self._typing,
            'status': self._status,
            'item': self._item,
            'hp': self._hp,
            'atk': self._atk,
            'def': self._def,
            'spatk': self._spatk,
            'spdef': self._spdef,
            'spd': self._spd,
            'acc': self._acc,
            'eva': self._eva,
            'sub': self._sub
        }

    def get_moves(self):
        """
        Retrieves the Pokemon's movelist and pp
        :return: a dictionary with keys being the moves and the values being their pp
        """
        return self._movepp

    def healthbar(self):
        """
        Shows the Pokemon's health bar
        :return: a float representing the percentage of the pokemon's remaining health
        """
        percent_health = 100 * self._hp / (pokedex[self._species]['health'] * 2 + 110)
        print(self._species + ' has ' + str(int(percent_health)) + '% hp remaining')
        return percent_health

    def passive_dmg(self, target=None):
        """
        Calculates and applies passive hp damage from burns and poisons
        ":param target: a target pokemon (literally just for leech seed)
        :return: a modified Pokemon object with the aforementioned hp changes
        """
        if not self._alive:
            return
        # Damage from status
        passive_dps = 0
        # DPS from burn or poison
        if self._status == 'bur' or self._status == 'poi':
            passive_dps = (pokedex[self._species]['health'] * 2 + 110) / 16
            if self._status == 'bur':
                print(self._species + ' lost ' + str(int(100 / 16)) + '% from its burn')
            if self._status == 'poi':
                print(self._species + ' lost ' + str(int(100 / 16)) + '% from poison')
        # DPS from toxic
        if self._status == 'tox':
            self._tox_counter += 1
            passive_dps = self._tox_counter * (pokedex[self._species]['health'] * 2 + 110) / 16
            print(self._species + ' lost ' + str(int(self._tox_counter * 100 / 16)) + '% from poison')
        self._hp -= passive_dps
        if self._hp <= 0:
            self._alive = False
            self._hp = 0
            print(self._species + ' fainted')
            return
        # For leech seed
        if self._leech:
            self._hp -= (pokedex[self._species]['health'] * 2 + 110) / 8
            target.mod_stat('leech', (pokedex[target.get_stats()['species']]['health'] * 2 + 110) / 8)
            print(self._species + "'s health was drained")
            if self._hp <= 0:
                self._alive = False
                self._hp = 0
                print(self._species + ' fainted')
                return
        # For Leftovers
        if self._item == 'leftovers':
            self._hp += (pokedex[self._species]['health'] * 2 + 110) / 16
            print(self._species + ' restored a little bit of health from its leftovers')
            if self._hp > (pokedex[self._species]['health'] * 2 + 110):
                self._hp = (pokedex[self._species]['health'] * 2 + 110)
        if self._protect is None:
            self._pro_con = None
        if self._protect is not None:
            self._protect = None
            self._pro_con += 1

    def mod_stat(self, stat, stage=1):
        """
        Modifies the stats/status of the pokemon when TARGETED by another
        :param stat: the hp/status/stats of the pokemon
        :param stage: the stage of the stat change
        :return: new updated stat values
        """
        # Leech seed health regen
        if stat == 'leech':
            self._hp += stage
            if self._hp > (pokedex[self._species]['health'] * 2 + 110):
                self._hp = pokedex[self._species]['health'] * 2 + 110
            return
        # Take Damage
        if stat == 'hp':
            if self._protect is not None:
                print(self._species + " protected itself")
            # substitute exception clause
            elif self._sub is not None:
                if self._sub - stage <= 0:
                    self._sub = None
                    print(self._species + "'s substitute was broken")
                else:
                    self._sub -= stage
                    print(self._species + "'s substitute absorbed the damage for it")
            else:
                lost_percent = 100 * (stage) / (pokedex[self._species]['health'] * 2 + 110)
                if lost_percent < 100:
                    print(self._species + ' lost: ' + str(int(lost_percent)) + '%')
                if lost_percent > 100:
                    print(self._species + ' lost: 100%')
                self._hp = self._hp - stage
                if self._hp <= 0:
                    self._hp = 0
                    self._alive = False
                    print(self._species + ' fainted!')
                return
        # Status
        if stat == 'par' or \
                stat == 'slp' or \
                stat == 'fre' or \
                stat == 'bur' or \
                stat == 'poi' or \
                stat == 'tox':
            if not self._alive:
                pass
            elif self._protect is not None:
                print(self._species + " protected itself")
            elif self._status is not None:
                print(self._species + ' already has a status condition')
            elif self._sub is not None:
                print(self._species + "'s substitute absorbed its status")
            else:
                self._status = stat
                if stat == 'slp':
                    self._slp_counter = 0
                    self._slp_len = random.randint(1, 3)
                    print(self._species + ' fell asleep')
                if stat == 'par':
                    print(self._species + ' was paralyzed')
                if stat == 'fre':
                    print(self._species + ' was frozen')
                if stat == 'bur':
                    print(self._species + ' was burned')
                if stat == 'poi':
                    print(self._species + ' was poisoned')
                if stat == 'tox':
                    self._tox_counter = 0
                    print(self._species + ' was badly poisoned')
            return
        # Confusion
        if stat == 'con' and self._confused is not None:
            if self._protect is not None:
                print(self._species + " protected itself")
            elif self._sub is not None:
                print(self._species + "'s substitute absorbed its status")
                return
            self._confused = True
            self._con_counter = 0
            self._con_len = random.randint(2, 5)
            print(self._species + ' was confused')
            return
        # Flinch
        if stat == 'fli' and self._flinch is not None:
            if self._protect is not None:
                print(self._species + " protected itself")
            elif self._sub is not None:
                print(self._species + "'s substitute absorbed its status")
                return
            self._flinch = True
            return
        # Applies leech seed
        if stat == 'lee':
            if self._protect is not None:
                print(self._species + " protected itself")
            elif self._leech:
                print(self._species + ' is already seeded')
            elif self._sub is not None:
                print(self._species + "'s substitute absorbed its status")
            else:
                self._leech = True
            return
        # Losing item
        if stat == 'knocked':
            if self._protect is not None:
                print(self._species + " protected itself")
            elif self._sub is not None:
                print(self._species + "'s substitute protected it")
                return
            if self._item == 'choice band':
                self._atk -= 1 / 3 * (pokedex[self._species]['atk'] * 2 + 5)
            if self._item == 'choice specs':
                self._spatk -= 1 / 3 * (pokedex[self._species]['spatk'] * 2 + 5)
            if self._item == 'choice scarf':
                self._spd -= 1 / 3 * (pokedex[self._species]['spd'] * 2 + 5)
            self._item = None
            self._choiced = False
            return
        # Stat modification
        # Positive
        if stage > 0:
            if stat == 'atk':
                self._atk += stage * ((pokedex[self._species]['atk'] * 2 + 5) / 2)
                print('Attack rose by ' + str(stage))
            if stat == 'def':
                self._def += stage * ((pokedex[self._species]['def'] * 2 + 5) / 2)
                print('Defense rose by ' + str(stage))
            if stat == 'spatk':
                self._spatk += stage * ((pokedex[self._species]['spatk'] * 2 + 5) / 2)
                print('Special Attack rose by ' + str(stage))
            if stat == 'spdef':
                self._spdef += stage * ((pokedex[self._species]['spdef'] * 2 + 5) / 2)
                print('Special Defense rose by ' + str(stage))
            if stat == 'spd':
                self._spd += stage * ((pokedex[self._species]['spd'] * 2 + 5) / 2)
                print('Speed rose by ' + str(stage))
            if stat == 'acc':
                self._acc += stage * 100 / 3
                print('Accuracy rose by ' + str(stage))
            if stat == 'eva':
                self._eva += stage * 100 / 3
                print('Evasiveness rose by ' + str(stage))
            return
        # Negative
        if stage < 0:
            if stat == 'atk':
                self._atk -= (1 - 2 / (2 - stage)) * (pokedex[self._species]['atk'] * 2 + 5)
                print('Attack fell by ' + str(-stage))
            if stat == 'def':
                self._def -= (1 - 2 / (2 - stage)) * (pokedex[self._species]['atk'] * 2 + 5)
                print('Defense fell by ' + str(-stage))
            if stat == 'spatk':
                self._spatk -= (1 - 2 / (2 - stage)) * (pokedex[self._species]['atk'] * 2 + 5)
                print('Special fell rose by ' + str(-stage))
            if stat == 'spdef':
                self._spdef -= (1 - 2 / (2 - stage)) * (pokedex[self._species]['atk'] * 2 + 5)
                print('Special Defense fell by ' + str(-stage))
            if stat == 'spd':
                self._spd -= (1 - 2 / (2 - stage)) * (pokedex[self._species]['atk'] * 2 + 5)
                print('Speed fell by ' + str(-stage))
            if stat == 'acc':
                self._acc -= (1 - 3 / (3 - stage)) * 100
                print('Accuracy fell by ' + str(-stage))
            if stat == 'eva':
                self._eva -= (1 - 3 / (3 - stage)) * 100
                print('Evasiveness fell by ' + str(-stage))
            return

    def turn(self, target, move):
        """
        Calculates the damage a pokemon takes when attacked
        :param target: another pokemon object
        :param move: a string representing the move you're attacking with
        :return: modifies the current pokemon's hp/stats/status
        """
        # Checks if alive
        if not self._alive:
            print(self._species + ' is unable to battle')
            return self._species + ' is unable to battle'
        # Sleep
        if self._status == "slp":
            self._slp_counter += 1
            if self._slp_counter == self._slp_len:
                self._status = None
                self._slp_counter = None
                self._slp_len = None
                print(self._species + ' woke up')
            else:
                print(self._species + ' is asleep')
                return self._species + ' is asleep'
        # Freeze
        elif self._status == 'fre':
            fre_rate = random.randint(0, 4)
            if fre_rate == 0:
                self._status = None
                print(self._species + ' has unfrozen')
                print(self._species + ' used ' + move)
            elif move_info[move]['typing'] == 'fir' and move_info[move]['pwr'] is not None:
                self._status = None
                print(self._species + ' has unfrozen')
                print(self._species + ' used ' + move)
            else:
                print(self._species + ' is frozen')
                return self._species + ' is frozen'
        # Flinch
        elif self._flinch:
            if self._spd < target.get_stats()['spd']:
                print(self._species + ' flinched')
                return self._species + ' flinched'
        # Paralyze
        elif self._status == 'par':
            para_rate = random.randint(0, 3)
            if para_rate == 0:
                print(self._species + ' is fully paralyzed')
                return self._species + ' is fully paralyzed'
            else:
                print(self._species + ' used ' + move)
        # Confusion
        elif self._confused:
            self._con_counter += 1
            if self._con_counter == self._con_len:
                self._confused = False
                self._con_counter = 0
                self._con_len = None
                print(self._species + ' snapped out of confusion')
            else:
                con_chance = random.randint(0, 2)
                if con_chance == 0:
                    dmg = ((42 * 40 * (self._atk / self._def)) / 50) \
                          * (random.randint(85, 100) / 100)
                    self._hp -= dmg
                    if self._hp <= 0:
                        self._hp = 0
                        self._alive = False
                        print(self._species + ' hurt itself in confusion')
                        print(self._species + ' fainted!')
                        return self._species + ' fainted!'
                    else:
                        print(self._species + ' hurt itself in confusion')
                        return self._species + ' hurt itself in confusion'
                else:
                    print(self._species + ' used ' + move)
        # Checks pp
        for possible_move, pp in self._movepp.items():
            if move == possible_move:
                if pp <= 0:
                    print(self._species + ' is out of PP')
                    print(self._species + ' used struggle')
                    # Calcs roll
                    roll = random.randint(85, 100) / 100
                    if roll < .9:
                        print('Low roll')
                    elif roll > .95:
                        print('High roll')
                    else:
                        print("Medium roll")
                    # Calcs crits
                    crit_chance = random.randint(0, 23)
                    crit_mult = 1
                    if crit_chance == 0:
                        crit_mult = 1.5
                        func_def = pokedex[target.get_stats()['species']]['def'] * 2 + 5
                        print('Critical hit')
                    else:
                        func_def = target.get_stats()['def']
                    # life orb amp
                    orb_amp = 1
                    if self._item == 'life orb':
                        orb_amp = 1.3
                    # Calcs burns
                    burn_mult = 1
                    if self._status == 'bur':
                        burn_mult = .5
                    dmg = ((42 * 50 * (self._atk / func_def)) / 50 + 2) \
                          * crit_mult * roll * orb_amp * burn_mult
                    target.mod_stat('hp', dmg)
                    print(self._species + ' took recoil')
                    self._hp -= dmg * 1 / 4
                    if self._hp <= 0:
                        self._hp = 0
                        self._alive = False
                        print(self._species + ' fainted!')
                    return self._species + ' is out of PP'
                else:
                    self._movepp[possible_move] = pp - 1
        else:
            print(self._species + ' used ' + move)
        # Miss
        if move_info[move]['acc'] is not None:
            miss_rate = random.randint(0, 100)
            if miss_rate > (100 * move_info[move]['acc'] * self._acc / target.get_stats()['eva']):
                print(self._species + ' missed')
                if move == 'high jump kick':
                    print(self._species + ' kept going and crashed')
                    self.mod_stat('hp', (pokedex[self._species]['health'] * 2 + 110) / 2)
                return 'Miss'
        # Take Damage
        if move_info[move]['pwr'] is not None:
            # Calcs stab
            if move_info[move]['typing'] in self._typing:
                stab = 1.5
                print('Stab bonus')
            else:
                stab = 1
            # Calcs typing
            eff_mult = 1
            for i in range(len(target.get_stats()['typing'])):
                if target.get_stats()['typing'][i] in type_list[move_info[move]['typing']]:
                    eff_mult = eff_mult * type_list[move_info[move]['typing']][target.get_stats()['typing'][i]]
            print(str(eff_mult) + 'x effective')
            # Calcs roll
            roll = random.randint(85, 100) / 100
            if roll < .9:
                print('Low roll')
            elif roll > .95:
                print('High roll')
            else:
                print("Medium roll")
            # Calcs crits
            if 'att' in move_info[move].keys():
                if 'hi-crit' in move_info[move]['att'].keys():
                    if move_info[move]['att']['hi-crit'] == +1:
                        crit_chance = random.randint(0, 7)
                    if move_info[move]['att']['hi-crit'] == +2:
                        crit_chance = random.randint(0, 1)
            else:
                crit_chance = random.randint(0, 23)
            crit_mult = 1
            if crit_chance == 0:
                crit_mult = 1.5
                func_def = pokedex[target.get_stats()['species']]['def'] * 2 + 5
                func_spdef = pokedex[target.get_stats()['species']]['def'] * 2 + 5
                print('Critical hit')
            else:
                func_def = target.get_stats()['def']
                func_spdef = target.get_stats()['spdef']
            # life orb amp
            orb_amp = 1
            if self._item == 'life orb':
                orb_amp = 1.3
            # Physical-Special split
            # Physical
            if move_info[move]['side'] == 'phy':
                # Calcs burns
                burn_mult = 1
                if self._status == 'bur':
                    burn_mult = .5
                dmg = ((42 * move_info[move]['pwr'] * (self._atk / func_def)) / 50 + 2) * \
                      stab * crit_mult * roll * eff_mult * orb_amp * burn_mult
                if target.get_stats()['sub'] is not None and \
                        dmg >= ((pokedex[target.get_stats()['species']]['health'] * 2 + 110) / 4):
                    dmg = (pokedex[target.get_stats()['species']]['health'] * 2 + 110) / 4
            if move_info[move]['side'] == 'spe':
                dmg = ((42 * move_info[move]['pwr'] * (self._spatk / func_spdef)) / 50 + 2) * \
                      stab * crit_mult * roll * eff_mult * orb_amp
                if target.get_stats()['sub'] is not None and \
                        dmg >= ((pokedex[target.get_stats()['species']]['health'] * 2 + 110) / 4):
                    dmg = (pokedex[target.get_stats()['species']]['health'] * 2 + 110) / 4
            # Applies Damage
            target.mod_stat('hp', dmg)
        # Status effect
        if move_info[move]['status_eff'] is not None:
            # Miss
            miss_rate = random.randint(0, 100)
            if miss_rate < (move_info[move]['status_eff'][1] * 100) or \
                    (move_info[move]['status_eff'][1] is None):
                # Makes sure grass statuses can't hit grass types
                if (move_info[move]['typing'] == 'gra') and \
                        ('gra' in target.get_stats()['typing']):
                    print("It doesn't affect " + target.get_stats()['species'])
                # Can't poison steel and poison types
                elif (move_info[move]['status_eff'][0] == 'poi') and ('ste' in target.get_stats()['typing'] or
                                                                      'poi' in target.get_stats()['typing']):
                    print("It doesn't affect " + target.get_stats()['species'])
                # Can't burn fire types
                elif (move_info[move]['status_eff'][0] == 'bur') and ('fir' in target.get_stats()['typing']):
                    print("It doesn't affect " + target.get_stats()['species'])
                # Can't paralyze electric and ground types:
                elif (move_info[move]['typing'] == 'ele') and \
                        ('gro' in target.get_stats()['typing'] or 'ele' in target.get_stats()['typing']):
                    print("It doesn't affect " + target.get_stats()['species'])
                elif (move_info[move]['status_eff'][0] == 'par') and ('ele' in target.get_stats()['typing']):
                    print("It doesn't affect " + target.get_stats()['species'])
                # tri attack exception
                elif move_info[move]['status_eff'][0] == 'tri':
                    tri = random.randint(0, 2)
                    if tri == 0 and ('fir' not in target.get_stats()['typing']):
                        target.mod_stat('bur', 0)
                    if tri == 1 and 'ele' not in target.get_stats()['typing']:
                        target.mod_stat('par', 0)
                    if tri == 2 and 'ice' not in target.get_stats()['typing']:
                        target.mod_stat('fre', 0)
                # Applies
                else:
                    target.mod_stat(move_info[move]['status_eff'][0], 0)
        # Stat modifier
        if move_info[move]['stat_eff'] is not None:
            # In case of multiple stat changes
            for stat_eff in move_info[move]['stat_eff']:
                if stat_eff[2] is not None:
                    # Calculates miss chance
                    miss_rate = random.randint(0, 100)
                    if miss_rate > (stat_eff[2] * 100):
                        pass
                # self stat change
                if stat_eff[3] == 'self':
                    self.mod_stat(stat_eff[0], stat_eff[1])
                # If on target
                if stat_eff[3] == 'target':
                    if target.get_stats()['sub'] is not None and (stat_eff[2] < 0):
                        print(target.get_stats()['species'] + "'s substitute protected it")
                    else:
                        target.mod_stat(stat_eff[0], stat_eff[2])
        # Applies recoil
        if move_info[move]['recoil'] is not None:
            if not self._alive:
                print(self._species + ' is unable to battle')
                return self._species + ' is unable to battle'
            # Traditional damage recoil
            if move_info[move]["recoil"][0] == 'dmg':
                print(self._species + ' took recoil')
                self._hp -= dmg * move_info[move]['recoil'][1]
                if self._hp <= 0:
                    self._hp = 0
                    self._alive = False
                    print(self._species + ' fainted!')
            if move_info[move]['recoil'][0] == 'death':
                self._hp = 0
                self._alive = False
                print(self._species + ' lost: 100%')
                print(self._species + ' fainted!')
            # Loophole for heals
            if move_info[move]['recoil'][0] == 'heal':
                if move_info[move]['recoil'][1] == 'half':
                    healing = (pokedex[self._species]['health'] * 2 + 110) / 2
                    print(self._species + ' health was restored')
                else:
                    healing = self._hp + dmg * move_info[move]['recoil'][1]
                    print(self._species + ' was slightly healed')
                if healing > (pokedex[self._species]['health'] * 2 + 110):
                    self._hp = pokedex[self._species]['health'] * 2 + 110
                else:
                    self._hp = healing
            # status
            if move_info[move]['recoil'][0] == 'status':
                self.mod_stat(move_info[move]['recoil'][1])
            # rest loophole
            if move_info[move]['recoil'][0] == 'rest':
                self._hp = pokedex[self._species]['health'] * 2 + 110
                self._status = 'slp'
                self._slp_counter = 0
                self._slp_len = random.randint(1, 3)
                print(self._species + ' fell asleep but was restored to full health')
        # Life orb recoil
        if self._item == 'life orb':
            if not self._alive:
                print(self._species + ' is unable to battle')
                return self._species + ' is unable to battle'
            if move_info[move]['pwr'] is not None:
                print(self._species + ' lost some health to its life orb')
                self._hp -= (pokedex[self._species]['health'] * 2 + 110) / 10
                if self._hp <= 0:
                    self._hp = 0
                    self._alive = False
                    print(self._species + ' fainted!')
        # Substitute
        if move == 'substitute':
            if self._sub is None and (self._hp >= (pokedex[self._species]['health'] * 2 + 110) / 4):
                self._sub = (pokedex[self._species]['health'] * 2 + 110) / 4
                self._hp -= self._sub
            else:
                print(self._species + ' cannot form a substitute')
        # Protect
        if move == 'protect':
            if self._pro_con is None:
                self._protect = True
                self._pro_con = 0
            else:
                if self._pro_con == 1:
                    if random.randint(0, 1) == 0:
                        self._protect = True
                    else:
                        print('But it failed')
                else:
                    if random.randint(0, 2 ** self._pro_con - 1) == 0:
                        self._protect = True
                    else:
                        print('But it failed')

    def choose_move(self, decision):
        """
        Choose move
        :param decision: a string either 'manual' or 'random', depending on how you want the move to be chosen
        :return: a possible move from the Pokemon's movepool
        """
        if not self._choiced:
            # Totally random
            if decision == 'random':
                while True:
                    rand_select = random.randint(0, 3)
                    counter = 0
                    for move in self._moveslot:
                        if rand_select == counter:
                            move_select = move
                            break
                        counter += 1
                    if self._movepp[move_select] > 0:
                        break
            # You choose
            if decision == 'manual':
                print('*****')
                print('Type ' + self._species + "'s move: " + str(self._moveslot))
                manual_select = input()
                while manual_select not in self._moveslot:
                    print('Make sure you type a valid move')
                    manual_select = input()
                move_select = manual_select
        else:
            move_select = self._choiced
        if (self._item == 'choice band') or (self._item == 'choice specs') or (self._item == 'choice scarf'):
            self._choiced = move_select
        return move_select

    def reset(self):
        """
        Resets the pokemon to full health and no status condition
        :return: pokemon to initial values
        """
        self._alive = True
        self._hp = pokedex[self._species]['health'] * 2 + 110
        self._atk = pokedex[self._species]['atk'] * 2 + 5
        if self._original_item == 'choice band':
            self._atk += (pokedex[self._species]['atk'] * 2 + 5) / 2
        self._def = pokedex[self._species]['def'] * 2 + 5
        self._spatk = pokedex[self._species]['spatk'] * 2 + 5
        if self._original_item == 'choice specs':
            self._spatk += (pokedex[self._species]['spatk'] * 2 + 5) / 2
        self._spdef = pokedex[self._species]['spdef'] * 2 + 5
        self._spd = pokedex[self._species]['spd'] * 2 + 5
        if self._original_item == 'choice scarf':
            self._spd += (pokedex[self._species]['spd'] * 2 + 5) / 2
        self._acc = 100
        self._eva = 100
        for move in self._moveslot:
            self._movepp[move] = move_info[move]['pp']
        self._status = None
        self._slp_counter = 0
        self._slp_len = None
        self._confused = None
        self._con_counter = None
        self._con_len = None
        self._flinch = None
        self._leech = None
        self._item = copy.deepcopy(self._original_item)
        self._choiced = False
        self._sub = None
        self._protect = None
        self._pro_con = None


def calc_speed(pokemon1, move1, pokemon2, move2):
    """
    Returns which Pokemon should move first in a given turn
    :param pokemon1: a pokemon object
    :param move1: a string of what move pokemon1 will perform
    :param pokemon2: another pokemon object
    :param move2: a string of what move pokemon2 will perform
    :return: pokemon1 or pokemon2 depending on which one should move first
    """
    prio1 = 0
    prio2 = 0
    # Finds prioity
    if 'att' in move_info[move1].keys():
        if 'pri' in move_info[move1]['att']:
            prio1 = move_info[move1]['att']['pri']
    if 'att' in move_info[move2].keys():
        if 'pri' in move_info[move2]['att']:
            prio2 = move_info[move2]['att']['pri']
    # Calculates priority
    if prio1 > prio2:
        return 'pokemon1'
    if prio2 > prio1:
        return 'pokemon2'
    # Normal speed
    else:
        if pokemon1.get_stats()['spd'] > pokemon2.get_stats()['spd']:
            return 'pokemon1'
        if pokemon2.get_stats()['spd'] > pokemon1.get_stats()['spd']:
            return 'pokemon2'
        else:
            # If speed tie
            if random.randint(0, 1) == 0:
                return 'pokemon1'
            else:
                return 'pokemon2'


def mock_battle(pokemon1, pokemon2, trials):
    """
    Does a simulated mock singles battle. NOTE: Totally random and unoptimized.
    :param pokemon1: a complete pokemon object
    :param pokemon2: another complete pokemon object
    :param trials: an integer representing the number of battles
    :return: the winner and their winrate
    """
    pokemon1_wins = 0
    pokemon2_wins = 0
    battle_num = 0
    for battle in range(trials):
        battle_num += 1
        print('BATTLE: ' + str(battle_num))
        turn_num = 0
        while True:
            turn_num += 1
            print('')
            print('TURN: ' + str(turn_num))
            # Looks through move pool
            rand_select1 = random.randint(0, 3)
            rand_select2 = random.randint(0, 3)
            counter1 = 0
            for move in pokemon1.get_moves().keys():
                if counter1 == rand_select1:
                    move_select1 = move
                    break
                counter1 += 1
            counter2 = 0
            for move in pokemon2.get_moves().keys():
                if counter2 == rand_select2:
                    move_select2 = move
                    break
                counter2 += 1
            # Calcs speed tier
            if pokemon1.get_stats()['spd'] > pokemon2.get_stats()['spd']:
                pokemon1.turn(pokemon2, move_select1)
                pokemon2.turn(pokemon1, move_select2)
                pokemon1.passive_dmg(pokemon2)
                pokemon2.passive_dmg(pokemon1)
                print('-----')
                pokemon1.healthbar()
                pokemon2.healthbar()
                print('-----')
            if pokemon2.get_stats()['spd'] > pokemon1.get_stats()['spd']:
                pokemon2.turn(pokemon1, move_select2)
                pokemon1.turn(pokemon2, move_select1)
                pokemon2.passive_dmg(pokemon1)
                pokemon1.passive_dmg(pokemon2)
                print('-----')
                pokemon2.healthbar()
                pokemon1.healthbar()
                print('-----')
            if not pokemon1.get_stats()['alive']:
                pokemon2_wins += 1
                print(pokemon2.get_stats()['species'] + ' Wins!!')
                print('======================')
                pokemon1.reset()
                pokemon2.reset()
                print('RESPAWN')
                break
            if not pokemon2.get_stats()['alive']:
                pokemon1_wins += 1
                print(pokemon1.get_stats()['species'] + ' Wins!!')
                print('======================')
                pokemon1.reset()
                pokemon2.reset()
                print('RESPAWN')
                break
    print('======================')
    print('======================')
    print('MATCH IS OVER')
    print('======================')
    print('======================')
    print('======================')
    if pokemon1_wins > pokemon2_wins:
        return pokemon1.get_stats()['species'] + ' won with a winrate of ' + str(pokemon1_wins / trials)
    if pokemon2_wins > pokemon1_wins:
        return pokemon2.get_stats()['species'] + ' won with a winrate of ' + str(pokemon2_wins / trials)


def mock_battle_v2(pokemon1, pokemon2, decision, trials):
    """
    Does a simulated mock singles battle. NOTE: Totally random and unoptimized.
    :param pokemon1: a complete pokemon object
    :param pokemon2: another complete pokemon object
    :param decision: a string either 'manual' or 'random', depending on how you want the move to be chosen
    :param trials: an integer representing the number of battles
    :return: the winner and their winrate
    """
    pokemon1_wins = 0
    pokemon2_wins = 0
    battle_num = 0
    for battle in range(trials):
        battle_num += 1
        print('BATTLE: ' + str(battle_num))
        turn_num = 0
        while True:
            turn_num += 1
            print('')
            print('TURN: ' + str(turn_num))
            # Choose move
            move_select1 = pokemon1.choose_move(decision)
            move_select2 = pokemon2.choose_move(decision)
            # Calcs speed tier
            if calc_speed(pokemon1, move_select1, pokemon2, move_select2) == 'pokemon1':
                pokemon1.turn(pokemon2, move_select1)
                pokemon2.turn(pokemon1, move_select2)
                pokemon1.passive_dmg(pokemon2)
                pokemon2.passive_dmg(pokemon1)
                print('-----')
                pokemon1.healthbar()
                pokemon2.healthbar()
                print('-----')
            elif calc_speed(pokemon1, move_select1, pokemon2, move_select2) == 'pokemon2':
                pokemon2.turn(pokemon1, move_select2)
                pokemon1.turn(pokemon2, move_select1)
                pokemon2.passive_dmg(pokemon1)
                pokemon1.passive_dmg(pokemon2)
                print('-----')
                pokemon2.healthbar()
                pokemon1.healthbar()
                print('-----')
            if not pokemon1.get_stats()['alive'] and not pokemon2.get_stats()['alive']:
                print("Double K.O: It's a tie ")
                print('======================')
                pokemon1.reset()
                pokemon2.reset()
                print('RESPAWN')
                break
            elif not pokemon1.get_stats()['alive']:
                pokemon2_wins += 1
                print(pokemon2.get_stats()['species'] + ' Wins!!')
                print('======================')
                pokemon1.reset()
                pokemon2.reset()
                print('RESPAWN')
                break
            elif not pokemon2.get_stats()['alive']:
                pokemon1_wins += 1
                print(pokemon1.get_stats()['species'] + ' Wins!!')
                print('======================')
                pokemon1.reset()
                pokemon2.reset()
                print('RESPAWN')
                break
    print('======================')
    print('======================')
    print('MATCH IS OVER')
    print('======================')
    print('======================')
    print('======================')
    if pokemon1_wins > pokemon2_wins:
        return pokemon1.get_stats()['species'] + ' won with a winrate of ' + str(pokemon1_wins / trials)
    if pokemon2_wins > pokemon1_wins:
        return pokemon2.get_stats()['species'] + ' won with a winrate of ' + str(pokemon2_wins / trials)


def predict_outcomes(pokemon1, pokemon2, trials):
    """
    Iterates through and looks at every possible combination of moves and evaluates its odds of winning
    :param pokemon1: a pokemon object
    :param pokemon2: another pokemon object
    :param trials: number of trials run
    :return: a dictionary with each of pokemon1's known move combinations with its values being
    another nested dictionary with each of pokemon2's move combinations and with keys equaling the winrate
    """
    transcript = {}
    wins_loss_ties = {
        'win': 0,
        'loss': 0,
        'tie': 0
    }
    for battle in range(trials):
        poke1_combo = []
        poke2_combo = []
        while True:
            # Choose move
            move_select1 = pokemon1.choose_move('random')
            poke1_combo.append(move_select1)
            move_select2 = pokemon2.choose_move('random')
            poke2_combo.append(move_select2)
            # Calcs speed tier
            if calc_speed(pokemon1, move_select1, pokemon2, move_select2) == 'pokemon1':
                pokemon1.turn(pokemon2, move_select1)
                pokemon2.turn(pokemon1, move_select2)
                pokemon1.passive_dmg(pokemon2)
                pokemon2.passive_dmg(pokemon1)
            elif calc_speed(pokemon1, move_select1, pokemon2, move_select2) == 'pokemon2':
                pokemon2.turn(pokemon1, move_select2)
                pokemon1.turn(pokemon2, move_select1)
                pokemon2.passive_dmg(pokemon1)
                pokemon1.passive_dmg(pokemon2)
            if not pokemon1.get_stats()['alive'] and not pokemon2.get_stats()['alive']:
                combo1 = tuple(poke1_combo)
                combo2 = tuple(poke2_combo)
                if combo1 not in transcript.keys():
                    transcript[combo1] = {}
                    transcript[combo1][combo2] = copy.deepcopy(wins_loss_ties)
                    transcript[combo1][combo2]['tie'] += 1
                elif combo2 not in transcript[combo1].keys():
                    transcript[combo1][combo2] = copy.deepcopy(wins_loss_ties)
                    transcript[combo1][combo2]['tie'] += 1
                else:
                    transcript[combo1][combo2]['tie'] += 1
                pokemon1.reset()
                pokemon2.reset()
                break
            elif not pokemon1.get_stats()['alive']:
                combo1 = tuple(poke1_combo)
                combo2 = tuple(poke2_combo)
                if combo1 not in transcript.keys():
                    transcript[combo1] = {}
                    transcript[combo1][combo2] = copy.deepcopy(wins_loss_ties)
                    transcript[combo1][combo2]['loss'] += 1
                elif combo2 not in transcript[combo1].keys():
                    transcript[combo1][combo2] = copy.deepcopy(wins_loss_ties)
                    transcript[combo1][combo2]['loss'] += 1
                else:
                    transcript[combo1][combo2]['loss'] += 1
                pokemon1.reset()
                pokemon2.reset()
                break
            elif not pokemon2.get_stats()['alive']:
                combo1 = tuple(poke1_combo)
                combo2 = tuple(poke2_combo)
                if combo1 not in transcript.keys():
                    transcript[combo1] = {}
                    transcript[combo1][combo2] = copy.deepcopy(wins_loss_ties)
                    transcript[combo1][combo2]['win'] += 1
                elif combo2 not in transcript[combo1].keys():
                    transcript[combo1][combo2] = copy.deepcopy(wins_loss_ties)
                    transcript[combo1][combo2]['win'] += 1
                else:
                    transcript[combo1][combo2]['win'] += 1
                pokemon1.reset()
                pokemon2.reset()
                break
    return transcript


def focused_prediction(pokemon1, pokemon2, move_choice, trials):
    '''
    Similiar to predict_outcomes, but focuses only on winning with a select strategy
    :param pokemon1: primary pokemon object
    :param pokemon2: secondary pokemon object
    :param move_choice: an ordered list of the moves you want the Pokemon1 to perform
    :param trials: number of choice
    :return: a transcript
    '''
    transcript = {}
    wins_loss_ties = {
        'win': 0,
        'loss': 0,
        'tie': 0
    }
    for battle in range(trials):
        poke1_combo = []
        poke2_combo = []
        current_move = 0
        while True:
            if current_move > len(move_choice) - 1:
                move_select1 = pokemon1.choose_move('random')
            else:
                move_select1 = move_choice[current_move]
            poke1_combo.append(move_select1)
            move_select2 = pokemon2.choose_move('random')
            poke2_combo.append(move_select2)
            # Calcs speed tier
            if calc_speed(pokemon1, move_select1, pokemon2, move_select2) == 'pokemon1':
                pokemon1.turn(pokemon2, move_select1)
                pokemon2.turn(pokemon1, move_select2)
                pokemon1.passive_dmg(pokemon2)
                pokemon2.passive_dmg(pokemon1)
            elif calc_speed(pokemon1, move_select1, pokemon2, move_select2) == 'pokemon2':
                pokemon2.turn(pokemon1, move_select2)
                pokemon1.turn(pokemon2, move_select1)
                pokemon2.passive_dmg(pokemon1)
                pokemon1.passive_dmg(pokemon2)
            if not pokemon1.get_stats()['alive'] and not pokemon2.get_stats()['alive']:
                combo1 = tuple(poke1_combo)
                combo2 = tuple(poke2_combo)
                if combo1 not in transcript.keys():
                    transcript[combo1] = {}
                    transcript[combo1][combo2] = copy.deepcopy(wins_loss_ties)
                    transcript[combo1][combo2]['tie'] += 1
                elif combo2 not in transcript[combo1].keys():
                    transcript[combo1][combo2] = copy.deepcopy(wins_loss_ties)
                    transcript[combo1][combo2]['tie'] += 1
                else:
                    transcript[combo1][combo2]['tie'] += 1
                pokemon1.reset()
                pokemon2.reset()
                break
            elif not pokemon1.get_stats()['alive']:
                combo1 = tuple(poke1_combo)
                combo2 = tuple(poke2_combo)
                if combo1 not in transcript.keys():
                    transcript[combo1] = {}
                    transcript[combo1][combo2] = copy.deepcopy(wins_loss_ties)
                    transcript[combo1][combo2]['loss'] += 1
                elif combo2 not in transcript[combo1].keys():
                    transcript[combo1][combo2] = copy.deepcopy(wins_loss_ties)
                    transcript[combo1][combo2]['loss'] += 1
                else:
                    transcript[combo1][combo2]['loss'] += 1
                pokemon1.reset()
                pokemon2.reset()
                break
            elif not pokemon2.get_stats()['alive']:
                combo1 = tuple(poke1_combo)
                combo2 = tuple(poke2_combo)
                if combo1 not in transcript.keys():
                    transcript[combo1] = {}
                    transcript[combo1][combo2] = copy.deepcopy(wins_loss_ties)
                    transcript[combo1][combo2]['win'] += 1
                elif combo2 not in transcript[combo1].keys():
                    transcript[combo1][combo2] = copy.deepcopy(wins_loss_ties)
                    transcript[combo1][combo2]['win'] += 1
                else:
                    transcript[combo1][combo2]['win'] += 1
                pokemon1.reset()
                pokemon2.reset()
                break
            current_move += 1
    return transcript


def eval_transcript(transcript, threshold, coverage):
    '''
    Looks at the transcript and returns the optimal strategy based on minimizing possibility of a loss
    :param transcript: a transcript of moves
    :param threshold: a float less than 1 representing the minimimum winrate you want the moveset to have against each possibility
    :param coverage: the amount of possibile counters you want the moveset to beat
    :return: a dictionary with each of the optimal strategies and their counters and average winrates
    '''
    good_moves = {}
    format_shit = {
        'avg winrate': None,
        'counters': None
    }
    for move_combo, i2 in transcript.items():
        good_end = 0
        possibilities = 0
        counters = []
        total_winrates = []
        for opp_combo, i3 in i2.items():
            total = 0
            wins = 0
            for outcome, quantity in i3.items():
                if outcome == 'win':
                    total += quantity
                    wins += quantity
                if outcome == 'loss':
                    total += quantity
            possibilities += 1
            if total == 0:
                total = 1
            total_winrates.append(wins / total)
            if wins / total > threshold:
                good_end += 1
            else:
                counters.append(opp_combo)
        if good_end / possibilities > coverage:
            print('==========================')
            print('Possible option: ' + str(move_combo))
            good_moves[move_combo] = copy.deepcopy(format_shit)
            divisor = 0
            dividend = 0
            for win_rate in total_winrates:
                divisor += 1
                dividend += win_rate
            good_moves[move_combo]['avg winrate'] = dividend / divisor
            print('     Average winrate: ' + str(dividend / divisor))
            print('     Possible counters: ' + str(counters))
            good_moves[move_combo]['counters'] = counters
    if good_moves == {}:
        print('==========================')
        print('Unwinnable')
    return good_moves


def best_move(transcript):
    """
    Determines the best possible move by finding the highest average winrate
    :param transcript: transcript
    :return: a tuple reppresenting the ordered list of "best" moves
    """
    good_moves = {}
    for move_combo, i2 in transcript.items():
        total_winrates = []
        for opp_combo, i3 in i2.items():
            total = 0
            wins = 0
            for outcome, quantity in i3.items():
                if outcome == 'win':
                    total += quantity
                    wins += quantity
                if outcome == 'loss':
                    total += quantity
            if total == 0:
                total = 1
            total_winrates.append(wins / total)
        divisor = 0
        dividend = 0
        for win_rate in total_winrates:
            divisor += 1
            dividend += win_rate
        good_moves[move_combo] = dividend / divisor
    highes_rate = 0
    for move, winrate in good_moves.items():
        if winrate > highes_rate:
            best = move
    return (best, highes_rate)


def rigor_analysis(pokemon1, pokemon2):
    """
    Does 100 trials to determine what the "best" possible move is through a 2 step process
        1. Randomly select moves and then filter through the move combinations with winrates higher than 60%
        2. Rigorously test the move combinations to find the singular move selection with the highest winrate
    :param pokemon1: primary Pokemon object
    :param pokemon2: secondary Pokemon object
    :return: the move options that would give pokemon1 the highest odds of winning
    """
    transcript1 = predict_outcomes(pokemon1, pokemon2, 100)
    pass_phase1 = eval_transcript(transcript1, .9, .9)
    optimal_winrate1 = 0
    optimal_move1 = None
    move_options = {}
    print('============================')
    print('============================')
    print('phase 1 over')
    print('============================')
    print('============================')
    print(move_options)
    for move_selection in pass_phase1.keys():
        transcript2 = focused_prediction(pokemon1, pokemon2, move_selection, 100)
        optimal_winrate2 = 0
        optimal_move2 = None
        move_winrate = best_move(transcript2)
        move_options[move_winrate[0]] = move_winrate[1]
    for move_selection1, winrate in move_options.items():
        if winrate > optimal_winrate1:
            optimal_winrate1 = winrate
            optimal_move1 = move_selection1
    return move_selection1, optimal_winrate1


def rigor_analysis_v2(pokemon1, pokemon2):
    """
    Does 100 trials to determine what the "best" possible move is through a 2 step process
        1. Randomly select moves and then filter through the move combinations with winrates higher than 60%
        2. Rigorously test the move combinations to find the singular move selection with the highest winrate
    :param pokemon1: primary Pokemon object
    :param pokemon2: secondary Pokemon object
    :return: the move options that would give pokemon1 the highest odds of winning
    """
    transcript1 = predict_outcomes(pokemon1, pokemon2, 1000)
    pass_phase1 = eval_transcript(transcript1, .9, .9)
    for move_selection in pass_phase1.keys():
        transcript2 = focused_prediction(pokemon1, pokemon2, move_selection, 1000)
        pass_phase2 = eval_transcript(transcript1, .9, .55)
    return pass_phase2


# GOD I HOPE THIS FUCKING WORKS
# print(mock_battle(Pokemon('bulbasaur', ['swords dance', 'fire punch', 'sleep powder', 'take down']), Pokemon('charmander', ['swords dance', 'fire punch', 'sleep powder', 'take down']), 100))
# print(mock_battle(Pokemon('charizard', ['swords dance', 'fire punch', 'sleep powder', 'take down']), Pokemon('blastoise', ['swords dance', 'toxic', 'sleep powder', 'take down']), 100))
'''
print(mock_battle_v2(Pokemon('charizard', ['swords dance', 'fire punch', 'substitute', 'take down'], 'leftovers'),
                     Pokemon('blastoise', ['swords dance', 'toxic', 'hydro pump', 'take down']),
                     'random', 10))
'''
'''
print(mock_battle_v2(Pokemon('charizard', ['swords dance', 'flamethrower', 'fire blast', 'fire punch'], 'life orb'),
                     Pokemon('venosaur', ['substitute', 'protect', 'leech seed', 'recover'], 'leftovers'),
                     'manual', 10))
'''
#test1 = predict_outcomes(Pokemon('charizard', ['swords dance', 'substitute', 'fire blast', 'take down'], 'life orb'),
                         #Pokemon('charizard', ['swords dance', 'substitute', 'fire blast', 'take down'], 'life orb'),
                         #10000)
#test1 = focused_prediction(Pokemon('charizard', ['swords dance', 'substitute', 'fire blast', 'take down'], 'life orb'),
                           #Pokemon('charizard', ['swords dance', 'substitute', 'fire blast', 'take down'], 'life orb'),
                           #['substitute', 'swords dance', 'take down', 'take down'],
                           #10000)
test1 = rigor_analysis_v2(Pokemon('charizard', ['swords dance', 'substitute', 'fire blast', 'take down'], 'life orb'),
                       Pokemon('charizard', ['swords dance', 'substitute', 'fire blast', 'take down'], 'life orb'))
print(test1)
#print(best_move(test1))

