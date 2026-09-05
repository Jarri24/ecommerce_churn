import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración de la página web
st.set_page_config(page_title="Churn Prediction Dashboard", page_icon="🛒", layout="wide")

# Título principal
st.title("🛒 Dashboard de Predicción de Fuga de Clientes (E-Commerce)")
st.markdown("Esta aplicación permite identificar proactivamente a los clientes con alta probabilidad de abandono y visualizar los factores críticos de negocio.")

# Métricas principales en columnas (KPIs)
col1, col2, col3 = st.columns(3)
col1.metric(label="📊 Volumen Analizado", value="3,941 Clientes")
col2.metric(label="🎯 Precisión Global", value="93.66%")
col3.metric(label="🔍 Tasa de Captura (Recall)", value="74.00%")

st.markdown("---")

# Sección de Factores Críticos (Feature Importance)
st.subheader("💡 Factores Principales de Fuga (Insights de Negocio)")
st.write("El análisis del modelo Random Forest demuestra que la antigüedad del cliente (**Tenure**) y los beneficios económicos (**CashbackAmount**) son los principales impulsores de la retención.")

# Cargamos la imagen del gráfico que guardamos antes
try:
    st.image('reports/feature_importance.png', caption='Top 10 Factores Críticos de Churn', use_container_width=True)
except:
    st.info("Asegúrate de haber generado el gráfico en tu notebook.")

# Sidebar interactivo (Simulador rápido)
st.sidebar.header("⚙️ Opciones de Simulación")
st.sidebar.text("Próximamente: Simulador de riesgo de cliente individual.")