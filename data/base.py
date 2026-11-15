# data/base.py

BOX_INFO = {
    "id": "base",
    "name": "Boîte de Base Arcadia Quest",
    "image": "assets/images/boite_base.jpg",
    "description": "La boîte originale d'Arcadia Quest avec sa campagne en 11 scénarios."
}

HEROES = {
    'Maya': {'hp': 5, 'def': 1, 'ability': 'Magie', 'ability_desc': 'Capacité magique innée.', 'image': 'assets/images/maya.jpg', 'box': 'base'},
    'Grom': {'hp': 5, 'def': 1, 'ability': 'Berserker', 'ability_desc': 'Lance +1 dé à tous ses jets tant qu\'il est blessé.', 'image': 'assets/images/grom.jpg', 'box': 'base'},
    'Scarlet': {'hp': 5, 'def': 1, 'ability': 'Tir Précis', 'ability_desc': 'Ignore les malus de distance.', 'image': 'assets/images/scarlet.jpg', 'box': 'base'},
    'Seth': {'hp': 5, 'def': 1, 'ability': 'Fureur', 'ability_desc': 'Action de mouvement gratuite si élimination.', 'image': 'assets/images/seth.jpg', 'box': 'base'},
    'Dirk': {'hp': 5, 'def': 1, 'ability': 'Bataille', 'ability_desc': 'Relance un dé de défense raté en CàC.', 'image': 'assets/images/dirk.jpg', 'box': 'base'},
    'Zazu': {'hp': 5, 'def': 1, 'ability': 'Esquive', 'ability_desc': 'Réduit d’un dé les attaques ennemies.', 'image': 'assets/images/zazu.jpg', 'box': 'base'},
    'Chubby': {'hp': 5, 'def': 2, 'ability': 'Robuste', 'ability_desc': 'Ignore le premier dégât reçu par tour.', 'image': 'assets/images/chubby.jpg', 'box': 'base'},
    'Hilda': {'hp': 5, 'def': 1, 'ability': 'Soin Divin', 'ability_desc': 'Restaure 1 PV à un allié adjacent.', 'image': 'assets/images/hilda.jpg', 'box': 'base'},
    'Bjorn': {'hp': 6, 'def': 1, 'ability': 'Puissance Berserk', 'ability_desc': 'Gagne un dé d’attaque si PV <= 2.', 'image': 'assets/images/bjorn.jpg', 'box': 'base'},
    'Krom': {'hp': 5, 'def': 2, 'ability': 'Coup Scénarisé', 'ability_desc': 'Dégât bonus aux cibles de quête.', 'image': 'assets/images/krom.jpg', 'box': 'base'},
    'Wryn': {'hp': 5, 'def': 1, 'ability': 'Tir Multiple', 'ability_desc': 'Répartit ses dés de tir entre deux cibles.', 'image': 'assets/images/wryn.jpg', 'box': 'base'},
    'Dart': {'hp': 5, 'def': 2, 'ability': 'Agilité', 'ability_desc': 'Traverse les cases occupées sans coup d\'opportunité.', 'image': 'assets/images/dart.jpg', 'box': 'base'}
}

# Bestiaire structuré avec les niveaux de cartes officiels (Niveau 1, 2, 3)
MONSTERS = {
    # --- NIVEAU 1 (Outer Circle - Scénarios 1 à 6) ---
    'Gobelin Archer (Niv 1)': {'level': 1, 'hp': 2, 'gold': 1, 'ability': 'Tir à couvert', 'box': 'base'},
    'Orc Maraudeur (Niv 1)': {'level': 1, 'hp': 3, 'gold': 1, 'ability': 'Charge', 'box': 'base'},
    'Sœur de la Douleur (Niv 1)': {'level': 1, 'hp': 3, 'gold': 2, 'ability': 'Tourment', 'box': 'base'},
    'Sœur du Plaisir (Niv 1)': {'level': 1, 'hp': 3, 'gold': 2, 'ability': 'Charme', 'box': 'base'},
    'Capitaine Gobelin (Boss Niv 1)': {'level': 1, 'hp': 6, 'gold': 5, 'ability': 'Riposte', 'box': 'base'},
    'Minotaure (Mini-Boss Niv 1)': {'level': 1, 'hp': 5, 'gold': 4, 'ability': 'Piétinement', 'box': 'base'},
    'Troll (Boss Niv 1)': {'level': 1, 'hp': 6, 'gold': 5, 'ability': 'Régénération', 'box': 'base'},

    # --- NIVEAU 2 (Inner Circle - Scénarios 7 à 10) ---
    'Gobelin Archer (Niv 2)': {'level': 2, 'hp': 3, 'gold': 2, 'ability': 'Tir perçant', 'box': 'base'},
    'Orc Maraudeur (Niv 2)': {'level': 2, 'hp': 4, 'gold': 2, 'ability': 'Frénésie', 'box': 'base'},
    'Homme-Bête à Marteau (Niv 2)': {'level': 2, 'hp': 4, 'gold': 2, 'ability': 'Écrasement', 'box': 'base'},
    'Homme-Bête à Lance (Niv 2)': {'level': 2, 'hp': 4, 'gold': 2, 'ability': 'Allonge', 'box': 'base'},
    'Lord Fang (Grand Boss Niv 2)': {'level': 2, 'hp': 8, 'gold': 10, 'ability': 'Vampirisme', 'box': 'base'},

    # --- NIVEAU 3 (Final - Scénario 11) ---
    'Seigneur des Monstres (Niv 3)': {'level': 3, 'hp': 7, 'gold': 4, 'ability': 'Commandement suprême', 'box': 'base'},
    'Lord Fang (Avatar Ultime Niv 3)': {'level': 3, 'hp': 10, 'gold': 15, 'ability': 'Immortalité', 'box': 'base'}
}

SCENARIOS = [
    {
        "name": "Scénario 1 : La Nuit Tombe (Outer Circle)", 
        "box": "base", 
        "tier": 1, # Indique le cercle (1 = Outer, 2 = Inner, 3 = Final)
        "boss": "Capitaine Gobelin (Boss Niv 1)",
        "description": "Les gobelins envahissent les rues de la cité. Vos guildes doivent sécuriser les points stratégiques.",
        "objectives": "Éliminer le Capitaine Gobelin et sécuriser les objectifs.",
        "monsters": ["Gobelin Archer (Niv 1)", "Orc Maraudeur (Niv 1)", "Capitaine Gobelin (Boss Niv 1)"]
    },
    {
        "name": "Scénario 2 : Pillage au Marché (Outer Circle)", 
        "box": "base", 
        "tier": 1,
        "boss": "Minotaure (Mini-Boss Niv 1)",
        "description": "Le marché central regorge de trésors abandonnés.",
        "objectives": "Piller les coffres et vaincre le Minotaure.",
        "monsters": ["Orc Maraudeur (Niv 1)", "Sœur de la Douleur (Niv 1)", "Minotaure (Mini-Boss Niv 1)"]
    },
    {
        "name": "Scénario 3 : Les Docks Endormis (Outer Circle)", 
        "box": "base", 
        "tier": 1,
        "boss": "Troll (Boss Niv 1)",
        "description": "Les entrepôts portuaires cachent un redoutable Troll.",
        "objectives": "Survivre et abattre le Troll.",
        "monsters": ["Gobelin Archer (Niv 1)", "Homme-Bête à Marteau (Niv 2)", "Troll (Boss Niv 1)"]
    },
    {
        "name": "Scénario 4 : La Tour des Gobelins (Outer Circle)", 
        "box": "base", 
        "tier": 1,
        "boss": "Capitaine Gobelin (Boss Niv 1)",
        "description": "Infiltrez le bastion fortifié des peaux-vertes.",
        "objectives": "Nettoyer la tour de son chef.",
        "monsters": ["Gobelin Archer (Niv 1)", "Orc Maraudeur (Niv 1)", "Capitaine Gobelin (Boss Niv 1)"]
    },
    {
        "name": "Scénario 5 : Festin au Village (Outer Circle)", 
        "box": "base", 
        "tier": 1,
        "boss": "Troll (Boss Niv 1)",
        "description": "Les monstres célèbrent une victoire en plein air.",
        "objectives": "Disperser le festin et vaincre le Troll.",
        "monsters": ["Homme-Bête à Lance (Niv 2)", "Sœur du Plaisir (Niv 1)", "Troll (Boss Niv 1)"]
    },
    {
        "name": "Scénario 6 : Les Égouts Sombres (Outer Circle)", 
        "box": "base", 
        "tier": 1,
        "boss": "Minotaure (Mini-Boss Niv 1)",
        "description": "Naviguez dans les labyrinthes fangeux sous la ville.",
        "objectives": "Trouver la sortie et éliminer la bête.",
        "monsters": ["Orc Maraudeur (Niv 1)", "Sœur de la Douleur (Niv 1)", "Minotaure (Mini-Boss Niv 1)"]
    },
    {
        "name": "Scénario 7 : Le Temple Sacrifié (Inner Circle)", 
        "box": "base", 
        "tier": 2, # Inner Circle -> Monstres de niveau 2 recommandés
        "boss": "Lord Fang (Grand Boss Niv 2)",
        "description": "L'influence maléfique de Lord Fang corrompt le sanctuaire.",
        "objectives": "Purifier le temple et affronter Lord Fang.",
        "monsters": ["Sœur de la Douleur (Niv 1)", "Sœur du Plaisir (Niv 1)", "Lord Fang (Grand Boss Niv 2)"]
    },
    {
        "name": "Scénario 8 : Les Jardins Suspendus (Inner Circle)", 
        "box": "base", 
        "tier": 2,
        "boss": "Lord Fang (Grand Boss Niv 2)",
        "description": "Un havre de paix transformé en piège mortel.",
        "objectives": "Sécuriser les jardins.",
        "monsters": ["Homme-Bête à Marteau (Niv 2)", "Homme-Bête à Lance (Niv 2)", "Lord Fang (Grand Boss Niv 2)"]
    },
    {
        "name": "Scénario 9 : La Bibliothèque Interdite (Inner Circle)", 
        "box": "base", 
        "tier": 2,
        "boss": "Lord Fang (Grand Boss Niv 2)",
        "description": "Découvrez les grimoires ancestraux.",
        "objectives": "Protéger les connaissances et survivre.",
        "monsters": ["Gobelin Archer (Niv 2)", "Sœur du Plaisir (Niv 1)", "Lord Fang (Grand Boss Niv 2)"]
    },
    {
        "name": "Scénario 10 : La Salle du Trône (Inner Circle)", 
        "box": "base", 
        "tier": 2,
        "boss": "Lord Fang (Grand Boss Niv 2)",
        "description": "L'antre direct de Lord Fang.",
        "objectives": "Percasser les défenses du Seigneur Vampire.",
        "monsters": ["Troll (Boss Niv 1)", "Minotaure (Mini-Boss Niv 1)", "Lord Fang (Grand Boss Niv 2)"]
    },
    {
        "name": "Scénario 11 : Affrontement Final - Le Temple de l'Aurore", 
        "box": "base", 
        "tier": 3, # Niveau final
        "boss": "Lord Fang (Avatar Ultime Niv 3)",
        "description": "Le combat ultime pour sauver Arcadia.",
        "objectives": "Terrasser définitivement Lord Fang et ses armées.",
        "monsters": ["Seigneur des Monstres (Niv 3)", "Lord Fang (Avatar Ultime Niv 3)"]
    }
]

LEXICON = {
    "Régénération": "Le monstre récupère des PV au début de son tour.",
    "Riposte": "Inflige des dégâts automatiques en réaction à une attaque au corps à corps.",
    "Tir à couvert": "Ignore certaines pénalités de distance ou d'obstacles."
}
