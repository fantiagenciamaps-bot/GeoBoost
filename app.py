import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="GeoBoost - Centro de Comando", page_icon="⚡", layout="wide")

st.title("⚡ GeoBoost | Centro de Comando & Operación Autónoma")
st.markdown("Sistema híbrido de prospección local, auditoría de Google Maps e intervención en vivo.")

# Barra lateral de navegación
st.sidebar.header("Panel de Control")
zona = st.sidebar.selectbox("Zona Activa", ["San Justo Centro", "San Justo Oeste", "Ramos Mejía", "Morón"])
seccion = st.sidebar.radio("Módulos", ["📊 Embudo Comercial (Kanban)", "💬 Chat en Vivo / Intervención", "🔍 Auditoría Express", "⚙️ Estado del Sistema"])

if seccion == "📊 Embudo Comercial (Kanban)":
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
    
    st.markdown(f"---")
    st.markdown(f"**Historial de chat con: {lead_seleccionado}**")
    
    # Simulación de chat activo
    st.text_area("Historial de mensajes:", value="[Bot 21:00]: Hola! Estuvimos auditando el perfil de Google Maps de Indumentaria M&M y detectamos oportunidades para subir en el ranking local.\n[Cliente 21:05]: Hola, cómo es eso? Cuánto cuesta?", height=150, disabled=True)
    
    modo_control = st.radio("Modo de operación para este chat:", ["🤖 Bot Automático Activo", "👤 Intervención Humana (Tomar el control)"])
    
    if "Humana" in modo_control:
        st.error("⚠️ Bot pausado para este comercio. Estás operando de forma manual.")
        respuesta_manual = st.text_input("Escribir respuesta por WhatsApp:")
        if st.button("Enviar Respuesta Manual"):
            st.success("¡Mensaje enviado al cliente por WhatsApp con éxito!")
    else:
        st.info("🤖 El bot de inteligencia artificial está respondiendo automáticamente según el embudo.")

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
