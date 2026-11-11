# data/base.py

BOX_INFO = {
    "id": "base",
    "name": "Boîte de Base Arcadia Quest",
    "image": "assets/images/boite_base.jpg",
    "description": "La boîte originale d'Arcadia Quest avec sa campagne en 11 scénarios."
}

HEROES = {
    'Maya': {'hp': 5, 'att': '3 Dés (Magie)', 'def': '1 Dé', 'ability': 'Maîtrise du Mana', 'box': 'base'},
    'Grom': {'hp': 5, 'att': '3 Dés (CàC)', 'def': '2 Dés', 'ability': 'Frappe Brutale', 'box': 'base'},
    'Scarlet': {'hp': 5, 'att': '3 Dés (Tir)', 'def': '1 Dé', 'ability': 'Tir Précis', 'box': 'base'},
    'Seth': {'hp': 5, 'att': '3 Dés (CàC)', 'def': '1 Dé', 'ability': 'Fureur', 'box': 'base'},
    'Dirk': {'hp': 5, 'att': '3 Dés (CàC)', 'def': '1 Dé', 'ability': 'Bataille', 'box': 'base'},
    'Zazu': {'hp': 5, 'att': '3 Dés (Magie)', 'def': '1 Dé', 'ability': 'Esquive', 'box': 'base'},
    'Chubby': {'hp': 5, 'att': '3 Dés (CàC)', 'def': '2 Dés', 'ability': 'Robuste', 'box': 'base'},
    'Hilda': {'hp': 5, 'att': '3 Dés (Magie)', 'def': '1 Dé', 'ability': 'Soin Divin', 'box': 'base'},
    'Bjorn': {'hp': 6, 'att': '4 Dés (CàC)', 'def': '1 Dé', 'ability': 'Puissance Berserk', 'box': 'base'},
    'Krom': {'hp': 5, 'att': '3 Dés (CàC)', 'def': '2 Dés', 'ability': 'Coup Scénarisé', 'box': 'base'},
    'Wryn': {'hp': 5, 'att': '3 Dés (Tir)', 'def': '1 Dé', 'ability': 'Tir Multiple', 'box': 'base'},
    'Dart': {'hp': 5, 'att': '3 Dés (CàC)', 'def': '2 Dés', 'ability': 'Agilité', 'box': 'base'}
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
    {"name": "Scénario 1 : La Nuit Tombe (Outer Circle)", "box": "base", "boss": "Capitaine Gobelin"},
    {"name": "Scénario 2 : Pillage au Marché (Outer Circle)", "box": "base", "boss": "Minotaure"},
    {"name": "Scénario 3 : Les Docks Endormis (Outer Circle)", "box": "base", "boss": "Troll"},
    {"name": "Scénario 4 : La Tour des Gobelins (Outer Circle)", "box": "base", "boss": "Capitaine Gobelin"},
    {"name": "Scénario 5 : Festin au Village (Outer Circle)", "box": "base", "boss": "Troll"},
    {"name": "Scénario 6 : Les Égouts Sombres (Outer Circle)", "box": "base", "boss": "Minotaure"},
    {"name": "Scénario 7 : Le Temple Sacrifié (Inner Circle)", "box": "base", "boss": "Lord Fang"},
    {"name": "Scénario 8 : Les Jardins Suspendus (Inner Circle)", "box": "base", "boss": "Lord Fang"},
    {"name": "Scénario 9 : La Bibliothèque Interdite (Inner Circle)", "box": "base", "boss": "Lord Fang"},
    {"name": "Scénario 10 : La Salle du Trône (Inner Circle)", "box": "base", "boss": "Lord Fang"},
    {"name": "Scénario 11 : Affrontement Final - Le Temple de l'Aurore", "box": "base", "boss": "Lord Fang"}
]

LEXICON = {
    "Régénération": "Le monstre récupère des PV au début de son tour.",
    "Riposte": "Inflige des dégâts automatiques en réaction à une attaque au corps à corps.",
    "Tir à couvert": "Ignore certaines pénalités de distance ou d'obstacles."
}
