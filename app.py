import streamlit as st
import random
import os
from data import base

st.set_page_config(page_title="Arcadia Quest Assistant", page_icon="⚔️", layout="centered")

# --- INITIALISATION SESSION ---
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'selected_boxes' not in st.session_state:
    st.session_state.selected_boxes = ['base']
if 'active_heroes' not in st.session_state:
    st.session_state.active_heroes = {}
if 'spawned_monsters' not in st.session_state:
    st.session_state.spawned_monsters = []
if 'turn' not in st.session_state:
    st.session_state.turn = 1
if 'threat' not in st.session_state:
    st.session_state.threat = 1
if 'gold' not in st.session_state:
    st.session_state.gold = 0
if 'campaign_scenario_index' not in st.session_state:
    st.session_state.campaign_scenario_index = 1
if 'current_scenario' not in st.session_state:
    st.session_state.current_scenario = ""

def get_combined_data(selected_boxes):
    heroes = {}
    monsters = {}
    scenarios = []
    lexicon = {}
    
    if 'base' in selected_boxes:
        heroes.update(base.HEROES)
        monsters.update(base.MONSTERS)
        scenarios.extend(base.SCENARIOS)
        lexicon.update(base.LEXICON)
        
    return heroes, monsters, scenarios, lexicon


# ==========================================
# ÉCRAN 1 : SÉLECTION DES BOÎTES
# ==========================================
if st.session_state.step == 1:
    st.title("⚔️ ARCADIA COOP DRIVER ⚔️")
    st.subheader("Matériel Actif")
    
    col_img, col_info = st.columns([1, 2])
    with col_img:
        box_image_path = base.BOX_INFO["image"]
        if os.path.exists(box_image_path):
            st.image(box_image_path, use_container_width=True)
        else:
            st.markdown("📦 **[ Image Boîte de Base ]**")
            
    with col_info:
        st.success("**Boîte de Base sélectionnée (Mode Isolé)**")
        st.write("• **12 Héros** officiels disponibles")
        st.write("• **11 Scénarios** de campagne d'origine")
        st.write("• **Bestiaire complet** (Gobelins, Orcs, Sœurs, Hommes-Bêtes, Trolls, Minotaure, Lord Fang)")
    
    st.divider()
    
    if st.button("CONFIGURER SCÉNARIO & HÉROS ➔", use_container_width=True):
        st.session_state.step = 2
        st.rerun()
        
# ==========================================
# ÉCRAN 2 : SCÉNARIO & HÉROS (VIDE AU DÉMARRAGE)
# ==========================================
elif st.session_state.step == 2:
    st.title("🗺️ Configuration de la Partie")
    
    all_heroes, all_monsters, all_scenarios, _ = get_combined_data(st.session_state.selected_boxes)
    
    # --- 1. Sélection du Scénario & Aperçu ---
    st.subheader("1. Choix du Scénario")
    scenario_names = [s['name'] for s in all_scenarios]
    chosen_scenario_name = st.selectbox("Sélectionnez le scénario", scenario_names)
    st.session_state.current_scenario = chosen_scenario_name
    
    current_scen_data = next((s for s in all_scenarios if s['name'] == chosen_scenario_name), None)
    if current_scen_data:
        with st.container():
            st.info(
                f"📜 **Extrait :** {current_scen_data['description']}\n\n"
                f"🎯 **Boss Principal :** {current_scen_data['boss']}\n\n"
                f"👾 **Monstres du Scénario :** {', '.join(current_scen_data['monsters'])}"
            )

    st.divider()

    # --- 2. Sélection des Héros via Liste Déroulante (Vide par défaut) ---
    st.subheader("2. Sélection des Héros Engagés")
    
    hero_options = list(all_heroes.keys())
    selected_this_screen = st.multiselect(
        "Choisissez vos héros (1 à 4+)", 
        hero_options,
        default=[]  # <-- Aucun héros pré-sélectionné
    )
    
    # Affichage des cartes/photos et infos des héros sélectionnés
    if selected_this_screen:
        st.write("### 🃏 Cartes & Pouvoirs des Héros Sélectionnés")
        cols = st.columns(min(len(selected_this_screen), 2))
        
        for idx, h_name in enumerate(selected_this_screen):
            h_data = all_heroes[h_name]
            with cols[idx % len(cols)]:
                st.markdown(f"#### {h_name}")
                
                if os.path.exists(h_data['image']):
                    st.image(h_data['image'], use_container_width=True)
                else:
                    st.warning(f"Image manquante : `{h_data['image']}`")
                
                st.write(f"❤️ **PV :** {h_data['hp']}")
                st.write(f"🛡️ **Défense :** {h_data['def']} Dé(s)")
                st.info(f"✨ **Pouvoir ({h_data['ability']}) :**\n{h_data['ability_desc']}")

    st.divider()
    
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
                st.session_state.active_heroes = {
                    h: {
                        'hp': all_heroes[h]['hp'], 
                        'max_hp': all_heroes[h]['hp'],
                        'image': all_heroes[h]['image']
                    } for h in selected_this_screen
                }
                st.session_state.spawned_monsters = []  # <-- Plateau strictement vide au démarrage
                st.session_state.step = 3
                st.rerun()

# ==========================================
# ÉCRAN 3 : TABLEAU DE BORD DE JEU
# ==========================================
elif st.session_state.step == 3:
    st.title("🛡️ Tableau de Bord")
    st.caption(f"Scénario : **{st.session_state.current_scenario}**")
    
    # --- MÉTRIQUES DE JEU (Tour, Menace, Or) ---
    col_t1, col_t2, col_t3 = st.columns(3)
    col_t1.metric("Tour", st.session_state.turn)
    col_t2.metric("Menace", st.session_state.threat)
    col_t3.metric("Or de Guilde 🪙", f"{st.session_state.gold} PO")
    
    if st.button("Tour Suivant (+1 Menace)", use_container_width=True):
        st.session_state.turn += 1
        st.session_state.threat += 1
        st.rerun()

    st.divider()
    
    # --- SUIVI DES HÉROS (AVEC MINI-PHOTOS & PV UNIQUEMENT) ---
    st.subheader("👥 Vos Héros")
    
    for h_name, data in list(st.session_state.active_heroes.items()):
        col_img, col_txt, col_btns = st.columns([1, 2, 2])
        
        with col_img:
            if os.path.exists(data['image']):
                st.image(data['image'], use_container_width=True)
            else:
                st.write(f"**{h_name}**")
                
        with col_txt:
            st.markdown(f"#### {h_name}")
            st.write(f"❤️ **PV :** {data['hp']} / {data['max_hp']}")
            
        with col_btns:
            c_min, c_plus = st.columns(2)
            if c_min.button("➖", key=f"h_min_{h_name}") and data['hp'] > 0:
                data['hp'] -= 1
                st.rerun()
            if c_plus.button("➕", key=f"h_plus_{h_name}") and data['hp'] < data['max_hp']:
                data['hp'] += 1
                st.rerun()
        st.divider()

    # --- RECOMMANDATION DE SPAWN INTELLIGENTE ---
    st.subheader("💡 Recommandation de Spawn (IA)")
    nb_heroes = len(st.session_state.active_heroes)
    scen_idx = st.session_state.campaign_scenario_index
    
    # Facteur de difficulté/puissance basé sur l'équipement accumulé (progression des scénarios)
    power_modifier = 1 + (scen_idx * 0.15)
    rec_minions = max(2, int(nb_heroes * 1.5 * power_modifier))
    
    current_scen_data = next((s for s in base.SCENARIOS if s['name'] == st.session_state.current_scenario), None)
    recommended_monster = current_scen_data['monsters'][0] if current_scen_data and current_scen_data['monsters'] else "Gobelin Archer"
    
    st.info(
        f"📊 Pour **{nb_heroes} héros** engagés au **Scénario {scen_idx}** (Difficulté adaptée à votre équipement) :\n"
        f"• Il est recommandé de faire spawner environ **{rec_minions} sbires** de type **{recommended_monster}** ou de préparer le boss **{current_scen_data['boss'] if current_scen_data else 'Boss'}**."
    )

    # --- SUIVI DES MONSTRES & GESTION DE L'OR ---
    st.subheader("👾 Monstres sur le Plateau")
    _, active_monsters_db, _, _ = get_combined_data(st.session_state.selected_boxes)
    
    m_to_add = st.selectbox("Ajouter un monstre (Sélection libre)", list(active_monsters_db.keys()), key="select_monster_add")
    if st.button("Faire spawner ce monstre", use_container_width=True):
        new_id = (st.session_state.spawned_monsters[-1]['id'] + 1) if st.session_state.spawned_monsters else 1
        m_info = active_monsters_db[m_to_add]
        st.session_state.spawned_monsters.append({
            'id': new_id, 
            'name': m_to_add, 
            'hp': m_info['hp'], 
            'max_hp': m_info['hp'], 
            'gold': m_info.get('gold', 1)
        })
        st.rerun()
        
    if not st.session_state.spawned_monsters:
        st.caption("Aucun monstre sur le plateau (Plateau vide).")
    else:
        for idx, m in enumerate(list(st.session_state.spawned_monsters)):
            m_cols = st.columns([3, 2, 1])
            monster_gold = m.get('gold', 1)
            
            m_cols[0].write(f"#{m['id']} {m['name']} ({m['hp']}/{m['max_hp']} PV) — 🪙 {monster_gold} PO")
            
            # Utilisation de m['id'] unique pour éviter les doublons de clés
            if m_cols[1].button("Dégât 🗡️", key=f"dmg_monster_{m['id']}"):
                m['hp'] -= 1
                if m['hp'] <= 0:
                    st.session_state.gold += monster_gold
                    st.toast(f"Monstre #{m['id']} ({m['name']}) vaincu ! +{monster_gold} PO de butin 🪙", icon="💰")
                    st.session_state.spawned_monsters.pop(idx)
                st.rerun()
                
            if m_cols[2].button("🗑️", key=f"del_monster_{m['id']}"):
                st.session_state.spawned_monsters.pop(idx)
                st.rerun()
                
            if m_cols[2].button("🗑️", key=f"m_del_{m['id']}_{idx}"):
                st.session_state.spawned_monsters.pop(idx)
                st.rerun()
                
            if m_cols[2].button("🗑️", key=f"m_del_{m['id']}_{idx}"):
                st.session_state.spawned_monsters.pop(idx)
                st.rerun()

    st.divider()
    
    # --- Moteur IA de Ciblage ---
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
    if st.button("🔄 Recommencer / Changer de Boîtes", use_container_width=True):
        st.session_state.step = 1
        st.session_state.spawned_monsters = []
        st.session_state.active_heroes = {}
        st.session_state.turn = 1
        st.session_state.threat = 1
        st.session_state.gold = 0
        st.rerun()
