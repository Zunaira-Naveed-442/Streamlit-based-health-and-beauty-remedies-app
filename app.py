import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="🌿 Smart Home Remedies", page_icon="🌸", layout="centered")

st.title("🌿 Smart Home Remedies & Beauty Care")
st.write("Your intelligent companion for **natural health and beauty remedies** — powered by knowledge and care 🌸")

# --- Remedies Dataset ---
remedies = {
    "Cough": [
        {"Title": "Honey and Ginger Tea", "Description": "Mix 1 tsp of honey with grated ginger in warm water. Drink twice daily.", "Why it Works": "Honey soothes throat irritation while ginger helps expel mucus."},
        {"Title": "Turmeric Milk", "Description": "Add ½ tsp turmeric powder to warm milk and drink before bed.", "Why it Works": "Curcumin in turmeric is anti-inflammatory and boosts immunity."},
        {"Title": "Peppermint Tea", "Description": "Drink peppermint tea twice daily.", "Why it Works": "Menthol helps open airways and relieve cough."},
        {"Title": "Black Pepper & Honey", "Description": "Mix ¼ tsp black pepper with 1 tsp honey.", "Why it Works": "Improves circulation and clears phlegm."},
        {"Title": "Steam Inhalation", "Description": "Inhale steam with 2 drops eucalyptus oil for 5 mins.", "Why it Works": "Loosens mucus and clears nasal passage."}
    ],
    "Flu": [
        {"Title": "Garlic Tea", "Description": "Boil 2 crushed garlic cloves in a cup of water and drink warm.", "Why it Works": "Has antiviral and immune-boosting compounds."},
        {"Title": "Ginger Lemon Drink", "Description": "Mix grated ginger and lemon juice in warm water.", "Why it Works": "Relieves body aches and boosts vitamin C."},
        {"Title": "Chicken Soup", "Description": "Drink homemade soup with garlic and pepper.", "Why it Works": "Rehydrates and provides anti-inflammatory benefits."},
        {"Title": "Elderberry Syrup", "Description": "Take 1 tbsp twice daily.", "Why it Works": "Shortens duration of flu symptoms."},
        {"Title": "Steam Inhalation", "Description": "Inhale steam for 10 minutes.", "Why it Works": "Clears sinuses and relieves headache."}
    ],
    "Fever": [
        {"Title": "Basil Tea", "Description": "Boil basil leaves in water and drink twice daily.", "Why it Works": "Natural fever reducer and immune booster."},
        {"Title": "Cold Compress", "Description": "Apply a cool wet cloth to forehead and wrists.", "Why it Works": "Helps lower body temperature."},
        {"Title": "Coriander Tea", "Description": "Boil coriander seeds and drink the water.", "Why it Works": "Flavonoids help reduce fever and detoxify the body."},
        {"Title": "Raisin Water", "Description": "Soak raisins overnight and drink water in the morning.", "Why it Works": "Antioxidants help fight infection."},
        {"Title": "Fenugreek Water", "Description": "Soak seeds overnight and sip water throughout the day.", "Why it Works": "Reduces body heat and clears toxins."}
    ],
    "Sore Throat": [
        {"Title": "Salt Water Gargle", "Description": "Mix ½ tsp salt in warm water and gargle twice daily.", "Why it Works": "Reduces bacteria and inflammation."},
        {"Title": "Honey Lemon Tea", "Description": "Mix 1 tbsp honey and lemon juice in warm water.", "Why it Works": "Coats throat and provides vitamin C."},
        {"Title": "Chamomile Tea", "Description": "Drink warm chamomile tea twice a day.", "Why it Works": "Contains anti-inflammatory and antibacterial properties."},
        {"Title": "Clove Tea", "Description": "Boil cloves in water and sip slowly.", "Why it Works": "Eugenol in cloves acts as a pain reliever."},
        {"Title": "Ginger Tea", "Description": "Add fresh ginger to boiling water and drink.", "Why it Works": "Reduces inflammation and soothes the throat."}
    ],
    "Skin Whitening": [
        {"Title": "Gram Flour & Lemon Mask", "Description": "Mix 2 tbsp gram flour, 1 tsp lemon juice, and rose water.", "Why it Works": "Brightens and removes tan."},
        {"Title": "Potato Juice", "Description": "Apply grated potato or juice daily.", "Why it Works": "Natural bleaching agent for lighter skin tone."},
        {"Title": "Rice Flour Scrub", "Description": "Mix rice flour and milk and scrub gently.", "Why it Works": "Removes dead cells and brightens skin."},
        {"Title": "Papaya Honey Mask", "Description": "Mash papaya with honey and apply for 20 mins.", "Why it Works": "Enzymes exfoliate and lighten complexion."},
        {"Title": "Sandalwood Paste", "Description": "Mix sandalwood powder with rose water.", "Why it Works": "Cools and brightens the skin naturally."}
    ],
    "Dark Spots": [
        {"Title": "Aloe Vera Gel", "Description": "Apply aloe gel before sleeping.", "Why it Works": "Contains aloin that fades pigmentation."},
        {"Title": "Lemon & Honey Mask", "Description": "Apply mixture for 10 minutes daily.", "Why it Works": "Vitamin C lightens dark spots."},
        {"Title": "Turmeric & Milk", "Description": "Apply paste of turmeric and milk.", "Why it Works": "Balances skin tone and reduces marks."},
        {"Title": "Potato Slice Rub", "Description": "Rub a slice on affected area daily.", "Why it Works": "Catecholase enzyme helps fade spots."},
        {"Title": "Green Tea Toner", "Description": "Apply cooled green tea using cotton.", "Why it Works": "Antioxidants repair skin cells."}
    ],
    "Hair Care": [
        {"Title": "Coconut Oil Massage", "Description": "Massage scalp twice weekly with warm oil.", "Why it Works": "Improves circulation and strengthens roots."},
        {"Title": "Onion Juice", "Description": "Apply onion juice for 20 minutes before shampoo.", "Why it Works": "Boosts hair growth and prevents thinning."},
        {"Title": "Amla Hair Mask", "Description": "Mix amla powder with yogurt and apply 30 mins.", "Why it Works": "Strengthens follicles and prevents greying."},
        {"Title": "Egg & Olive Oil Mask", "Description": "Mix egg yolk with olive oil and apply for 15 mins.", "Why it Works": "Adds protein and shine to hair."},
        {"Title": "Fenugreek Paste", "Description": "Apply soaked fenugreek paste on scalp.", "Why it Works": "Reduces dandruff and hair fall."}
    ],
    "Skin Glow": [
        {"Title": "Turmeric & Yogurt Mask", "Description": "Mix 1 tsp turmeric with 2 tbsp yogurt.", "Why it Works": "Brightens and hydrates dull skin."},
        {"Title": "Banana & Honey Mask", "Description": "Mash banana with honey and apply for 15 mins.", "Why it Works": "Moisturizes and softens skin."},
        {"Title": "Cucumber & Rose Water", "Description": "Spray mixture on face daily.", "Why it Works": "Soothes and refreshes skin tone."},
        {"Title": "Tomato & Sugar Scrub", "Description": "Rub tomato slice dipped in sugar gently.", "Why it Works": "Exfoliates and adds glow."},
        {"Title": "Milk & Saffron", "Description": "Soak saffron in milk, apply before bed.", "Why it Works": "Evens complexion and adds radiance."}
    ]
}

# --- Flatten remedies into searchable list ---
all_remedies = []
for cat, items in remedies.items():
    for i in items:
        entry = i.copy()
        entry["Category"] = cat
        all_remedies.append(entry)

# --- Search / Recommendation System ---
st.subheader("🔍 Remedy by Symptoms or Concern")
query = st.text_input("Enter your symptom or concern (e.g. 'dry cough', 'hair fall', 'dark spots', 'flu body pain')")

if query:
    results = [
        r for r in all_remedies
        if query.lower() in r["Category"].lower()
        or query.lower() in r["Title"].lower()
        or query.lower() in r["Description"].lower()
        or query.lower() in r["Why it Works"].lower()
    ]
    if results:
        st.success(f"✅ Found {len(results)} remedies related to **'{query}'**:")
        for idx, r in enumerate(results, 1):
            with st.expander(f"{idx}. {r['Title']} ({r['Category']})"):
                st.write(f"**How to Use:** {r['Description']}")
                st.write(f"**Why it Works:** {r['Why it Works']}")
    else:
        st.warning("No exact match found. Try related terms like 'flu', 'skin glow', or 'dandruff'.")

# --- Category Browser ---
st.write("---")
st.subheader("🌸 Browse Remedies by Category")
category = st.selectbox("Select a Category:", list(remedies.keys()))

for idx, item in enumerate(remedies[category], start=1):
    with st.expander(f"{idx}. {item['Title']}"):
        st.write(f"**How to Use:** {item['Description']}")
        st.write(f"**Why it Works:** {item['Why it Works']}")

st.write("---")
st.info("💡 *These remedies are for educational use only. Consult a doctor for serious conditions.*")
st.caption("Developed with ❤️ using Streamlit — Natural Care, Smartly Delivered 🌿")
