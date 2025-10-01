import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from fpdf import FPDF
import tempfile
import os

st.title("Body na kružnici")

# Vstupy
x_center = st.number_input("Souřadnice středu X", value=0.0)
y_center = st.number_input("Souřadnice středu Y", value=0.0)
radius = st.number_input("Poloměr kružnice (m)", value=5.0, min_value=0.1)
points = st.number_input("Počet bodů", min_value=1, value=8)
color = st.color_picker("Barva bodů", "#ff0000")

# Výpočet bodů
angles = np.linspace(0, 2*np.pi, int(points), endpoint=False)
x_points = x_center + radius * np.cos(angles)
y_points = y_center + radius * np.sin(angles)

# Vykreslení grafu
fig, ax = plt.subplots()
ax.plot(x_points, y_points, "o", color=color)
circle = plt.Circle((x_center, y_center), radius, fill=False, linestyle="--")
ax.add_artist(circle)
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_aspect("equal", adjustable="box")
ax.grid(True)

st.pyplot(fig)

# Info o autorovi
if st.checkbox("O aplikaci a autorovi"):
    st.write("""
    **Autor:** Martin Růžička  
    **Kontakt:** martin1.ruzicka@seznam.cz  
    **Použité technologie:** Python, Streamlit, Matplotlib, FPDF  
    """)

# Export do PDF
if st.button("Uložit do PDF"):
    tmpfile = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    fig.savefig(tmpfile.name)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, "Body na kruznici - Report", ln=True, align="C")
    pdf.cell(200, 10, f"Stred: ({x_center}, {y_center})", ln=True)
    pdf.cell(200, 10, f"Polomer: {radius} m", ln=True)
    pdf.cell(200, 10, f"Pocet bodu: {points}", ln=True)
    pdf.cell(200, 10, f"Barva bodu: {color}", ln=True)
    pdf.cell(200, 10, "Autor: Jan Novák", ln=True)
    pdf.cell(200, 10, "Kontakt: jan.novak@email.cz", ln=True)
    pdf.image(tmpfile.name, x=50, y=80, w=100)

    pdf_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf.output(pdf_file.name)

    with open(pdf_file.name, "rb") as f:
        st.download_button("Stáhnout PDF", f, file_name="report.pdf")

    os.unlink(tmpfile.name)
    os.unlink(pdf_file.name)
