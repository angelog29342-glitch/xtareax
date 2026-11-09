import streamlit as st
st.title("Mi primera aplicación de Streamlit")
st.header('¡Hola profe!')
st.text('Presentación simple')

st.button('Hazme clic')
texto = st.text_input('Escriba algo:')
st.write('Usted escribió:', texto )
st.sidebar.title('1ra barrera lateral')
st.sidebar.head('¡Hola, profe Mónica!')
