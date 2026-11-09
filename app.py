import streamlit as st
st.title("Mi primera aplicación de Streamlit")
st.header('¡Hola profe!')
st.text('Presentación simple')
st.image('logo_uss.png')
st.button('Hazme clic')
texto = st.text_input('Escriba algo:')
st.write('Usted escribió:', texto )
st.sidebar.title('1ra barrera lateral')
st.sidebar.header('¡Hola, profe Mónica!')
st.sidebar.image('logo_uss.png')
text = st.sidebar.text_input('Clic en la barra lateral')
st.sidebar.write('Escribió:', text)

