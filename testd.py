import streamlit as st

st.title("Containers con clases personalizadas")

# Definir clases CSS personalizadas
st.markdown("""
<style>
/* Clase para recuadro rojo */
.red-container {
    border: 3px solid #ff3333 !important;
    border-radius: 15px !important;
    padding: 25px !important;
    background: linear-gradient(135deg, #fff5f5, #ffe6e6) !important;
    margin: 20px 0 !important;
    box-shadow: 0 4px 12px rgba(255, 0, 0, 0.1) !important;
}

/* Clase para recuadro azul */
.st-emotion-cache-3uj0rx et2rgd20 {
    border: 3px solid #3366ff !important;
    border-radius: 15px !important;
    padding: 25px !important;
    background: linear-gradient(135deg, #f0f5ff, #e6ecff) !important;
    margin: 20px 0 !important;
    box-shadow: 0 4px 12px rgba(0, 100, 255, 0.1) !important;
}

/* Clase para recuadro verde */
.green-container {
    border: 3px solid #33cc33 !important;
    border-radius: 15px !important;
    padding: 25px !important;
    background: linear-gradient(135deg, #f5fff0, #e6ffe6) !important;
    margin: 20px 0 !important;
}
</style>
""", unsafe_allow_html=True)

# Container con clase roja
st.markdown('<div class="red-container">', unsafe_allow_html=True)
with st.container():
    st.write("## 🎯 Panel Principal")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Guardar", use_container_width=True):
            st.success("Guardado")
    with col2:
        if st.button("🗑️ Eliminar", use_container_width=True):
            st.warning("Eliminado")
st.markdown('</div>', unsafe_allow_html=True)

# Container con clase azul
st.markdown('<div class="st-emotion-cache-3uj0rx et2rgd20">', unsafe_allow_html=True)
with st.container():
    st.write("## 📊 Estadísticas")
    st.metric("Usuarios", "1,234", "+12%")
    st.metric("Ingresos", "$45,678", "+8%")
    st.metric("Conversión", "3.4%", "-0.2%")
st.markdown('</div>', unsafe_allow_html=True)

# Container con clase verde
st.markdown('<div class="green-container">', unsafe_allow_html=True)
with st.container():
    st.write("## ⚙️ Configuración")
    st.checkbox("Notificaciones por email")
    st.checkbox("Notificaciones push")
    st.checkbox("Modo oscuro")
st.markdown('</div>', unsafe_allow_html=True)
