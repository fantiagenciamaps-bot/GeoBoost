import streamlit as st
import pandas as pd
import pydeck as pdk

# Configuración de la página
st.set_page_config(page_title="GeoBoost - Google Business Console", page_icon="🌐", layout="wide")

# Inyección de Estilos CSS - Estricto Google Material Design (Light Workspace)
st.markdown("""
    <style>
    /* Fondo general blanco puro estilo Google Workspace */
    .stApp {
        background-color: #ffffff;
        color: #202124;
        font-family: 'Roboto', sans-serif;
    }
    
    /* Barra lateral limpia y minimalista */
    [data-testid="stSidebar"] {
        background-color: #f8f9fa;
        border-right: 1px solid #dadce0;
    }
    
    /* Tarjetas de métricas y contenedores estilo Google */
    div.stMarkdown container, div.row-widget {
        background-color: #ffffff;
        border: 1px solid #dadce0;
        border-radius: 8px;
        padding: 15px;
    }

    /* Botones principales estilo Google Blue */
    .stButton>button {
        background-color: #1a73e8;
        color: white;
        border-radius: 4px;
        border: none;
        font-weight: 500;
        padding: 6px 16px;
        box-shadow: 0 1px 2px 0 rgba(60,64,67,0.3);
    }
    .stButton>button:hover {
        background-color: #1557b0;
        color: white;
    }
    
    /* Inputs y selects limpios */
    input, select, textarea {
        border-radius: 4px !important;
        border: 1px solid #dadce0 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Encabezado corporativo estilo Google Cloud / Business Profile
col_logo, col_title, col_user = st.columns([0.5, 4, 1])
with col_logo:
    st.markdown("### 🌐")
with col_title:
    st.markdown("### GeoBoost Console")
    st.caption("Panel de administración y automatización para comercios locales")
with col_user:
    st.markdown("👤 **Admin San Justo**")

st.markdown("<hr style='border: 1px solid #dadce0; margin-top: 0px;'>", unsafe_allow_html=True)

# Barra lateral de navegación
st.sidebar.header("Navegación")
zona = st.sidebar.selectbox("Ubicación Activa", ["San Justo Centro", "San Justo Oeste", "Ramos Mejía", "Morón"])
seccion = st.sidebar.radio("Módulos", ["🗺️ Radar Google Maps", "📊 Pipeline Comercial", "💬 Mensajería y Bots", "🔍 Auditor de Fichas", "⚙️ Estado del Sistema"])

# Base de datos simulada de comercios en San Justo
df_comercios = pd.DataFrame({
    'comercio': ['Ferretería San Justo', 'Kiosco El Paso', 'Pizzería La Strada', 'Indumentaria M&M'],
    'rubro': ['Ferretería', 'Kiosco', 'Gastronomía', 'Moda'],
    'estado': ['Sin respuesta a reseñas', 'Fotos viejas', 'Perfil incompleto', 'Optimizado'],
    'lat': [-34.6830, -34.6870, -34.6810, -34.6855],
    'lon': [-58.5580, -58.5620, -58.5550, -58.5600],
    'color': [[234, 67, 53, 220], [234, 67, 53, 220], [251, 188, 5, 220], [52, 168, 83, 220]]
})

if seccion == "🗺️ Radar Google Maps":
    st.subheader(f"📍 Mapeo de Fichas - {zona}")
    
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
        
        r = pdk.Deck(
            layers=[layer],
            initial_view_state=view_state,
            tooltip={"text": "Comercio: {comercio}\nRubro: {rubro}\nEstado: {estado}"},
        )
        st.pydeck_chart(r, use_container_width=True)
        st.caption("🔍 Visualización interactiva basada en los colores corporativos de Google.")

    with col_info:
        st.markdown("### 📋 Directorio Local")
        for index, row in df_comercios.iterrows():
            with st.expander(f"{row['comercio']} ({row['rubro']})"):
                st.markdown(f"**Diagnóstico:** {row['estado']}")
                if st.button(f"Enviar Auditoría", key=f"btn_{index}"):
                    st.success(f"¡Reporte enviado a {row['comercio']}!")

elif seccion == "📊 Pipeline Comercial":
    st.subheader(f"📈 Embudo de Ventas - {zona}")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("#### 📥 Detectados")
        st.info("Ferretería San Justo\n*Ferretería*")
    with col2:
        st.markdown("#### 📤 Auditados")
        st.success("Pizzería La Strada\n*Gastronomía*")
    with col3:
        st.markdown("#### 🔥 Leads Calientes")
        st.warning("**Indumentaria M&M**\n*Interesado ($17.500)*")
    with col4:
        st.markdown("#### 💰 Cerrados")
        st.markdown("✅ *Ninguno activo*")

elif seccion == "💬 Mensajería y Bots":
    st.subheader("💬 Centro de Mensajería (WhatsApp Business)")
    lead_sel = st.selectbox("Conversación activa:", ["Indumentaria M&M (+54 9 11 1122-3344)"])
    st.text_area("Historial:", value="[Bot]: Hola! Auditamos el perfil de Google Maps...\n[Cliente]: Hola, cuánto sale?", height=140, disabled=True)
    
    modo = st.radio("Control de sesión:", ["🤖 IA Automática", "👤 Humano (Intervenir)"])
    if "Humano" in modo:
        st.warning("Control manual activo para esta línea.")
        st.text_input("Respuesta rápida:")
        st.button("Enviar Mensaje")

elif seccion == "🔍 Auditorer de Fichas":
    st.subheader("🔍 Analizador de Perfiles Google Maps")
    url = st.text_input("URL del perfil de negocio:")
    if st.button("Ejecutar Diagnóstico"):
        st.success("Auditoría completada con éxito. Formulario Tally adjunto.")

else:
    st.subheader("⚙️ Estado de la Infraestructura")
    st.success("🟢 Red de Líneas WhatsApp: Conectada")
    st.success("🟢 Scraper Geográfico: Sincronizado")
    
    c1, c2 = st.columns(2)
    c1.metric("Fichas Escaneadas", "42")
    c2.metric("Conversiones", "5")
