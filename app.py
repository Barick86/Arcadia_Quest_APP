import streamlit as st
import random
import os

st.set_page_config(page_title="Arcadia Quest Assistant - Base", page_icon="⚔️", layout="centered")

# --- DATABASE BOÎTE DE BASE ---
MONSTERS_DB = {
    'Gobelin Archer': {'att': '2 Dés (Dist)', 'def': '1 Dé', 'hp': 2, 'ability': 'Tir à couvert'},
    'Orc Maraudeur': {'att': '3 Dés (CàC)', 'def': '2 Dés', 'hp': 3, 'ability': 'Charge'},
    'Capitaine Gobelin': {'att': '4 Dés (CàC)', 'def': '2 Dés', 'hp': 6, 'ability': 'Riposte (Boss)'}
}

HEROES_DB = {
    'Maya': {'hp': 5, 'att': '3 Dés (Magie)', 'def': '1 Dé', 'ability': 'Maîtrise du Mana'},
    'Grom': {'hp': 5, 'att': '3 Dés (CàC)', 'def': '2 Dés', 'ability': 'Frappe Brutale'},
    'Scarlet': {'hp': 5, 'att': '3 Dés (Tir)', 'def': '1 Dé', 'ability': 'Tir Précis'},
    'Seth': {'hp': 5, 'att': '3 Dés (CàC)', 'def': '1 Dé', 'ability': 'Fureur'},
    'Dirk': {'hp': 5, 'att': '3 Dés (CàC)', 'def': '1 Dé', 'ability': 'Bataille'},
    'Zazu': {'hp': 5, 'att': '3 Dés (Magie)', 'def': '1 Dé', 'ability': 'Esquive'}
}

SCENARIOS_DB = [
    "Scénario 1 : L'Attaque des Gobelins",
    "Scénario 2 : Les Cavernes Sombres",
    "Scénario 3 : Le Repaire du Capitaine"
]

# --- INITIALISATION SESSION ---
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'active_heroes' not in st.session_state:
    st.session_state.active_heroes = {}
if 'spawned_monsters' not in st.session_state:
    st.session_state.spawned_monsters = []
if 'turn' not in st.session_state:
    st.session_state.turn = 1
if 'threat' not in st.session_state:
    st.session_state.threat = 1

# --- ÉCRAN 1 : ACCUEIL & BOÎTE ACTIVE ---
if st.session_state.step == 1:
    st.title("⚔️ ARCADIA COOP DRIVER ⚔️")
    st.subheader("Matériel Actif")
    
    # Affichage de la boîte de base (avec gestion future de l'image locale)
    col_img, col_info = st.columns([1, 2])
    with col_img:
        box_image_path = "assets/images/boite_base.jpg"
        if os.path.exists(box_image_path):
            st.image(box_image_path, use_container_width=True)
        else:
            # Placeholder visuel en attendant l'image réelle
            st.markdown("📦 **[ Image Boîte de Base ]**\n*(Place ton image dans assets/images/boite_base.jpg)*")
            
    with col_info:
        st.success("**Boîte de Base sélectionnée (Mode Isolé)**")
        st.write("• 6 Héros disponibles")
        st.write("• 3 Scénarios originaux")
        st.write("• Bestiaire standard")
    
    st.divider()
    
    if st.button("CONFIGURER SCÉNARIO & HÉROS ➔", use_container_width=True):
        st.session_state.step = 2
        st.rerun()

# --- ÉCRAN 2 : SCÉNARIO & HÉROS ---
elif st.session_state.step == 2:
    st.title("🗺️ Configuration de la Partie")
    
    chosen_scenario = st.selectbox("Choisissez le Scénario", SCENARIOS_DB)
    st.session_state.current_scenario = chosen_scenario
    
    st.subheader("Sélectionnez vos Héros")
    
    selected_this_screen = []
    for h_name, h_data in HEROES_DB.items():
        if st.checkbox(f"{h_name} (PV: {h_data['hp']} | Att: {h_data['att']} | Pouvoir: {h_data['ability']})", key=f"hero_{h_name}"):
            selected_this_screen.append(h_name)
            
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Retour", use_container_width=True):
            st.session_state.step = 1
            st.rerun()
    with col2:
        if st.button("LANCER LA PARTIE ➔", use_container_width=True):
            if not selected_this_screen:
                st.error("Sélectionnez au moins un héros !")
            else:
                st.session_state.active_heroes = {h: {'hp': HEROES_DB[h]['hp'], 'max_hp': HEROES_DB[h]['hp']} for h in selected_this_screen}
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
    
    if st.button("Tour Suivant (+1 Menace)", use_container_width=True):
        st.session_state.turn += 1
        st.session_state.threat += 1
        st.rerun()

    st.divider()
    
    # --- SUIVI DES HÉROS ---
    st.subheader("👥 Vos Héros")
    for h_name, data in list(st.session_state.active_heroes.items()):
        c1, c2 = st.columns([3, 2])
        c1.write(f"**{h_name}** : {data['hp']} / {data['max_hp']} PV")
        
        col_minus, col_plus = c2.columns(2)
        if col_minus.button("➖", key=f"h_min_{h_name}") and data['hp'] > 0:
            data['hp'] -= 1
            st.rerun()
        if col_plus.button("➕", key=f"h_plus_{h_name}") and data['hp'] < data['max_hp']:
            data['hp'] += 1
            st.rerun()
            
    st.divider()
    
    # --- SUIVI DES MONSTRES ---
    st.subheader("👾 Monstres sur le Plateau")
    
    m_to_add = st.selectbox("Ajouter un monstre", list(MONSTERS_DB.keys()), key="select_monster_add")
    if st.button("Faire spawner ce monstre", use_container_width=True):
        new_id = (st.session_state.spawned_monsters[-1]['id'] + 1) if st.session_state.spawned_monsters else 1
        m_info = MONSTERS_DB[m_to_add]
        st.session_state.spawned_monsters.append({'id': new_id, 'name': m_to_add, 'hp': m_info['hp'], 'max_hp': m_info['hp']})
        st.rerun()

    if not st.session_state.spawned_monsters:
        st.caption("Aucun monstre sur le plateau.")
    else:
        for idx, m in enumerate(list(st.session_state.spawned_monsters)):
            m_cols = st.columns([3, 2, 1])
            m_cols[0].write(f"#{m['id']} {m['name']} ({m['hp']}/{m['max_hp']} PV)")
            if m_cols[1].button("Dégât 🗡️", key=f"m_dmg_{m['id']}_{idx}"):
                m['hp'] -= 1
                if m['hp'] <= 0:
                    st.session_state.spawned_monsters.pop(idx)
                st.rerun()
            if m_cols[2].button("🗑️", key=f"m_del_{m['id']}_{idx}"):
                st.session_state.spawned_monsters.pop(idx)
                st.rerun()

    st.divider()
    
    # --- MOTEUR IA ---
    st.subheader("🤖 Moteur IA - Ciblage Prioritaire")
    if st.button("Calculer la Cible (Héros le plus faible en PV)", use_container_width=True):
        alive_heroes = {h: d for h, d in st.session_state.active_heroes.items() if d['hp'] > 0}
        if alive_heroes:
            min_hp = min(d['hp'] for d in alive_heroes.values())
            candidates = [h for h, d in alive_heroes.items() if d['hp'] == min_hp]
            target = random.choice(candidates)
            st.success(f"🎯 Cible désignée : **{target}** ({min_hp} PV restants) !")
        else:
            st.error("Tous les héros sont KO !")

    st.divider()
    if st.button("🔄 Recommencer la Partie", use_container_width=True):
        st.session_state.step = 1
        st.session_state.spawned_monsters = []
        st.session_state.active_heroes = {}
        st.session_state.turn = 1
        st.session_state.threat = 1
        st.rerun()
