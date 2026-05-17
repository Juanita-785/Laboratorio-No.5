# -*- coding: utf-8 -*-
"""
Created on Tue May 12 17:44:10 2026

@author: Shara Cetina y Juanita Gomez
"""

import numpy as np
import matplotlib.pyplot as plt
from biosppy.signals import ecg

# ==========================================================
# CARGA DE LA SEÑAL
# ==========================================================

fs = 800

senal_completa = np.loadtxt("ECG_Filtrado_IIR.txt")

# División en segmentos de 120 segundos
punto_corte = 120 * fs

segmento_1 = senal_completa[:punto_corte]
segmento_2 = senal_completa[punto_corte:2*punto_corte]

# ==========================================================
# PROCESAMIENTO ECG Y CÁLCULO RR
# ==========================================================

def procesar_ritmo(segmento, fs):

    out = ecg.ecg(signal=segmento, sampling_rate=fs, show=False)

    rpeaks = out['rpeaks']

    # Intervalos RR
    rr = np.diff(rpeaks) / fs
    tiempo_rr = rpeaks[1:] / fs

    # Filtrado fisiológico
    mask = (rr > 0.45) & (rr < 1.2)

    rr = rr[mask]
    tiempo_rr = tiempo_rr[mask]

    return tiempo_rr, rr, rpeaks


t1, rr1, r1 = procesar_ritmo(segmento_1, fs)
t2, rr2, r2 = procesar_ritmo(segmento_2, fs)

# ==========================================================
# TACOGRAMAS
# ==========================================================

plt.figure(figsize=(12,8))

plt.subplot(2,1,1)
plt.plot(t1, rr1, 'g-o', markersize=3)
plt.title("Tacograma Segmento 1")
plt.ylabel("RR (s)")
plt.grid()

plt.subplot(2,1,2)
plt.plot(t2, rr2, 'r-o', markersize=3)
plt.title("Tacograma Segmento 2")
plt.xlabel("Tiempo (s)")
plt.ylabel("RR (s)")
plt.grid()

plt.tight_layout()
plt.show()

# ==========================================================
# VISUALIZACIÓN DE PICOS R
# ==========================================================

def visualizar_picos(segmento, fs, titulo):

    out = ecg.ecg(signal=segmento, sampling_rate=fs, show=False)

    rpeaks = out['rpeaks']

    tiempo = np.arange(len(segmento)) / fs

    plt.figure(figsize=(14,4))

    plt.plot(tiempo, segmento, label='ECG')

    plt.plot(rpeaks/fs, segmento[rpeaks],'ro',label='Picos R')

    plt.title(titulo)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud[]')

    plt.legend()
    plt.grid(True)
    plt.show()


visualizar_picos(segmento_1, fs, "Picos R Segmento 1")
visualizar_picos(segmento_2, fs, "Picos R Segmento 2")

# ==========================================================
# MÉTRICAS HRV
# ==========================================================

def calcular_metricas_hrv(rr_intervals, nombre_segmento):

    media_rr = np.mean(rr_intervals)

    desviacion_rr = np.std(rr_intervals)

    varianza_rr = np.var(rr_intervals)

    bpm_promedio = 60 / media_rr

    print(f"\n--- Análisis: {nombre_segmento} ---")
    print(f"Media R-R: {media_rr:.4f} s")
    print(f"Desviación Estándar (SDNN): {desviacion_rr:.4f} s")
    print(f"Varianza: {varianza_rr:.6f} s²")
    print(f"Frecuencia Cardíaca Promedio: {bpm_promedio:.1f} BPM")

    return media_rr, desviacion_rr, varianza_rr


metricas1 = calcular_metricas_hrv(rr1, "Segmento 1 (Reposo)")
metricas2 = calcular_metricas_hrv(rr2, "Segmento 2 (Lectura/Actividad)")

# ==========================================================
# COMPARACIÓN HRV
# ==========================================================

labels = ['Media R-R (s)', 'Desv. Estándar (s)']

seg1_vals = [float(metricas1[0]), float(metricas1[1])]
seg2_vals = [float(metricas2[0]), float(metricas2[1])]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(8,5))

ax.bar(x - width/2, seg1_vals, width, label='Segmento 1', color='green')

ax.bar(x + width/2, seg2_vals, width, label='Segmento 2', color='red')

ax.set_ylabel('Tiempo (s)')
ax.set_title('Comparación de Parámetros HRV')

ax.set_xticks(x)
ax.set_xticklabels(labels)

ax.legend()
ax.grid(axis='y')

plt.show()

# ==========================================================
# DIAGRAMA DE POINCARÉ + CSI + CVI
# ==========================================================

def poincare(rr, titulo):

    # RR(n) y RR(n+1)
    x = rr[:-1]
    y = rr[1:]

    # Cálculo SD1 y SD2
    sd1 = np.std((y - x) / np.sqrt(2))
    sd2 = np.std((y + x) / np.sqrt(2))

    # Índices autonómicos
    csi = sd2 / sd1
    cvi = np.log10(sd1 * sd2)

    # ======================================================
    # GRÁFICO
    # ======================================================

    plt.figure(figsize=(6,6))

    plt.scatter(x, y, color='blue', alpha=0.6)

    # Línea identidad
    min_rr = min(np.min(x), np.min(y))
    max_rr = max(np.max(x), np.max(y))

    plt.plot([min_rr, max_rr],[min_rr, max_rr],'r--',label='y = x')

    plt.title(f'Diagrama de Poincaré - {titulo}')

    plt.xlabel('RR(n) [s]')
    plt.ylabel('RR(n+1) [s]')

    plt.grid(True)
    plt.axis('equal')

    texto = (
        f"SD1 = {sd1:.4f} s\n"
        f"SD2 = {sd2:.4f} s\n"
        f"CSI = {csi:.4f}\n"
        f"CVI = {cvi:.4f}"
    )

    plt.text(0.05, 0.95, texto, transform=plt.gca().transAxes, fontsize=10, verticalalignment='top', bbox=dict(facecolor='white',alpha=0.8))

    plt.legend()
    plt.show()

    # ======================================================
    # RESULTADOS
    # ======================================================

    print(f"\n--- {titulo} ---")
    print(f"SD1: {sd1:.4f} s")
    print(f"SD2: {sd2:.4f} s")
    print(f"CSI (actividad simpática): {csi:.4f}")
    print(f"CVI (actividad vagal): {cvi:.4f}")

    return sd1, sd2, csi, cvi


# Diagramas de Poincaré
resultados_1 = poincare(rr1, "Segmento 1 (Reposo)")
resultados_2 = poincare(rr2, "Segmento 2 (Lectura/Actividad)")