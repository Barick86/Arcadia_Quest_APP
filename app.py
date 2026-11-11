import streamlit as st
import random

st.set_page_config(page_title="Arcadia Quest Assistant", page_icon="⚔️", layout="centered")

# --- DATABASE ---
MONSTERS_DB = {
    'Gobelin Archer': {'att': '2 Dés (Dist)', 'def': '1 Dé', 'hp': 2, 'ability': 'Tir à couvert', 'box': 'base'},
    'Orc Maraudeur': {'att': '3 Dés (CàC)', 'def': '2 Dés', 'hp': 3, 'ability': 'Charge', 'box': 'base'},
    'Capitaine Gobelin': {'att': '4 Dés (CàC)', 'def': '2 Dés', 'hp': 6, 'ability': 'Riposte (Boss)', 'box': 'base'},
    'Chien des Enfers': {'att': '3 Dés (CàC)', 'def': '1 Dé', 'hp': 3, 'ability': 'Brûlure', 'box': 'inferno'}
}

HEROES_DB = {
    'Maya': {'hp': 5, 'att': '3 Dés (Magie)', 'def': '1 Dé', 'ability': 'Maîtrise du Mana', 'box': 'base'},
    'Grom': {'hp': 5, 'att': '3 Dés (CàC)', 'def': '2 Dés', 'ability': 'Frappe Brutale', 'box': 'base'},
    'Scarlet': {'hp': 5, 'att': '3 Dés (Tir)', 'def': '1 Dé', 'ability': 'Tir Précis', 'box': 'base'},
    'Seth': {'hp': 5, 'att': '3 Dés (CàC)', 'def': '1 Dé', 'ability': 'Fureur', 'box': 'base'},
    'Infernal Knight': {'hp': 6, 'att': '4 Dés (CàC)', 'def': '3 Dés', 'ability': 'Lame de Magma', 'box': 'inferno'}
}

SCENARIOS_DB = [
    {"name": "Scénario 1 : L'Attaque des Gobelins", "box": "base", "boss": "Capitaine Gobelin"},
    {"name": "Scénario 2 : Les Profondeurs Infernales", "box": "inferno", "boss": "Chien des Enfers"}
]

# --- INITIALISATION SESSION ---
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'selected_boxes' not in st.session_state:
    st.session_state.selected_boxes = ['base', 'inferno']
if 'active_heroes' not in st.session_state:
    st.session_state.active_heroes = {}
if 'spawned_monsters' not in st.session_state:
    st.session_state.spawned_monsters = []
if 'turn' not in st.session_state:
    st.session_state.turn = 1
if 'threat' not in st.session_state:
    st.session_state.threat = 1

# --- ÉCRAN 1 : BOÎTES ---
if st.session_state.step == 1:
    st.title("⚔️ ARCADIA COOP DRIVER ⚔️")
    st.subheader("1. Matériel & Boîtes Disponibles")
    
    boxes = {'base': 'Boîte de Base', 'inferno': 'Inferno', 'pets': 'Pets', 'hell': 'Hell of a Box'}
    for b_key, b_name in boxes.items():
        checked = st.checkbox(b_name, value=(b_key in st.session_state.selected_boxes))
        if checked and b_key not in st.session_state.selected_boxes:
            st.session_state.selected_boxes.append(b_key)
        elif not checked and b_key in st.session_state.selected_boxes:
            st.session_state.selected_boxes.remove(b_key)
            
    if st.button("CONFIGURER SCÉNARIO & HÉROS ➔", use_container_width=True):
        st.session_state.step = 2
        st.rerun()

# --- ÉCRAN 2 : SCÉNARIO & GUILDE ---
elif st.session_state.step == 2:
    st.title("🗺️ Configuration")
    
    # Filtrage des scénarios selon les boîtes
    available_scenarios = [s for s in SCENARIOS_DB if s['box'] in st.session_state.selected_boxes]
    if not available_scenarios:
        st.warning("Aucun scénario disponible avec les boîtes sélectionnées. Cochez au moins la boîte de base.")
        if st.button("⬅️ Retour"):
            st.session_state.step = 1
            st.rerun()
    else:
        chosen_scenario = st.selectbox("Choisissez le Scénario", [s['name'] for s in available_scenarios])
        st.session_state.current_scenario = chosen_scenario
        
        st.subheader("Sélectionnez vos Héros")
        available_heroes = {k: v for k, v in HEROES_DB.items() if v['box'] in st.session_state.selected_boxes}
        
        selected_this_screen = []
        for h_name, h_data in available_heroes.items():
            if st.checkbox(f"{h_name} (PV: {h_data['hp']} | Att: {h_data['att']} | Pouvoir: {h_data['ability']})", key=f"hero_{h_name}"):
                selected_this_screen.append(h_name)
                
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⬅️ Retour", use_container_width=True):
                st.session_state.step = 1
                st.rerun()
        with col2:
            if st.button(" LANCER LA PARTIE ➔", use_container_width=True):
                if not selected_this_screen:
                    st.error("Sélectionnez au moins un héros !")
                else:
                    # Initialisation des PV des héros
                    st.session_state.active_heroes = {h: {'hp': HEROES_DB[h]['hp'], 'max_hp': HEROES_DB[h]['hp']} for h in selected_this_screen}
                    # Spawn initial des monstres du scénario
                    st.session_state.spawned_monsters = [
                        {'id': 1, 'name': 'Gobelin Archer', 'hp': 2, 'max_hp': 2},
                        {'id': 2, 'name': 'Orc Maraudeur', 'hp': 3, 'max_hp': 3}
                    ]
                    st.session_state.step = 3
                    st.rerun()

# --- ÉCRAN 3 : TABLEAU DE BORD DE JEU ---
elif st.session_state.step == 3:
    st.title("🛡️ Tableau de Bord")
    
    col_t1, col_t2 = st.columns(2)
    col_t1.metric("Tour Actuel", st.session_state.turn)
    col_t2.metric("Niveau de Menace", st.session_state.threat)
    
    if st.button("Tour Suivant (+1 Menace)"):
        st.session_state.turn += 1
        st.session_state.threat += 1
        st.rerun()

    st.divider()
    
    # --- SUIVI DES HÉROS ---
    st.subheader("👥 Vos Héros")
    for h_name, data in st.session_state.active_heroes.items():
        c1, c2, c3 = st.columns([2, 2, 1])
        c1.text(f"{h_name} (PV: {data['hp']}/{data['max_hp']})")
        
        # Boutons de gestion PV adaptés mobile (+ / -)
        if c2.button("➖", key=f"h_minus_{h_name}") and data['hp'] > 0:
            data['hp'] -= 1
            st.rerun()
        if c2.button("➕", key=f"h_plus_{h_name}") and data['hp'] < data['max_hp']:
            data['hp'] += 1
            st.rerun()
            
    st.divider()
    
    # --- SUIVI DES MONSTRES (GRANULAIRE) ---
    st.subheader("👾 Monstres sur le Plateau")
    
    # Ajout rapide d'un monstre
    m_to_add = st.selectbox("Ajouter un monstre", list(MONSTERS_DB.keys()))
    if st.button("Faire spawner ce monstre"):
        new_id = len(st.session_state.spawned_monsters) + 1
        m_info = MONSTERS_DB[m_to_add]
        st.session_state.spawned_monsters.append({'id': new_id, 'name': m_to_add, 'hp': m_info['hp'], 'max_hp': m_info['hp']})
        st.rerun()

    for idx, m in enumerate(st.session_state.spawned_monsters):
        m_box_col1, m_box_col2, m_box_col3 = st.columns([3, 2, 1])
        m_box_col1.text(f"#{m['id']} {m['name']} (PV: {m['hp']}/{m['max_hp']})")
        if m_box_col2.button("Dégât 🗡️", key=f"m_dmg_{idx}"):
            m['hp'] -= 1
            if m['hp'] <= 0:
                st.session_state.spawned_monsters.pop(idx)
            st.rerun()
        if m_box_col3.button("🗑️", key=f"m_del_{idx}"):
            st.session_state.spawned_monsters.pop(idx)
            st.rerun()

    st.divider()
    
    # --- MOTEUR IA ---
    st.subheader("🤖 Moteur IA - Ciblage Prioritaire")
    if st.button("Calculer la Cible (Héros le plus faible en PV)", use_container_width=True):
        alive_heroes = {h: d for h, d in st.session_state.active_heroes.items() if d['hp'] > 0}
        if alive_heroes:
            # Trouve le héros avec le moins de PV
            min_hp = min(d['hp'] for d in alive_heroes.values())
            candidates = [h for h, d in alive_heroes.items() if d['hp'] == min_hp]
            target = random.choice(candidates)
            st.success(f"🎯 Cible désignée : **{target}** ({min_hp} PV restants) !")
        else:
            st.error("Tous les héros sont KO !")

    if st.button("🔄 Recommencer la Partie"):
        st.session_state.step = 1
        st.rerun()