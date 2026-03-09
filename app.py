import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import math

# 1. Configuración de la página
st.set_page_config(page_title="Pizarrón Interactivo", layout="centered")
st.title("🖍️ Pizarrón: Distribución de Medias")

# 2. Entradas del usuario (con los datos del pizarrón por defecto)
col1, col2, col3 = st.columns(3)
with col1:
    mu = st.number_input("Media (μ)", value=75.0)
with col2:
    sigma = st.number_input("Desviación (σ)", value=10.0)
with col3:
    n = st.number_input("Muestra (n)", value=25, min_value=1)

col4, col5 = st.columns(2)
with col4:
    x1 = st.number_input("Límite inferior", value=70.0)
with col5:
    x2 = st.number_input("Límite superior", value=78.0)

# 3. Cálculos
error_est = sigma / math.sqrt(n)
z1 = (x1 - mu) / error_est
z2 = (x2 - mu) / error_est

# Calcular las áreas divididas (como en el pizarrón)
area_izq = norm.cdf(0) - norm.cdf(z1)
area_der = norm.cdf(z2) - norm.cdf(0)
area_total = area_izq + area_der

st.markdown("---")
st.subheader(f"Área Total = {area_izq:.4f} + {area_der:.4f} = {area_total:.4f} ({area_total*100:.1f}%)")

# 4. Gráficas estilo Pizarrón
with plt.xkcd():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    color_pluma = '#2b5b84' # Azul tipo plumón
    
    # --- GRÁFICA 1: VALORES REALES ---
    x_eje = np.linspace(mu - 4*error_est, mu + 4*error_est, 500)
    y_eje = norm.pdf(x_eje, mu, error_est)
    
    ax1.plot(x_eje, y_eje, color=color_pluma, linewidth=2)
    ax1.axhline(0, color=color_pluma, linewidth=2)
    
    # Sombrear área real
    x_fill = np.linspace(x1, x2, 100)
    ax1.fill_between(x_fill, norm.pdf(x_fill, mu, error_est), 0, facecolor='none', edgecolor=color_pluma, hatch='////')
    
    # Etiquetas inferiores idénticas al pizarrón
    ax1.set_xticks([x1, mu, x2])
    ax1.set_xticklabels([f'x1={x1}', f'μ={mu}', f'x2={x2}'], color=color_pluma, fontsize=12)
    ax1.tick_params(axis='x', colors=color_pluma, length=5, direction='inout')
    
    # Limpiar bordes
    ax1.get_yaxis().set_visible(False)
    for espina in ['top', 'right', 'left', 'bottom']: ax1.spines[espina].set_visible(False)

    # --- GRÁFICA 2: VALORES Z ---
    z_eje = np.linspace(-4, 4, 500)
    z_y_eje = norm.pdf(z_eje, 0, 1)
    
    ax2.plot(z_eje, z_y_eje, color=color_pluma, linewidth=2)
    ax2.axhline(0, color=color_pluma, linewidth=2)
    
    # Línea central dividiendo las áreas
    ax2.vlines(0, 0, norm.pdf(0,0,1), color=color_pluma, linewidth=1.5)
    
    # Sombrear área Z (izquierda y derecha)
    z_fill_izq = np.linspace(z1, 0, 50)
    z_fill_der = np.linspace(0, z2, 50)
    ax2.fill_between(z_fill_izq, norm.pdf(z_fill_izq, 0, 1), 0, facecolor='none', edgecolor=color_pluma, hatch='////')
    ax2.fill_between(z_fill_der, norm.pdf(z_fill_der, 0, 1), 0, facecolor='none', edgecolor=color_pluma, hatch='////')
    
    # Escribir los valores de las áreas ADENTRO de la gráfica
    ax2.text(z1/2, 0.05, f'{area_izq:.4f}', ha='center', color=color_pluma, fontsize=11, fontweight='bold')
    ax2.text(z2/2, 0.05, f'{area_der:.4f}', ha='center', color=color_pluma, fontsize=11, fontweight='bold')
    
    # Etiquetas inferiores Z idénticas al pizarrón
    ax2.set_xticks([z1, 0, z2])
    ax2.set_xticklabels([f'z1={z1:.2f}', 'Z=0', f'z2={z2:.2f}'], color=color_pluma, fontsize=12)
    ax2.tick_params(axis='x', colors=color_pluma, length=5, direction='inout')
    
    # Limpiar bordes
    ax2.get_yaxis().set_visible(False)
    for espina in ['top', 'right', 'left', 'bottom']: ax2.spines[espina].set_visible(False)

    st.pyplot(fig)