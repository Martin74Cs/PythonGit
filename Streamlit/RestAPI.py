import streamlit as st
import requests
import json
# API URL
API_URL = "http://localhost/api/elektro"
API_URL = "http://localhost/api/kabely"

st.title("REST API ve Streamlit")

# Funkce pro načtení dat
def load_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"⚠️ Chyba při načítání dat: {response.status_code}")
        return []

# Uložení dat do session state, pokud ještě nejsou
if "data" not in st.session_state:
    st.session_state["data"] = load_data()

# === FORMULÁŘ PRO ODESLÁNÍ DAT ===
st.header("Odeslat nový záznam")

with st.form(key="elektro_form"):
    name = st.text_input("deleni")
    popis = st.text_area("označení")
    submit_button = st.form_submit_button("Odeslat")

# with st.form(key="elektro_form"):
#     name = st.text_input("Název")
#     popis = st.text_area("Popis")
#     submit_button = st.form_submit_button("Odeslat")

if submit_button:
    # headers = {'Content-Type': 'application/json'}  
    # pridat = {'name': 'xxjjjjxx', 'popis': 'python' }
    # response = requests.post(API_URL, json.dumps(pridat), headers=headers)
    # st.session_state["data"] = load_data()
    # st.error(f"⚠️ jAK TO DOPADLO : {response.status_code}")

    data = {"name": name, "popis": popis}
    data = {"deleni": name, "označení": popis}
    headers = {"Content-Type": "application/json"}   
    response = requests.post(API_URL, json=data , headers=headers)
    st.write(f"📡 API Status Code: {response.status_code}")  # Debug

    if response.status_code in [200, 201]:
        st.success("✅ Úspěšně odesláno!")
        
        # Aktualizace session state
        st.session_state["data"] = load_data()
    else:
        st.error(f"⚠️ Chyba při odesílání: {response.status_code}")
        # st.write(response.text)
        st.session_state["data"] = load_data()

# === ZOBRAZENÍ DAT ===
st.header("📋 Seznam záznamů")

data = st.session_state["data"]

# if data:
#     for item in data:
#         st.write(f"**ID:** {item.get('id')}")
#         st.write(f"**Název:** {item.get('name')}")
#         st.write(f"**Popis:** {item.get('popis')}")
#         st.write("---")
# else:
#     st.info("ℹ️ Žádná data k dispozici.")


if data:
    for item in data:
        col1, col2 = st.columns([4, 1])  # Rozložení: text vlevo, tlačítko vpravo
        with col1:
            st.write(f"**ID:** {item.get('id')}")
            st.write(f"**Apid:** {item.get('apid')}")
            st.write(f"**Deleni:** {item.get('deleni')}")
            st.write(f"**Označení:** {item.get('označení')}")
            st.write("---")
        with col2:
            if st.button("🗑️", key=item.get("id")):
                delete_url = f"{API_URL}/{item.get('id')}"          
                print(delete_url)
                response = requests.delete(delete_url)
                st.session_state["data"] = load_data()
                if response.status_code != 200:
                    st.error(f"⚠️ Chyba při mazání {item.get('Id')}")                
else:
    st.info("ℹ️ Žádná data k dispozici.")
