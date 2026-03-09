import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import math

# 1. Configuración
st.set_page_config(page_title="Pizarrón Interactivo", layout="centered")
st.title("🖍️ Pizarrón: Distribución de Medias")

# 2. Datos principales
col1, col2, col3 = st.columns(3)
with col1:
    mu = st.number_input("Media (μ)", value=75.0)
with col2:
    sigma = st.number_input("Desviación estándar (σ)", value=10.0)
with col3:
    n = st.number_input("Muestra (n)", value=25, min_value=1)

error_est = sigma / math.sqrt(n)

st.markdown("---")

# 3. Menú interactivo
tipo_calculo = st.radio(
    "¿Qué tipo de probabilidad quieres calcular?",
    ("Entre dos valores", "Menor que (<)", "Mayor que (>)"),
    horizontal=True
)

# 4. Lógica dinámica
x1, x2, z1, z2 = None, None, None, None
x_val, z_val = None, None

if tipo_calculo == "Entre dos valores":
    col4, col5 = st.columns(2)
    with col4: x1 = st.number_input("Límite inferior (x1)", value=70.0)
    with col5: x2 = st.number_input("Límite superior (x2)", value=78.0)
    
    # Asegurar orden correcto
    if x1 > x2: x1, x2 = x2, x1
    
    z1 = (x1 - mu) / error_est
    z2 = (x2 - mu) / error_est
    probabilidad = norm.cdf(z2) - norm.cdf(z1)

elif tipo_calculo == "Menor que (<)":
    x_val = st.number_input("Calcular probabilidad de que sea MENOR a:", value=74.0)
    z_val = (x_val - mu) / error_est
    probabilidad = norm.cdf(z_val)

else: # Mayor que (>)
    x_val = st.number_input("Calcular probabilidad de que sea MAYOR a:", value=76.0)
    z_val = (x_val - mu) / error_est
    probabilidad = 1 - norm.cdf(z_val)

st.subheader(f"✨ Probabilidad Total = {probabilidad:.4f} ({probabilidad*100:.2f}%)")

# 5. Gráficas estilo Pizarrón - SOLUCIÓN PARA SUPERPOSICIÓN
with plt.xkcd():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    color_pluma = '#2b5b84'
    
    x_eje = np.linspace(mu - 4*error_est, mu + 4*error_est, 500)
    z_eje = np.linspace(-4, 4, 500)
    
    # Campanas base
    ax1.plot(x_eje, norm.pdf(x_eje, mu, error_est), color=color_pluma, linewidth=2)
    ax2.plot(z_eje, norm.pdf(z_eje, 0, 1), color=color_pluma, linewidth=2)
    ax1.axhline(0, color=color_pluma, linewidth=2)
    ax2.axhline(0, color=color_pluma, linewidth=2)

    # Variables de padding vertical (cuánto separar del eje horizontal)
    y_baja = -0.02 * norm.pdf(mu, mu, error_est) # Para el centro (μ, 0)
    y_alta = -0.10 * norm.pdf(mu, mu, error_est) # Para los valores (x, z) - ¡Mucho más baja!

    # Sombrear y etiquetar según la selección
    if tipo_calculo == "Entre dos valores":
        # Área Real
        x_fill = np.linspace(x1, x2, 100)
        ax1.fill_between(x_fill, norm.pdf(x_fill, mu, error_est), 0, facecolor='none', edgecolor=color_pluma, hatch='////')
        
        # Etiquetas Real (Estrategia de Staggering y Alineación Dinámica)
        ax1.set_xticks([]) # Desactivar etiquetas automáticas
        
        # Media (baja, al centro)
        ax1.text(mu, y_baja, f'μ={mu:.1f}', color=color_pluma, ha='center', va='top', fontsize=12)
        
        # x1 (izquierda, alta, alineación derecha)
        ax1.text(x1, y_alta, f'x1={x1:.1f}', color=color_pluma, ha='right', va='top', rotation=45, fontsize=12)
        
        # x2 (derecha, alta, alineación izquierda)
        ax1.text(x2, y_alta, f'x2={x2:.1f}', color=color_pluma, ha='left', va='top', rotation=45, fontsize=12)

        # Área Z
        z_fill = np.linspace(z1, z2, 100)
        ax2.fill_between(z_fill, norm.pdf(z_fill, 0, 1), 0, facecolor='none', edgecolor=color_pluma, hatch='////')
        
        # Etiquetas Z (Estrategia de Staggering y Alineación Dinámica)
        ax2.set_xticks([]) # Desactivar etiquetas automáticas
        
        # Centro 0 (baja, al centro)
        ax2.text(0, -0.02, '0', color=color_pluma, ha='center', va='top', fontsize=12, fontweight='bold')
        
        # z1 (izquierda, alta, alineación derecha)
        ax2.text(z1, -0.10, f'z1={z1:.2f}', color=color_pluma, ha='right', va='top', rotation=45, fontsize=12)
        
        # z2 (derecha, alta, alineación izquierda)
        ax2.text(z2, -0.10, f'z2={z2:.2f}', color=color_pluma, ha='left', va='top', rotation=45, fontsize=12)

    elif tipo_calculo == "Menor que (<)":
        # Área Real
        x_fill = np.linspace(mu - 4*error_est, x_val, 100)
        ax1.fill_between(x_fill, norm.pdf(x_fill, mu, error_est), 0, facecolor='none', edgecolor=color_pluma, hatch='////')
        ax1.set_xticks([]) # Desactivar etiquetas automáticas
        
        # Etiquetas (Dinámica <)
        # Media (baja, centro)
        ax1.text(mu, y_baja, f'μ={mu:.1f}', color=color_pluma, ha='center', va='top', fontsize=12)
        
        # x (izquierda, alta, alineación derecha)
        ax1.text(x_val, y_alta, f'{x_val:.1f}', color=color_pluma, ha='right', va='top', rotation=45, fontsize=12)

        # Área Z
        z_fill = np.linspace(-4, z_val, 100)
        ax2.fill_between(z_fill, norm.pdf(z_fill, 0, 1), 0, facecolor='none', edgecolor=color_pluma, hatch='////')
        ax2.set_xticks([]) # Desactivar etiquetas automáticas
        
        # Etiquetas (Dinámica <)
        # Centro 0 (baja, centro)
        ax2.text(0, -0.02, '0', color=color_pluma, ha='center', va='top', fontsize=12, fontweight='bold')
        
        # z (izquierda, alta, alineación derecha)
        ax2.text(z_val, -0.10, f'{z_val:.2f}', color=color_pluma, ha='right', va='top', rotation=45, fontsize=12)

    else: # Mayor que (>)
        # Área Real
        x_fill = np.linspace(x_val, mu + 4*error_est, 100)
        ax1.fill_between(x_fill, norm.pdf(x_fill, mu, error_est), 0, facecolor='none', edgecolor=color_pluma, hatch='////')
        ax1.set_xticks([]) # Desactivar etiquetas automáticas
        
        # Etiquetas (Dinámica >)
        # Media (baja, centro)
        ax1.text(mu, y_baja, f'μ={mu:.1f}', color=color_pluma, ha='center', va='top', fontsize=12)
        
        # x (derecha, alta, alineación izquierda)
        ax1.text(x_val, y_alta, f'{x_val:.1f}', color=color_pluma, ha='left', va='top', rotation=45, fontsize=12)

        # Área Z
        z_fill = np.linspace(z_val, 4, 100)
        ax2.fill_between(z_fill, norm.pdf(z_fill, 0, 1), 0, facecolor='none', edgecolor=color_pluma, hatch='////')
        ax2.set_xticks([]) # Desactivar etiquetas automáticas
        
        # Etiquetas (Dinámica >)
        # Centro 0 (baja, centro)
        ax2.text(0, -0.02, '0', color=color_pluma, ha='center', va='top', fontsize=12, fontweight='bold')
        
        # z (derecha, alta, alineación izquierda)
        ax2.text(z_val, -0.10, f'{z_val:.2f}', color=color_pluma, ha='left', va='top', rotation=45, fontsize=12)

    # Limpiar bordes
    for ax in [ax1, ax2]:
        ax.get_yaxis().set_visible(False)
        for espina in ['top', 'right', 'left', 'bottom']: ax.spines[espina].set_visible(False)

    st.pyplot(fig)