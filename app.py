import streamlit as st
import matplotlib.pyplot as plt
import math

# Titulek aplikace
st.set_page_config(page_title="Body na kružnici", page_icon="🎯", layout="centered")
st.title("🎯 Generátor bodů na kružnici")

st.markdown(
    """
    Tato aplikace vykreslí body na kružnici podle zadaných parametrů.
    - Nastav **střed kružnice (X, Y)**  
    - Zvol **poloměr a počet bodů**  
    - Vyber **barvu bodů**  
    - Graf má číselné osy včetně jednotek (metry)  
    - Klikni na tlačítko pro **uložení obrázku**
    """
)

# --- Ovládací prvky ---
st.sidebar.header("⚙️ Parametry kružnice")

x0 = st.sidebar.slider("Střed X [m]", -20.0, 20.0, 0.0, step=0.5)
y0 = st.sidebar.slider("Střed Y [m]", -20.0, 20.0, 0.0, step=0.5)
r = st.sidebar.slider("Poloměr [m]", 1.0, 20.0, 5.0, step=0.5)
n = st.sidebar.slider("Počet bodů", 3, 500, 10, step=1)
barva = st.sidebar.selectbox("Barva bodů", ["blue", "red", "green", "purple", "orange"])

# --- Výpočet bodů ---
x, y = [], []
for i in range(n):
    angle = 2 * math.pi * i / n
    x.append(x0 + r * math.cos(angle))
    y.append(y0 + r * math.sin(angle))

# --- Vykreslení ---
fig, ax = plt.subplots(figsize=(6,6))
ax.scatter(x, y, c=barva, s=60, edgecolors="black")
ax.set_aspect('equal')
ax.set_xlabel("X [m]")
ax.set_ylabel("Y [m]")
ax.set_title(f"{n} bodů na kružnici\n(střed=({x0}, {y0}), poloměr={r} m)")
ax.grid(True)

st.pyplot(fig)

# --- Uložení obrázku ---
if st.button("💾 Uložit obrázek jako PNG"):
    fig.savefig("kruh.png")
    st.success("✅ Obrázek byl uložen jako 'kruh.png'")

