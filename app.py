import streamlit as st
st.title("Mi primera aplicación de Streamlit")
st.header('¡Hola profe!')
st.text('Presentación simple')

st.button('Hazme clic')
texto = st.text_input('Escriba algo:')
st.write('Usted escribió:', texto )
