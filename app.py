import streamlit as st
import pandas as pd
import pydeck as pdk

# Configuración de la página
st.set_page_config(page_title="GeoBoost - Centro de Comando", page_icon="⚡", layout="wide")

# Estilos CSS Material Design limpios
st.markdown("""
    <style>
    .stApp {
        background-color: #f8f9fa;
        color: #202124;
    }
    .stButton>button {
        background-color: #1a73e8;
        color: white;
        border-radius: 4px;
        border: none;
        font-weight: 500;
    }
    .stButton>button:hover {
        background-color: #1557b0;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ GeoBoost | Centro de Comando & Operación Autónoma")
st.markdown("Sistema autónomo de prospección local, auditoría de Google Maps e intervención en vivo.")

# Barra lateral de navegación
st.sidebar.header("Panel de Control")
zona = st.sidebar.selectbox("Zona Activa", ["San Justo Centro", "San Justo Oeste", "Ramos Mejía", "Morón"])
seccion = st.sidebar.radio("Módulos", ["🗺️ Mapa Geoespacial (Estilo Maps)", "📊 Embudo Comercial (Kanban)", "💬 Chat en Vivo / Intervención", "🔍 Auditoría Express", "⚙️ Estado del Sistema"])

# Base de datos simulada de comercios geolocalizados en San Justo
df_comercios = pd.DataFrame({
    'comercio': ['Ferretería San Justo', 'Kiosco El Paso', 'Pizzería La Strada', 'Indumentaria M&M'],
    'rubro': ['Ferretería', 'Kiosco', 'Gastronomía', 'Moda'],
    'estado': ['Sin respuesta a reseñas', 'Fotos viejas', 'Perfil incompleto', 'Optimizado'],
    'lat': [-34.6830, -34.6870, -34.6810, -34.6855],
    'lon': [-58.5580, -58.5620, -58.5550, -58.5600],
    'color': [[234, 67, 53, 220], [234, 67, 53, 220], [251, 188, 5, 220], [52, 168, 83, 220]]
})

if seccion == "🗺️ Mapa Geoespacial (Estilo Maps)":
    st.subheader(f"🗺️ Radar Geoespacial y Fichas Activas - {zona}")
    
    col_mapa, col_info = st.columns([2, 1])
    
    with col_mapa:
        layer = pdk.Layer(
            "ScatterplotLayer",
            data=df_comercios,
            get_position=["lon", "lat"],
            get_color="color",
            get_radius=180,
            pickable=True,
            auto_highlight=True,
        )
        
        view_state = pdk.ViewState(
            latitude=-34.6845,
            longitude=-58.5585,
            zoom=14,
            pitch=0,
        )
        
        # Usamos mapa base nativo sin requerir tokens de Mapbox externos
        r = pdk.Deck(
            layers=[layer],
            initial_view_state=view_state,
            tooltip={"text": "Comercio: {comercio}\nRubro: {rubro}\nEstado: {estado}"},
        )
        st.pydeck_chart(r, use_container_width=True)
        st.caption("💡 Mapa interactivo operativo para San Justo.")

    with col_info:
        st.markdown("### 📋 Listado de Locales")
        for index, row in df_comercios.iterrows():
            with st.expander(f"{row['comercio']} ({row['rubro']})"):
                st.markdown(f"**Estado Maps:** {row['estado']}")
                if st.button(f"Enviar Auditoría", key=f"btn_{index}"):
                    st.success(f"¡Diagnóstico enviado por WhatsApp a {row['comercio']}!")

elif seccion == "📊 Embudo Comercial (Kanban)":
    st.subheader(f"📈 Pipeline de Conversión - {zona}")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("### 📥 Detectados")
        st.info("Ferretería San Justo\n*Rubro: Ferretería*\n*Estado: Sin respuesta a reseñas*")
        st.info("Kiosco El Paso\n*Rubro: Kiosco*\n*Estado: Fotos antiguas*")
    with col2:
        st.markdown("### 📤 Auditoría Enviada")
        st.success("Pizzería La Strada\n*Rubro: Gastronomía*\n*Estado: Mensaje entregado*")
    with col3:
        st.markdown("### 🔥 Leads Calientes")
        st.warning("**Indumentaria M&M**\n*Rubro: Moda*\n*Preguntó precio del Plan Start ($17.500)*")
    with col4:
        st.markdown("### 💰 Cerrados")
        st.markdown("✅ *Ninguno en este lote todavía*")

elif seccion == "💬 Chat en Vivo / Intervención":
    st.subheader("💬 Bandeja de Entrada en Tiempo Real (WhatsApp / Bot)")
    
    lead_seleccionado = st.selectbox("Seleccioná un comercio para ver la conversación:", 
                                   ["Indumentaria M&M (+54 9 11 1122-3344)", "Pizzería La Strada (+54 9 11 5555-4444)"])
    
    st.markdown("---")
    st.markdown(f"**Historial de chat con: {lead_seleccionado}**")
    
    st.text_area("Historial de mensajes:", value="[Bot 21:00]: Hola! Estuvimos auditando el perfil de Google Maps y detectamos oportunidades.\n[Cliente 21:05]: Hola, cuánto cuesta?", height=150, disabled=True)
    
    modo_control = st.radio("Modo de operación para este chat:", ["🤖 Bot Automático Activo", "👤 Intervención Humana (Tomar el control)"])
    
    if "Humana" in modo_control:
        st.error("⚠️ Bot pausado para este comercio. Estás operando de forma manual.")
        respuesta_manual = st.text_input("Escribir respuesta por WhatsApp:")
        if st.button("Enviar Respuesta Manual"):
            st.success("¡Mensaje enviado al cliente por WhatsApp con éxito!")
    else:
        st.info("🤖 El bot de inteligencia artificial está respondiendo automáticamente.")

elif seccion == "🔍 Auditoría Express":
    st.subheader("🔍 Generador de Diagnóstico de Google Maps")
    url_maps = st.text_input("Pegá el link del perfil de Google Maps:")
    
    if st.button("Analizar Perfil"):
        if url_maps:
            st.success("¡Auditoría generada con éxito!")
            st.markdown("- **Reseñas Negativas:** 2 sin responder.")
            st.markdown("- **Multimedia:** Falta actualizar fotos del local.")
            st.info("💡 Link al Formulario de Admisión (Tally) listo para disparar por WhatsApp.")
        else:
            st.warning("Ingresá una URL válida.")

else:
    st.subheader("⚙️ Estado de la Infraestructura y Conexiones")
    st.success("🟢 Líneas de WhatsApp (SIMs Claro/Personal): Conectadas")
    st.success("🟢 Scraper de Leads (Apify / Outscraper): Operativo")
    st.success("🟢 Webhooks y Google Sheets: Sincronizados")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Leads Escaneados Hoy", "42")
    c2.metric("Auditorías en Curso", "15")
    c3.metric("Tasa de Respuesta", "31%")
