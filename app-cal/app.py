import streamlit as st

st.set_page_config(page_title="Calculadora de Preço", page_icon="??", layout="centered")

st.title("?? Calculadora de Preço de Venda")
st.write("Calcule o preço ideal de venda considerando custos, despesas e lucro desejado.")

custo = st.number_input("Custo do produto (R$):", min_value=0.0, value=100.0, step=10.0)
despesas = st.number_input("Porcentagem de despesas/impostos (%):", min_value=0.0, max_value=99.0, value=0.0, step=1.0)
lucro = st.number_input("Porcentagem de lucro desejada (%):", min_value=0.0, max_value=99.0, value=30.0, step=1.0)

if st.button("Calcular Preço de Venda", use_container_width=True):
    divisor = 1 - ((despesas + lucro) / 100)
    
    if divisor <= 0:
        st.error("?? A soma das despesas e do lucro é muito alta! O preço ficaria infinito ou negativo.")
    else:
        preco_venda = custo / divisor
        st.success(f"### Você deve vender por: **R$ {preco_venda:.2f}**")