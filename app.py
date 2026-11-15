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
    st.session_state.campaign_scenario_index = 0
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
# ÉCRAN 2 : SCÉNARIO & HÉROS
# ==========================================
elif st.session_state.step == 2:
    st.title("🗺️ Configuration de la Partie")
    
    all_heroes, all_monsters, all_scenarios, _ = get_combined_data(st.session_state.selected_boxes)
    
    st.subheader("1. Choix du Scénario")
    scenario_names = [s['name'] for s in all_scenarios]
    default_idx = min(st.session_state.campaign_scenario_index, len(scenario_names) - 1)
    chosen_scenario_name = st.selectbox("Sélectionnez le scénario", scenario_names, index=default_idx)
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

    st.subheader("2. Sélection des Héros Engagés")
    hero_options = list(all_heroes.keys())
    default_heroes = list(st.session_state.active_heroes.keys()) if st.session_state.active_heroes else []
    
    selected_this_screen = st.multiselect("Choisissez vos héros (1 à 4+)", hero_options, default=default_heroes)
    
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
                st.session_state.active_heroes = {h: {'image': all_heroes[h]['image']} for h in selected_this_screen}
                st.session_state.spawned_monsters = []
                st.session_state.step = 3
                st.rerun()

# ==========================================
# ÉCRAN 3 : TABLEAU DE BORD DE JEU
# ==========================================
elif st.session_state.step == 3:
    st.title("🛡️ Tableau de Bord")
    st.caption(f"Scénario : **{st.session_state.current_scenario}**")
    
    col_t1, col_t2, col_t3 = st.columns(3)
    col_t1.metric("Tour", st.session_state.turn)
    col_t2.metric("Menace", st.session_state.threat)
    col_t3.metric("Or de Guilde 🪙", f"{st.session_state.gold} PO")
    
    col_bt1, col_bt2 = st.columns(2)
    if col_bt1.button("Tour Suivant (+1 Menace)", use_container_width=True):
        st.session_state.turn += 1
        st.session_state.threat += 1
        st.rerun()
        
    if col_bt2.button("🏁 Terminer ce Scénario (Marché)", use_container_width=True):
        st.session_state.step = 4
        st.rerun()

    st.divider()
    
    st.subheader("👥 Guilde Active")
    cols_heroes = st.columns(min(len(st.session_state.active_heroes), 4))
    for idx, (h_name, data) in enumerate(st.session_state.active_heroes.items()):
        with cols_heroes[idx % len(cols_heroes)]:
            if os.path.exists(data['image']):
                st.image(data['image'], use_container_width=True)
            st.markdown(f"<p align='center'><b>{h_name}</b></p>", unsafe_allow_html=True)

    st.divider()

    st.subheader("💡 Contexte & Objectif du Scénario")
    _, active_monsters_db, all_scenarios, _ = get_combined_data(st.session_state.selected_boxes)
    current_scen_data = next((s for s in all_scenarios if s['name'] == st.session_state.current_scenario), None)
    scen_tier = current_scen_data.get('tier', 1) if current_scen_data else 1
    
    st.info(
        f"📜 **Objectif :** {current_scen_data.get('objectives', 'Accomplir la quête principale.')}\n\n"
        f"⚙️ **Cercle de Campagne :** Niveau {scen_tier} "
        f"({'Outer Circle - Recommandé Niv 1' if scen_tier == 1 else 'Inner Circle - Recommandé Niv 2' if scen_tier == 2 else 'Temple de l\'Aurore - Recommandé Niv 3'}).\n\n"
        f"🎯 **Boss :** {current_scen_data.get('boss', 'Boss de fin')}\n\n"
        f"👾 **Monstres prévus :** {', '.join(current_scen_data.get('monsters', []))}"
    )

    st.subheader("👾 Faire spawner un monstre")
    clean_monster_names = sorted(list(set([m.rsplit(' (', 1)[0] for m in active_monsters_db.keys()])))
    
    col_sel_m, col_sel_lvl = st.columns([2, 1])
    with col_sel_m:
        chosen_monster_base = st.selectbox("Famille de monstre", clean_monster_names, key="select_monster_family")
    with col_sel_lvl:
        chosen_level = st.selectbox("Niveau de carte", [1, 2, 3], index=scen_tier-1, key="select_monster_level")

    matching_key = None
    for k in active_monsters_db.keys():
        if chosen_monster_base in k and f"Niv {chosen_level}" in k:
            matching_key = k
            break
    if not matching_key:
        matching_key = f"{chosen_monster_base} (Niv {chosen_level})"
        if matching_key not in active_monsters_db:
            matching_key = list(active_monsters_db.keys())[0]

    if st.button(f"Faire spawner : {matching_key}", use_container_width=True):
        new_id = (st.session_state.spawned_monsters[-1]['id'] + 1) if st.session_state.spawned_monsters else 1
        m_info = active_monsters_db.get(matching_key, {'hp': 3, 'gold': 1, 'color_badge': f'🟢 Niv {chosen_level}', 'ability': 'Standard'})
        st.session_state.spawned_monsters.append({
            'id': new_id, 'name': matching_key, 'hp': m_info['hp'], 'max_hp': m_info['hp'], 'gold': m_info.get('gold', 1)
        })
        st.rerun()
        
    st.markdown("### 📋 Monstres actifs sur le Plateau")
    if not st.session_state.spawned_monsters:
        st.caption("Aucun monstre sur le plateau (Plateau vide).")
    else:
        for idx, m in enumerate(list(st.session_state.spawned_monsters)):
            m_data = active_monsters_db.get(m['name'], {})
            monster_gold = m.get('gold', m_data.get('gold', 1))
            color_badge = m_data.get('color_badge', '🟢 Niv 1')
            card_image = m_data.get('image', '')
            ability = m_data.get('ability', 'Aucune')

            with st.container(border=True):
                m_cols = st.columns([3, 2, 1])
                m_cols[0].markdown(f"**#{m['id']} {m['name']}** ({color_badge})<br>❤️ `{m['hp']}/{m['max_hp']} PV` — 🪙 `{monster_gold} PO`", unsafe_allow_html=True)
                
                if m_cols[1].button("Dégât 🗡️", key=f"dmg_mon_{m['id']}_{idx}"):
                    m['hp'] -= 1
                    if m['hp'] <= 0:
                        st.session_state.gold += monster_gold
                        st.toast(f"Monstre #{m['id']} ({m['name']}) vaincu ! +{monster_gold} PO de butin 🪙", icon="💰")
                        st.session_state.spawned_monsters.pop(idx)
                    st.rerun()
                    
                if m_cols[2].button("🗑️", key=f"del_mon_{m['id']}_{idx}"):
                    st.session_state.spawned_monsters.pop(idx)
                    st.rerun()

                with st.expander(f"🃏 Carte & Capacité ({ability})"):
                    if card_image and os.path.exists(card_image):
                        st.image(card_image, width=250)
                    else:
                        st.caption(f"Capacité spéciale : **{ability}**")
                        st.caption(f"*(Image attendue : `{card_image}`)*")

    st.divider()
    
    # --- MOTEUR IA DE CIBLAGE FUSIONNÉ ---
    st.subheader("🤖 Moteur IA - Ciblage Aléatoire")
    if st.button("🎲 Tirer un type de ciblage aléatoire (Faible / Fort)", use_container_width=True):
        strategy = random.choice(["FAIBLE", "FORT"])
        if strategy == "FAIBLE":
            st.success("🎯 **Ordre de l'IA :** Cibler en priorité le héros ayant le **moins de PV** sur votre plateau !")
        else:
            st.success("🎯 **Ordre de l'IA :** Cibler en priorité le héros ayant le **plus de PV** sur votre plateau !")

    st.divider()
    if st.button("🔄 Recommencer / Changer de Boîtes", use_container_width=True):
        st.session_state.step = 1
        st.session_state.spawned_monsters = []
        st.session_state.active_heroes = {}
        st.session_state.turn = 1
        st.session_state.threat = 1
        st.session_state.gold = 0
        st.session_state.campaign_scenario_index = 0
        st.rerun()

# ==========================================
# ÉCRAN 4 : PHASE DE MARCHÉ & TRANSITION
# ==========================================
elif st.session_state.step == 4:
    st.title("🛒 Phase de Marché & Transition")
    st.success("Scénario précédent validé avec succès ! Il est temps de dépenser votre butin.")
    
    st.metric("Trésor de Guilde Disponible 🪙", f"{st.session_state.gold} PO")
    
    st.write("### 💸 Dépenser des PO (Achats de Marché)")
    col_spend1, col_spend2, col_spend3, col_spend4 = st.columns(4)
    if col_spend1.button("-1 PO", use_container_width=True) and st.session_state.gold >= 1:
        st.session_state.gold -= 1
        st.rerun()
    if col_spend2.button("-2 PO", use_container_width=True) and st.session_state.gold >= 2:
        st.session_state.gold -= 2
        st.rerun()
    if col_spend3.button("-3 PO", use_container_width=True) and st.session_state.gold >= 3:
        st.session_state.gold -= 3
        st.rerun()
    if col_spend4.button("-5 PO", use_container_width=True) and st.session_state.gold >= 5:
        st.session_state.gold -= 5
        st.rerun()

    custom_cost = st.number_input("Ou dépenser un montant personnalisé de PO :", min_value=0, max_value=max(st.session_state.gold, 0), step=1)
    if st.button("Valider la dépense personnalisée", use_container_width=True):
        if custom_cost > 0 and st.session_state.gold >= custom_cost:
            st.session_state.gold -= custom_cost
            st.toast(f"Dépense de {custom_cost} PO effectuée !", icon="💸")
            st.rerun()

    st.divider()
    
    _, _, all_scenarios, _ = get_combined_data(st.session_state.selected_boxes)
    current_scen_data = next((s for s in all_scenarios if s['name'] == st.session_state.current_scenario), None)
    scen_tier = current_scen_data.get('tier', 1) if current_scen_data else 1
    market_level = min(scen_tier + 1, 3)
    
    st.info(
        f"🛍️ **Recommandation de Marché :** En raison de la fin du scénario (Cercle Niveau {scen_tier}), "
        f"vous avez accès aux cartes d'équipement de **Marché de Niveau {market_level}**."
    )
    
    st.subheader("🗺️ Choix du Scénario Suivant")
    scenario_names = [s['name'] for s in all_scenarios]
    next_default_idx = min(st.session_state.campaign_scenario_index + 1, len(scenario_names) - 1)
    chosen_next_scenario = st.selectbox("Sélectionnez la prochaine quête de la campagne", scenario_names, index=next_default_idx)
    
    st.divider()
    
    if st.button("🚀 LANCER DIRECTEMENT LE PROCHAIN SCÉNARIO ➔", use_container_width=True):
        st.session_state.current_scenario = chosen_next_scenario
        st.session_state.campaign_scenario_index = scenario_names.index(chosen_next_scenario)
        st.session_state.spawned_monsters = []
        st.session_state.turn = 1
        st.session_state.threat = 1
        st.session_state.step = 3
        st.rerun()
