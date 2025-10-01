!pip install streamlit -q

import streamlit as st
import matplotlib.pyplot as plt
import math

st.title("🎯 Body na kružnici")

# --- Ovládací posuvníky ---
x0 = st.slider("Střed X (m)", -20.0, 20.0, 0.0, step=0.5)
y0 = st.slider("Střed Y (m)", -20.0, 20.0, 0.0, step=0.5)
r = st.slider("Poloměr (m)", 1.0, 20.0, 5.0, step=0.5)
n = st.slider("Počet bodů", 3, 500, 10, step=1)
barva = st.selectbox("Barva bodů", ["blue", "red", "green", "purple", "orange"])

# --- Výpočet bodů ---
x, y = [], []
for i in range(n):
    angle = 2 * math.pi * i / n
    x.append(x0 + r * math.cos(angle))
    y.append(y0 + r * math.sin(angle))

# --- Vykreslení ---
fig, ax = plt.subplots(figsize=(6,6))
ax.scatter(x, y, c=barva)
ax.set_aspect('equal')
ax.set_xlabel("X [m]")
ax.set_ylabel("Y [m]")
ax.set_title(f"{n} bodů na kružnici (střed=({x0},{y0}), poloměr={r} m)")
ax.grid(True)

st.pyplot(fig)

# --- Uložení obrázku ---
if st.button("💾 Uložit obrázek"):
    fig.savefig("kruh.png")
    st.success("✅ Obrázek uložen jako kruh.png")
