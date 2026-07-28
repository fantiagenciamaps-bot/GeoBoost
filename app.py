import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="GeoBoost - Panel de Control", page_icon="🚀", layout="wide")

st.title("🚀 GeoBoost | Panel de Automatización Comercial")
st.markdown("Sistema autónomo de prospección, auditoría y conversión para comercios locales.")

# Barra lateral de navegación
st.sidebar.header("Menú de Control")
zona = st.sidebar.selectbox("Zona objetivo", ["San Justo", "Ramos Mejía", "Morón", "San Justo Centro"])
accion = st.sidebar.radio("Sección", ["Ver Leads / CRM", "Auditoría Express", "Estado de la Red"])

if accion == "Ver Leads / CRM":
    st.subheader(f"📊 Leads Activos en {zona}")
    
    # Datos de ejemplo de comercios locales detectados
    data = {
        "Comercio": ["Ferretería San Justo", "Kiosco El Paso", "Pizzería La Strada", "Indumentaria M&M"],
        "Rubro": ["Ferretería", "Kiosco", "Gastronomía", "Moda"],
        "Estado Google Maps": ["Sin respuestas a reseñas", "Fotos viejas", "Perfil incompleto", "Optimizado"],
        "WhatsApp": ["+54 9 11 2345-6789", "+54 9 11 9876-5432", "+54 9 11 5555-4444", "+54 9 11 1122-3344"],
        "Estado Bot": ["Auditoría enviada", "Pendiente", "Preventa abierta", "Cerrado ($197)"]
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

elif accion == "Auditoría Express":
    st.subheader("🔍 Auditoría Automática de Google Maps")
    url_maps = st.text_input("Pegá el link del perfil de Google Maps del comercio:")
    
    if st.button("Ejecutar Auditoría"):
        if url_maps:
            st.success("¡Análisis completado con éxito!")
            st.markdown("---")
            st.markdown("### 📋 Resultados del Diagnóstico:")
            st.markdown("- **Reseñas:** Se detectaron 4 opiniones negativas sin responder.")
            st.markdown("- **Multimedia:** Las fotos principales tienen más de 2 años de antigüedad.")
            st.markdown("- **Información:** Faltan horarios especiales actualizados.")
            st.info("💡 Sugerencia: El sistema ya preparó el mensaje personalizado para enviar por WhatsApp con estos datos.")
        else:
            st.warning("Por favor, ingresá una URL válida de Google Maps.")

else:
    st.subheader("⚙️ Estado de la Infraestructura")
    st.success("Bot de WhatsApp (Líneas principales): Conectado y Operativo")
    st.success("Scraper de Leads / Google Maps: Sincronizado")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Leads Escaneados Hoy", "38")
    col2.metric("Auditorías Enviadas", "14")
    col3.metric("Respuestas Recibidas", "5")
