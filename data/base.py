# data/base.py

BOX_INFO = {
    "id": "base",
    "name": "Boîte de Base Arcadia Quest",
    "image": "assets/images/boite_base.jpg",
    "description": "La boîte originale d'Arcadia Quest avec sa campagne en 11 scénarios."
}

HEROES = {
    'Maya': {
        'hp': 5, 'def': 1, 
        'ability': 'Magie', 
        'ability_desc': 'Capacité magique innée propre au personnage.',
        'image': 'assets/images/maya.jpg',
        'box': 'base'
    },
    'Grom': {
        'hp': 5, 'def': 1, 
        'ability': 'Berserker', 
        'ability_desc': 'Lance +1 dé à tous ses jets tant qu\'il est blessé.',
        'image': 'assets/images/grom.jpg',
        'box': 'base'
    },
    'Scarlet': {
        'hp': 5, 'def': 1, 
        'ability': 'Tir Précis', 
        'ability_desc': 'Permet d’ignorer les malus de distance ou de cibler un adversaire à travers une case occupée.',
        'image': 'assets/images/scarlet.jpg',
        'box': 'base'
    },
    'Seth': {
        'hp': 5, 'def': 1, 
        'ability': 'Fureur', 
        'ability_desc': 'Octroie une action de mouvement gratuite supplémentaire s’il élimine un monstre pendant son tour.',
        'image': 'assets/images/seth.jpg',
        'box': 'base'
    },
    'Dirk': {
        'hp': 5, 'def': 1, 
        'ability': 'Bataille', 
        'ability_desc': 'Permet de relancer un dé de défense blanc raté lors d’une attaque ennemie au corps à corps.',
        'image': 'assets/images/dirk.jpg',
        'box': 'base'
    },
    'Zazu': {
        'hp': 5, 'def': 1, 
        'ability': 'Esquive', 
        'ability_desc': 'Réduit d’un dé les attaques ennemies ciblant Zazu grâce à son agilité naturelle.',
        'image': 'assets/images/zazu.jpg',
        'box': 'base'
    },
    'Chubby': {
        'hp': 5, 'def': 2, 
        'ability': 'Robuste', 
        'ability_desc': 'Ignore le premier dégât reçu lors de chaque tour de jeu.',
        'image': 'assets/images/chubby.jpg',
        'box': 'base'
    },
    'Hilda': {
        'hp': 5, 'def': 1, 
        'ability': 'Soin Divin', 
        'ability_desc': 'Peut dépenser une action pour restaurer 1 PV à un héros allié adjacent sur le plateau.',
        'image': 'assets/images/hilda.jpg',
        'box': 'base'
    },
    'Bjorn': {
        'hp': 6, 'def': 1, 
        'ability': 'Puissance Berserk', 
        'ability_desc': 'Gagne un dé d’attaque supplémentaire lorsque ses PV tombent à 2 ou moins.',
        'image': 'assets/images/bjorn.jpg',
        'box': 'base'
    },
    'Krom': {
        'hp': 5, 'def': 2, 
        'ability': 'Coup Scénarisé', 
        'ability_desc': 'Inflige un dégât bonus aux sbires et boss liés aux objectifs du scénario en cours.',
        'image': 'assets/images/krom.jpg',
        'box': 'base'
    },
    'Wryn': {
        'hp': 5, 'def': 1, 
        'ability': 'Tir Multiple', 
        'ability_desc': 'Peut répartir ses dés d’attaque entre deux cibles différentes à distance.',
        'image': 'assets/images/wryn.jpg',
        'box': 'base'
    },
    'Dart': {
        'hp': 5, 'def': 2, 
        'ability': 'Agilité', 
        'ability_desc': 'Permet de traverser les cases occupées par des monstres sans subir d’attaque d’opportunité.',
        'image': 'assets/images/dart.jpg',
        'box': 'base'
    }
}

MONSTERS = {
    'Gobelin Archer': {'att': '2 Dés (Dist)', 'def': '1 Dé', 'hp': 2, 'ability': 'Tir à couvert', 'box': 'base'},
    'Orc Maraudeur': {'att': '3 Dés (CàC)', 'def': '2 Dés', 'hp': 3, 'ability': 'Charge', 'box': 'base'},
    'Sœur de la Douleur': {'att': '3 Dés (CàC)', 'def': '2 Dés', 'hp': 3, 'ability': 'Tourment', 'box': 'base'},
    'Sœur du Plaisir': {'att': '3 Dés (Magie)', 'def': '2 Dés', 'hp': 3, 'ability': 'Charme', 'box': 'base'},
    'Homme-Bête à Marteau': {'att': '4 Dés (CàC)', 'def': '2 Dés', 'hp': 4, 'ability': 'Écrasement', 'box': 'base'},
    'Homme-Bête à Lance': {'att': '3 Dés (CàC)', 'def': '3 Dés', 'hp': 4, 'ability': 'Allonge', 'box': 'base'},
    'Minotaure': {'att': '4 Dés (CàC)', 'def': '2 Dés', 'hp': 5, 'ability': 'Piétinement (Mini-Boss)', 'box': 'base'},
    'Troll': {'att': '4 Dés (CàC)', 'def': '3 Dés', 'hp': 6, 'ability': 'Régénération (Boss)', 'box': 'base'},
    'Capitaine Gobelin': {'att': '4 Dés (CàC)', 'def': '2 Dés', 'hp': 6, 'ability': 'Riposte (Boss)', 'box': 'base'},
    'Lord Fang': {'att': '5 Dés (CàC/Magie)', 'def': '3 Dés', 'hp': 8, 'ability': 'Seigneur Vampire (Grand Boss)', 'box': 'base'}
}

SCENARIOS = [
    {
        "name": "Scénario 1 : La Nuit Tombe (Outer Circle)", 
        "box": "base", 
        "boss": "Capitaine Gobelin",
        "description": "Les gobelins envahissent les rues de la cité. Vos guildes doivent sécuriser les points stratégiques avant la tombée de la nuit.",
        "monsters": ["Gobelin Archer", "Orc Maraudeur", "Capitaine Gobelin"]
    },
    {
        "name": "Scénario 2 : Pillage au Marché (Outer Circle)", 
        "box": "base", 
        "boss": "Minotaure",
        "description": "Le marché central regorge de trésors abandonnés. Emparez-vous-en avant vos rivaux tout en matant la bête féroce qui y rôde.",
        "monsters": ["Orc Maraudeur", "Sœur de la Douleur", "Minotaure"]
    },
    {
        "name": "Scénario 3 : Les Docks Endormis (Outer Circle)", 
        "box": "base", 
        "boss": "Troll",
        "description": "Les entrepôts portuaires cachent de sombres secrets et un redoutable Troll qui bloque l'accès aux navires.",
        "monsters": ["Gobelin Archer", "Homme-Bête à Marteau", "Troll"]
    },
    {
        "name": "Scénario 4 : La Tour des Gobelins (Outer Circle)", 
        "box": "base", 
        "boss": "Capitaine Gobelin",
        "description": "Infiltrez le bastion fortifié des peaux-vertes pour déloger leur chef autoproclamé.",
        "monsters": ["Gobelin Archer", "Orc Maraudeur", "Capitaine Gobelin"]
    },
    {
        "name": "Scénario 5 : Festin au Village (Outer Circle)", 
        "box": "base", 
        "boss": "Troll",
        "description": "Les monstres célèbrent une victoire en plein air. Interrompez leur festin et survivez à leur férocité.",
        "monsters": ["Homme-Bête à Lance", "Sœur du Plaisir", "Troll"]
    },
    {
        "name": "Scénario 6 : Les Égouts Sombres (Outer Circle)", 
        "box": "base", 
        "boss": "Minotaure",
        "description": "Naviguez dans les labyrinthes fangeux sous la ville où rôdent de monstrueuses créatures oubliées.",
        "monsters": ["Orc Maraudeur", "Sœur de la Douleur", "Minotaure"]
    },
    {
        "name": "Scénario 7 : Le Temple Sacrifié (Inner Circle)", 
        "box": "base", 
        "boss": "Lord Fang",
        "description": "L'influence maléfique de Lord Fang commence à corrompre le sanctuaire sacré d'Arcadia.",
        "monsters": ["Sœur de la Douleur", "Sœur du Plaisir", "Lord Fang"]
    },
    {
        "name": "Scénario 8 : Les Jardins Suspendus (Inner Circle)", 
        "box": "base", 
        "boss": "Lord Fang",
        "description": "Un havre de paix transformé en piège mortel par les sbires du Seigneur Vampire.",
        "monsters": ["Homme-Bête à Marteau", "Homme-Bête à Lance", "Lord Fang"]
    },
    {
        "name": "Scénario 9 : La Bibliothèque Interdite (Inner Circle)", 
        "box": "base", 
        "boss": "Lord Fang",
        "description": "Découvrez les grimoires ancestraux tout en échappant aux gardes d'élite de la citadelle.",
        "monsters": ["Gobelin Archer", "Sœur du Plaisir", "Lord Fang"]
    },
    {
        "name": "Scénario 10 : La Salle du Trône (Inner Circle)", 
        "box": "base", 
        "boss": "Lord Fang",
        "description": "L'antre direct de Lord Fang. Chaque recoin abrite un danger mortel.",
        "monsters": ["Troll", "Minotaure", "Lord Fang"]
    },
    {
        "name": "Scénario 11 : Affrontement Final - Le Temple de l'Aurore", 
        "box": "base", 
        "boss": "Lord Fang",
        "description": "Le combat ultime pour sauver Arcadia et terrasser définitivement Lord Fang et ses armées.",
        "monsters": ["Tous les types de monstres", "Lord Fang"]
    }
]

LEXICON = {
    "Régénération": "Le monstre récupère des PV au début de son tour.",
    "Riposte": "Inflige des dégâts automatiques en réaction à une attaque au corps à corps.",
    "Tir à couvert": "Ignore certaines pénalités de distance ou d'obstacles."
}
